"""Convierte un extracto de OpenStreetMap (API /map) de Elche en datos compactos para Ilici City.
Uso: python3 osm_to_game.py entrada.osm salida.json
Coordenadas del juego: metros; x hacia el este, z hacia el sur; La Glorieta queda en (55,-55).
Datos © OpenStreetMap contributors (ODbL)."""
import sys, json, math, hashlib
import xml.etree.ElementTree as ET

LAT0, LON0 = 38.2656793, -0.6965317          # plaça Glorieta
KX = 111320 * math.cos(math.radians(LAT0)); KZ = 110950
def to_game(lat, lon): return (55 + (lon - LON0) * KX, -55 - (lat - LAT0) * KZ)
RZ = (-598.0, -312.0, 320.0, 353.0)          # zona real: x0, z0, x1, z1

def inside(p, m=0): return RZ[0]-m <= p[0] <= RZ[2]+m and RZ[1]-m <= p[1] <= RZ[3]+m
def dp(pts, eps):
    if len(pts) < 3: return pts
    (ax, az), (bx, bz) = pts[0], pts[-1]; L = math.hypot(bx-ax, bz-az) or 1e-9
    i, dmax = 0, 0
    for k in range(1, len(pts)-1):
        px, pz = pts[k]; d = abs((bx-ax)*(az-pz) - (ax-px)*(bz-az)) / L
        if d > dmax: i, dmax = k, d
    if dmax > eps: return dp(pts[:i+1], eps)[:-1] + dp(pts[i:], eps)
    return [pts[0], pts[-1]]
def dp_ring(pts, eps):
    """Simplifica un polígono cerrado (sin repetir el primer punto)."""
    if len(pts) < 4: return pts
    k = max(range(len(pts)), key=lambda i: (pts[i][0]-pts[0][0])**2 + (pts[i][1]-pts[0][1])**2)
    a = dp(pts[:k+1], eps); b = dp(pts[k:] + [pts[0]], eps)
    return a[:-1] + b[:-1]
def clip_line(pts):
    """Parte una polilínea en tramos dentro de la zona (recorta en el borde)."""
    out, cur = [], []
    def edge(a, b):
        # punto de cruce con el rectángulo por bisección
        lo, hi = 0.0, 1.0
        ina = inside(a)
        for _ in range(30):
            mid = (lo+hi)/2; p = (a[0]+(b[0]-a[0])*mid, a[1]+(b[1]-a[1])*mid)
            if inside(p) == ina: lo = mid
            else: hi = mid
        t = (lo+hi)/2; return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
    for k, p in enumerate(pts):
        if inside(p):
            if not cur and k > 0: cur.append(edge(pts[k-1], p))
            cur.append(p)
        else:
            if cur:
                cur.append(edge(pts[k-1], p)); out.append(cur); cur = []
    if cur: out.append(cur)
    return [c for c in out if len(c) >= 2]
def area(poly): return abs(sum(poly[i][0]*poly[i-1][1]-poly[i-1][0]*poly[i][1] for i in range(len(poly))))/2
def enc(pts): return [v for p in pts for v in (round(p[0], 1), round(p[1], 1))]
def hsh(s): return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) / 0xffffffff

root = ET.parse(sys.argv[1]).getroot()
N = {n.get('id'): to_game(float(n.get('lat')), float(n.get('lon'))) for n in root.iter('node')}
W = {}
for w in root.iter('way'):
    W[w.get('id')] = ([r.get('ref') for r in w.findall('nd')], {t.get('k'): t.get('v') for t in w.findall('tag')})
def pts_of(refs): return [N[r] for r in refs if r in N]

DRIVE = {'motorway':14,'trunk':14,'primary':12,'secondary':11,'tertiary':9.5,'unclassified':7,'residential':7,'living_street':6,'service':5}
WALK = {'pedestrian':6,'footway':3,'path':2.5,'steps':3,'cycleway':3,'track':3}
roads, walks = [], []
for wid, (refs, tg) in W.items():
    hw = tg.get('highway')
    if not hw or tg.get('area') == 'yes' or tg.get('access') == 'private' and hw == 'service': continue
    pts = pts_of(refs)
    if len(pts) < 2: continue
    ow = 1 if tg.get('oneway') in ('yes', '1', 'true') or tg.get('junction') == 'roundabout' else (-1 if tg.get('oneway') == '-1' else 0)
    lanes = tg.get('lanes')
    for seg in clip_line(pts):
        seg = dp(seg, 0.8)
        rec = {'n': tg.get('name') or '', 'p': enc(seg), 'b': 1 if tg.get('bridge') else 0}
        if hw in DRIVE:
            w = DRIVE[hw]
            if lanes and lanes.isdigit(): w = max(w, int(lanes) * 3.3)
            if ow and hw in ('residential', 'living_street', 'unclassified'): w = min(w, 6)
            rec.update({'t': hw, 'w': round(w, 1), 'o': ow}); roads.append(rec)
        elif hw in WALK:
            rec.update({'t': hw, 'w': WALK[hw]}); walks.append(rec)

