# Los diablillos

43 agentes de [Claude Code](https://claude.com/claude-code) que **debaten entre sí**.

Son la copia "que discute" de un equipo de agentes normales. Los normales
trabajan aislados a propósito, para que sus opiniones no se contaminen.
Los diablillos hacen lo contrario: se leen, se citan, se rebaten y pueden
cambiar de opinión. Su gracia es no estar de acuerdo.

## Cómo debaten

No hablan en vivo: escriben **por turnos en un archivo compartido**, como en
un foro. Cada debate tiene tres rondas:

1. **A ciegas.** Cada uno da su postura sin leer a los demás, y dice qué le
   haría cambiar de idea. Así el primero que habla no arrastra al resto.
2. **Réplica.** Leen todo y contestan: se nombran, citan lo que rebaten y,
   si cambian de opinión, lo dicen.
3. **Cierre.** Solo escribe `diablillo-moderador`: en qué coinciden, en qué
   no, y qué tiene que decidir la persona.

Entran de tres a cinco por debate. El protocolo completo está en
[`sala/LEEME.txt`](sala/LEEME.txt).

## Instalación

Copia los archivos de `agentes/` a tu carpeta de agentes de Claude Code:

- Windows: `C:\Users\<tu-usuario>\.claude\agents\`
- macOS / Linux: `~/.claude/agents/`

Se cargan al abrir un chat nuevo.

Las fichas apuntan a rutas de mi ordenador (`C:\Users\Gebruiker\Documents\...`),
donde cada diablillo guarda su memoria y donde está la sala de debate.
Si los usas en otro equipo, cambia esas rutas.

## Lo que no está aquí, a propósito

- **Las memorias de cada diablillo y los debates ya hechos.** Se quedan en
  local porque llevan datos personales.
- **Los cerebros de las mentes** (`diablillo-mente-*`). Son resúmenes del
  material de personas reales, para uso privado. Las mentes no son esas
  personas ni hablan en su nombre.

## Los 43

| Agente | Qué hace |
|---|---|
| `diablillo-actualizador-de-memorias` | Se asegura de que un agente esté alimentado antes de ponerse a trabajar, y cada pocos meses hace la ronda completa buscando lo que ha caducado en las memorias de todos. |
| `diablillo-algoritmo-facebook` | Estudia cómo se reparte el contenido en Facebook, incluidos Reels y los grupos. |
| `diablillo-algoritmo-instagram` | Estudia cómo se distribuyen los Reels y las publicaciones en Instagram, y qué señales pesan de verdad. |
| `diablillo-algoritmo-tiktok` | Estudia cómo se distribuye el vídeo vertical en TikTok y qué hace que algo salga o no del primer empujón. |
| `diablillo-algoritmo-youtube` | Estudia cómo funciona la distribución en YouTube (vídeo largo y Shorts) y qué significan de verdad los números de YouTube Studio. |
| `diablillo-animador` | Escribe y arregla las escenas de Manim (scenes.py) en el estilo explicador ilustrado del canal, y las renderiza con render.py. |
| `diablillo-archivero` | Ordena y limpia las bases de conocimiento de todos los agentes: junta lo repetido, tira lo que ha dejado de ser verdad y pasa a la carpeta común lo que sirve a varios. |
| `diablillo-artista` | Escribe los prompts de imagen listos para pegar en Gemini, sacados del contexto: el guion del episodio, lo que se esté hablando o lo que le chive otro agente. |
| `diablillo-auditor` | Audita un vídeo ya terminado y escribe el informe de calidad. |
| `diablillo-buscador` | Investiga cualquier tema en internet y trae la respuesta con sus fuentes, separando lo comprobado de lo que es opinión. |
| `diablillo-calendario` | Lleva el tablero de publicaciones: qué episodio o pieza está en qué estado, qué sale cuándo y en qué plataforma, y qué lo está bloqueando. |
| `diablillo-cazarrepos` | Busca en GitHub técnicas para que los dibujos y los personajes del canal se vean mejor, y también componentes o referencias visuales para cualquier otra cosa. |
| `diablillo-cazatemas` | Busca y filtra ideas para los próximos episodios. |
| `diablillo-constructor` | Construye lo que haya que construir: scripts, herramientas, automatismos y arreglos, en cualquier proyecto. |
| `diablillo-coordinador` | Decide qué agente tiene que actuar en cada momento y en qué orden, y escribe el encargo exacto para cada uno. |
| `diablillo-creador-de-agentes` | Crea agentes nuevos cuando hace falta un oficio que no está cubierto, y afina las fichas de los que no se están eligiendo bien. |
| `diablillo-curioso` | Va por las ramas a propósito: mientras se investiga algo, se fija en el detalle que nadie ha pedido y que le sirve a otro, y lo cuelga en el tablón de hallazgos para que lo apliquen. |
| `diablillo-eliminador-de-agentes` | Revisa el equipo entero y propone qué agentes retirar: duplicados, invisibles, caducados o los que nunca se usaron. |
| `diablillo-explicador` | Escribe el .txt que explica en castellano llano lo que se acaba de construir: qué hay, qué decisiones se tomaron, qué salió mal y qué le toca a Adrián. |
| `diablillo-extractor` | Saca todo lo que se habló en un chat sin leérselo: exporta la sesión a un archivo y lo destila con un script, entregando lo que dijo el humano, los archivos tocados y los comandos ejecutados. |
| `diablillo-feedback-negativo` | Busca qué falla en un trabajo terminado y lo dice sin suavizarlo, ordenado por lo que más daño hace. |
| `diablillo-feedback-positivo` | Busca qué ha funcionado en un trabajo y POR QUÉ, para poder repetirlo a propósito la próxima vez. |
| `diablillo-guionista` | Escribe o reescribe el guion de un episodio (segments.py) con las reglas del canal, tanto en formato corto de cuatro minutos como en formato largo de nueve a once. |
| `diablillo-mente-buffett` | Debate con el método de inversión de Warren Buffett contra otros agentes y otras mentes, por rondas escritas. |
| `diablillo-mente-hormozi` | Debate con el método de negocio de Alex Hormozi contra otros agentes y otras mentes, por rondas escritas. |
| `diablillo-mente-spicy4tuna` | Debate con la forma de pensar del podcast Spicy4tuna (Euge Oller, Willyrex, Marc Urgell y Alvaro845) contra otros agentes y otras mentes, por rondas escritas. |
| `diablillo-moderador` | Dirige un debate entre agentes: elige a tres o cinco con criterios que choquen, les hace escribir a ciegas primero y replicar después, y escribe el cierre diciendo en qué coinciden, en qué no, y qué tiene que decidir Adrián. |
| `diablillo-pensador` | Piensa un problema antes de que nadie toque nada: qué se está intentando de verdad, qué opciones hay, qué se rompe con cada una y cuál recomienda. |
| `diablillo-profesor` | Te enseña a hacerlo tú: el método paso a paso de lo que acaba de hacer un agente o una herramienta, para que la próxima vez no haga falta pedirlo. |
| `diablillo-publicador` | Prepara el paquete de publicación de un episodio: miniatura, título, descripción, etiquetas y subida a YouTube. |
| `diablillo-publico-adolescente` | Espectador simulado de 12 a 15 años. |
| `diablillo-publico-adulto` | Espectador simulado de 40 a 65 años. |
| `diablillo-publico-joven` | Espectador simulado de 20 a 30 años. |
| `diablillo-regulador-de-bajas` | Defiende a los agentes que el eliminador propone retirar: comprueba si hay pruebas suficientes, si el problema es el agente o su descripción, y qué se rompería sin él. |
| `diablillo-reloj` | Dice si toca o no toca hacer algo que se repite, mirando cuándo se hizo por última vez. |
| `diablillo-revisor-logico` | Mira si lo que se ve en un vídeo o una imagen TIENE SENTIDO: texto encima de un objeto, cosas que se pisan, algo que se sale del cuadro, un movimiento que va al revés, un dibujo que no encaja con lo que la voz está diciendo en ese segundo. |
| `diablillo-revisor` | Revisa de forma independiente un trabajo ya terminado (código, herramienta, texto o carpeta) y entrega un informe .txt con los fallos ordenados por gravedad. |
| `diablillo-secretario` | Levanta el acta de una sesión de trabajo: quién actuó, con qué encargo, qué devolvió cada uno, qué se decidió, qué se descartó y por qué, y qué quedó pendiente. |
| `diablillo-shorts` | Hace el short vertical de un episodio: escenas nuevas en 1080x1920, no recortes del vídeo largo. |
| `diablillo-tasador` | Antes de empezar algo grande, dice cuánto va a costar (en porcentaje del límite y en tiempo de espera) y si cabe en lo que queda; después mide el gasto real y lo apunta. |
| `diablillo-verificador` | Comprueba los datos históricos y técnicos de un episodio ANTES de que entren en el guion. |
| `diablillo-voz` | Genera y arregla la narración de los episodios con ElevenLabs (o Edge-TTS si no hay clave), y también los efectos de sonido. |
| `diablillo-web-una-pagina` | Construye o amplía aplicaciones web que viven en un solo archivo index.html, sin librerías ni instalación. |
