# Auditoría visual de Ilici City

Fase de mejora gráfica: misma ciudad y mismo juego, pero visualmente más cuidado. No se añaden mecánicas y la lógica no se toca.

## Cómo se dibuja hoy cada cosa

| Elemento | Sistema actual | Dónde |
|---|---|---|
| Render | WebGLRenderer, ACES, sombras PCF suaves (solo escritorio), niebla lineal, hemisférica + sol | `renderer`, `hemi`, `sun`, `updateLighting` |
| Personas (jugador y NPC) | `makePedMesh`: piezas con color por vértice fusionadas; articulaciones como grupos (hombro→codo, cadera→rodilla) que mueven `animPed` y todas las poses (robo, bici, manos arriba, sanitarios, armas…) | `makePedMesh`, `animPed` |
| Vehículos | `buildCarMesh`: perfiles laterales extruidos (`carProfiles`) + piezas; ruedas aparte que giran | `carGeos`, `buildCarMesh` |
| Edificios de la cuadrícula | cajas instanciadas con textura de fachada (ventanas, persianas), cornisas y balcones | `addBuilding`, `instanced` |
| Edificios del centro real (OSM) | plantas reales extruidas con material liso: paredes grandes sin ventanas | bloque "centro real" |
| Calles | losas de asfalto casi negro, aceras con baldosa, marcas y pasos de cebra instanciados | `slabs`, marcas viales |
| Mobiliario | farolas, bancos, papeleras, semáforos: cajas instanciadas | farolas, bancos |
| Palmeras | ~2.800: tronco cilíndrico recto + hojas de caja | `addPalm` |
| Materiales | Lambert por color (`lambert(hex)`), algunos Phong | `matCache` |

Referencia de coste (centro, tercera persona): unas 400–500 llamadas de dibujo y unos 0,9 M de triángulos. La cuadrícula: unas 90 llamadas.

## Lista priorizada

Puntuación de 1 a 5 (en coste y rendimiento, 5 = barato y seguro).

| # | Elemento | Impacto visual | Frecuencia | Identidad | Coste | Rendimiento | Notas |
|---|---|---|---|---|---|---|---|
| 1 | Personaje y peatones | 5 | 5 (siempre en pantalla) | 4 | 4 | 4 | Un solo constructor para todos. Se mejora sin cambiar sus articulaciones: todas las poses siguen funcionando |
| 2 | Fachadas del centro real | 5 | 5 (zona de inicio) | 5 | 3 | 4 | Paredes lisas enormes sin ventanas: es lo que más "rompe" la imagen |
| 3 | Vehículos | 4 | 5 | 3 | 3 | 4 | Silueta aceptable; faltan faros y pilotos que se enciendan, cristales, llantas, intermitentes |
| 4 | Palmeras | 4 | 5 | 5 | 4 | 3 | La identidad de Elche. Hay que instanciarlas con cuidado |
| 5 | Calles (asfalto, bordillos, mobiliario) | 4 | 5 | 3 | 4 | 5 | El asfalto casi negro y sin bordillos aplana todo |
| 6 | Iluminación, cielo y niebla | 4 | 5 | 3 | 5 | 4 | Barato, pero afecta a todo. Cambios globales: mejor al final, con todo lo demás ya hecho |
| 7 | Edificios de la cuadrícula | 3 | 4 | 3 | 3 | 4 | Ya tienen fachada con ventanas; faltan variantes (comercio en bajos, azoteas) |
| 8 | Vegetación secundaria y césped | 2 | 3 | 3 | 4 | 3 | |

## Orden de trabajo

El orden propuesto se mantiene, con un cambio justificado por el código: las **fachadas del centro real** pasan al bloque de edificios y se adelantan a las calles. A pie de calle ocupan la mitad de la pantalla en la zona donde empieza el juego.

1. Personaje principal y peatones ✅
2. Vehículos ✅
3. Edificios (primero el centro real) ✅
4. Calles y mobiliario urbano ✅
5. Palmeras y vegetación ✅
6. Iluminación y atmósfera ✅
7. Materiales y detalles ✅ (segunda pasada): agua con movimiento, fuente de la Glorieta, Basílica detallada, sombras de contacto y comercios con nombre

## Resultado de esta primera pasada

- **Coste medido**, en la misma vista de calle de la cuadrícula:
  - antes: unas 1.000 llamadas de dibujo y 1,06 M de triángulos;
  - después: unas 1.050–1.100 llamadas y 1,26 M de triángulos.

  El personaje baja de unas 5.900 a unas 5.000 caras y el detalle de coches, farolas y semáforos va en mallas fusionadas o instanciadas. Las palmeras usan LOD.
- **Artefactos corregidos** por el camino:
  - acné de sombra bajo los toldos;
  - ruido de precisión del hash con seno;
  - parpadeo por `floor()` sobre la normal interpolada;
  - moiré de lejos: el detalle fino se funde según la distancia.
- **Semáforos**: ahora muestran el estado real que respeta el tráfico. Antes eran colores fijos.

## Segunda pasada

- **Sombras de contacto**: una mancha suave bajo cada peatón (y el jugador) y bajo cada coche cercano. Son dos mallas instanciadas, así que cuestan dos llamadas. En móvil, sin sombras en tiempo real, es lo que "posa" a la gente en el suelo.
- **Agua**: material propio con reflejo del cielo y oleaje animado en el shader (sin texturas). Se usa en el Vinalopó, en las láminas de agua del centro real y en la fuente de la Glorieta.
- **Fuente de la Glorieta**: taza superior con agua y surtidor.
- **Basílica de Santa María**: tambor con ventanas, cúpula de teja vidriada azul con nervios, linterna y cruz; campanario con impostas, arcos del cuerpo de campanas, balaustrada y remate con cupulín azul. Colisiones iguales que antes.
- **Comercios con nombre**: unos 1.700 rótulos, todos en una sola llamada de dibujo (atlas de 64 rótulos y malla instanciada).
  - En el centro real se calculan con las mismas cuentas que el shader de fachada, así que cada rótulo cae justo sobre la banda de un escaparate. Solo van en fachadas que dan a una calle con nombre.
  - De noche se iluminan.
  - Los nombres son inventados (sin marcas reales). Usan un generador aleatorio aparte, de modo que no cambia ni un edificio de sitio.

## Siguientes pasos propuestos

- Calahorra y Altamira con más geometría propia.
- Peatones y vehículos a distancia con modelos simplificados (LOD).

## Modelos externos: decisión

Desde el entorno de desarrollo no se puede acceder a los repositorios habituales de modelos CC0 (Kenney, Poly Pizza). Aparte de eso, el sistema de animación del juego mueve directamente las articulaciones de los personajes: robo de coche, bici, manos arriba, sanitarios, delincuentes, armas y golpes. Un GLB con esqueleto obligaría a rehacer todas esas poses. Por eso esta fase mejora la geometría procedural manteniendo exactamente la misma interfaz, lo que garantiza compatibilidad y un estilo coherente.

La puerta a los GLB queda abierta: la carga se haría con GLTFLoader mediante un importmap y los modelos irían incrustados o como archivos adjuntos. Tiene sentido para piezas estáticas, como mobiliario o monumentos, siempre con licencia CC0/CC-BY comprobada.
