# Ilici City

Juego de mundo abierto estilo GTA ambientado en Elche (Alicante). Funciona en el navegador, en ordenador y en móvil. Todo el juego está en un único archivo, `index.html`, con three.js cargado desde CDN.

## Cómo jugar

Abre `index.html` en un navegador. Si lo abres con doble clic y no carga, sírvelo por HTTP:

```bash
cd ilici-city && python3 -m http.server 8000
# abre http://localhost:8000
```

| Tecla | Acción |
|---|---|
| W A S D / flechas | Andar o conducir |
| Shift | Correr |
| Espacio | Saltar (a pie) / freno de mano (en coche) |
| Z | Agacharse o levantarse |
| E / Enter | Entrar, robar un coche o salir |
| F / clic | Disparar, golpear o lanzar granada (mantén para ráfaga) |
| Q / rueda / 1-7 | Cambiar de arma |
| H | Claxon |
| C | Cámara normal / cenital |
| V | Primera o tercera persona (también en Pausa → Vista) |
| M | Mapa con nombres de calles |
| I | Mostrar u ocultar los controles en pantalla |
| P / Esc | Pausa, misiones y controles |

Los controles aparecen en pantalla al empezar (tecla I) y en el menú de pausa. En móvil hay joystick, botones táctiles (Saltar y Agachar incluidos) y un botón «?» con la ayuda. En tercera persona apuntar es automático; en primera persona se apunta con la mira. Los avisos salen en una columna pequeña arriba a la derecha para no tapar el juego.

## Qué incluye

- **Mapa de Elche estilizado**: el río Vinalopó cruza la ciudad por un cauce hundido, con 6 puentes. Hay barrios con su propio estilo de edificios (Centro Histórico, El Raval, Carrús, El Toscar, El Pla, Altabix, Los Palmerales y el polígono) y las avenidas de Novelda, Alicante y Santa Pola.
- **Monumentos**: Basílica de Santa María (cúpula azul), Palacio de Altamira, Torre de la Calahorra, Ayuntamiento con la Calendura, La Glorieta, Mercado Central, Parque Municipal, Huerto del Cura con la Palmera Imperial, Estadio Martínez Valero, Campus UMH, Hospital General, Comisaría y Estación.
- **Unas 2.800 palmeras**: palmerales, huertos y las orillas del río.
- **Callejero**: cada calle tiene nombre (C/ Corredora, Paseo de la Estación, C/ Reina Victoria, Av. de la Libertad...). Se ven en placas de azulejo en los cruces, en el HUD y en el mapa.
- **Más detalle urbano**: balcones, toldos y rótulos de tiendas, semáforos (el tráfico los respeta), bancos, papeleras, quioscos, paradas de autobús, ficus y una réplica de la Dama de Elche.
- **Armas**: empiezas con una Desert Eagle y 35 balas. En el Palmeral hay además bate, pistola, subfusil, escopeta, granadas y chaleco antibalas. Cada arma se ve en la mano, con animación de golpe con el bate, puñetazo y lanzamiento de granada. Puedes disparar desde el coche.
- **Botín**: todo NPC que matas suelta dinero y, a veces, un botiquín, chaleco, munición, un paquete o una pistola. Los policías sueltan siempre su arma (pistola, subfusil o escopeta, según el nivel de búsqueda).
- **Mercado negro en Los Palmerales**: en la armería clandestina de «El Chatarrero» compras armas, munición y chaleco. En el trapicheo de «El Rata» compras paquetes de droga para revenderlos a clientes repartidos por la ciudad (marcados en morado). Si la policía te ve vendiendo caen 2 estrellas, y si te detienen te lo requisan.
- **Vehículos**: utilitarios, sedanes, deportivos, taxis, furgonetas, furgonetas de reparto, pick-ups, camiones y autobuses urbanos que paran en las paradas. Todos se pueden robar y conducir.
- **Bicicletas**: en «Bicis Elx» (La Glorieta, cuadrado verde del mapa) compras una bici por 10 € y sales pedaleando.
- **Carretera al aeropuerto**: sale de la ronda de Levante hacia el este y llega al Aeropuerto de Alicante-Elche (El Altet), con terminal, torre de control, pista, aviones aparcados, uno despegando cada poco y aparcamiento.
- **Tráfico y peatones**: los coches circulan por la derecha y siguen la red de calles. Los peatones caminan por las aceras, cruzan la calle y huyen si pasa algo.
- **Sistema de búsqueda de 5 estrellas**: la policía te persigue calculando rutas por las calles. Con 2 o más estrellas dispara y se baja del coche para perseguirte a pie. Te detiene si te quedas quieto y las estrellas bajan si la despistas. Los peatones abatidos sueltan dinero.
- **Daños**: los coches echan humo, se incendian y explotan.
- **5 misiones**: Dátiles para la abuela, Taxi al Martínez Valero, Carrera del Palmeral, El deportivo del míster y La Nit de l'Albà (termina con fuegos artificiales).
- **12 dátiles de oro** escondidos, a 100 € cada uno.
- **Primera persona**: modo shooter con mira, arma en primer plano con retroceso, ratón con captura del puntero (o arrastrando en el móvil) y vista desde el asiento del conductor.
- **Saltar y agacharse**: saltas por encima de bancos y cajas. Agachado vas más despacio, disparas con más precisión y la policía te acierta la mitad de veces.
- **Personajes y coches modelados**: los peatones tienen cuerpo humano (cara, pelo, torso, codos y rodillas que se doblan) y variantes de hombre y mujer, ropa corta o larga y falda. Los coches tienen carrocería con silueta real, llantas, parachoques y retrovisores.
- **Gráficos**: cielo con sol y estrellas, corrección de color cinematográfica, asfalto y aceras con textura, fachadas con persianas y marcos, cornisas, coches con pintura brillante y halos de luz de farolas y faros por la noche. El menú de pausa permite elegir calidad alta, media o baja.
- **Ciclo de día y noche**: amanece a las 7:00 y anochece hacia las 21:00. De noche se iluminan ventanas, farolas y faros.
- **Progreso guardado** en el navegador (localStorage).

El mapa se basa en la geografía real de Elche, pero no es un plano exacto. Las calles siguen una cuadrícula para que el juego funcione bien.

## Ideas para seguir

- Cargar las calles reales de Elche desde OpenStreetMap (requiere acceso a la API de Overpass).
- Más tipos de misiones, radio con música y modelos de coche más detallados.
- Multijugador.