rings = []                                   # (tags, puntos) de edificios, incluidos multipolígonos
for wid, (refs, tg) in W.items():
    if 'building' in tg and refs and refs[0] == refs[-1]: rings.append((tg, pts_of(refs)[:-1], wid))
for rel in root.iter('relation'):
    tg = {t.get('k'): t.get('v') for t in rel.findall('tag')}
    if tg.get('type') == 'multipolygon' and 'building' in tg:
        for m in rel.findall('member'):
            if m.get('type') == 'way' and m.get('role') == 'outer' and m.get('ref') in W:
                refs = W[m.get('ref')][0]
                if refs and refs[0] == refs[-1]: rings.append((tg, pts_of(refs)[:-1], m.get('ref')))
blds = []
for tg, pts, wid in rings:
    if len(pts) < 3: continue
    cx = sum(p[0] for p in pts)/len(pts); cz = sum(p[1] for p in pts)/len(pts)
    if not inside((cx, cz)): continue
    pts = dp_ring(pts, 0.4)
    if len(pts) < 3: continue
    a = area(pts)
    if a < 6: continue
    if tg.get('height'):
        try: h = float(tg['height'].split()[0])
        except ValueError: h = 12
    elif tg.get('building:levels', '').isdigit(): h = int(tg['building:levels']) * 3.2 + 1.2
    else:
        r = hsh(wid)
        old_town = -230 < cx < 60 and -330 < cz < 120      # la Vila y el Raval, edificios más bajos
        if a < 40: floors = 1 + int(r * 2)
        elif old_town: floors = 2 + int(r * 3)
        else: floors = 3 + int(r * 5)
        if tg.get('building') in ('church', 'cathedral') or tg.get('amenity') == 'place_of_worship': floors = 6
        if tg.get('historic') == 'castle': floors = 4
        h = floors * 3.2 + 1.2
    rec = {'p': enc(pts), 'h': round(h, 1)}
    if tg.get('name'): rec['n'] = tg['name']
    blds.append(rec)

areas = []
AREA_T = {'park': 'park', 'garden': 'park', 'village_green': 'park', 'grass': 'park', 'pitch': 'pitch', 'playground': 'plaza', 'sports_centre': 'plaza'}
for wid, (refs, tg) in W.items():
    if not refs or refs[0] != refs[-1] or 'building' in tg: continue
    t = AREA_T.get(tg.get('leisure')) or AREA_T.get(tg.get('landuse'))
    if not t and (tg.get('area') == 'yes' and tg.get('highway') in ('pedestrian', 'footway') or tg.get('place') == 'square' or tg.get('area:highway')): t = 'plaza'
    if not t and tg.get('natural') == 'water': t = 'water'
    if not t: continue
    pts = pts_of(refs)[:-1]
    if len(pts) < 3: continue
    cx = sum(p[0] for p in pts)/len(pts); cz = sum(p[1] for p in pts)/len(pts)
    if not inside((cx, cz), 30): continue
    rec = {'t': t, 'p': enc(dp_ring(pts, 0.5))}
    if tg.get('name'): rec['n'] = tg['name']
    areas.append(rec)

river = sorted({p for refs, tg in W.values() if tg.get('waterway') == 'river' for p in pts_of(refs)}, key=lambda p: p[1])
river = [p for p in river if RZ[1] - 180 < p[1] < RZ[3] + 180]
KEEP = {'place_of_worship', 'townhall', 'marketplace', 'theatre', 'police', 'library', 'fountain', 'hospital', 'arts_centre', 'museum', 'post_office', 'bus_station', 'cinema'}
pois = []
for n in root.iter('node'):
    tg = {t.get('k'): t.get('v') for t in n.findall('tag')}
    nm = tg.get('name')
    if not nm: continue
    kind = tg.get('historic') or tg.get('tourism') or (tg.get('amenity') if tg.get('amenity') in KEEP else None)
    if not kind: continue
    p = N[n.get('id')]
    if inside(p): pois.append({'n': nm, 't': kind, 'x': round(p[0], 1), 'z': round(p[1], 1)})

out = {'src': '© OpenStreetMap contributors (ODbL)', 'rz': RZ, 'roads': roads, 'walks': walks, 'bld': blds, 'areas': areas, 'river': enc(river), 'pois': pois}
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, separators=(',', ':'))
print(f"calles {len(roads)} peatonales {len(walks)} edificios {len(blds)} áreas {len(areas)} río {len(river)} puntos {len(pois)} pdi")
