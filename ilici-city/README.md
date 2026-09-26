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
| E | Interactuar con lo que tengas delante (coches, tiendas, trabajos, misiones, vecinos, aeronaves). Los círculos del suelo solo marcan: nada se activa solo |
| Intro | Bajarse del coche (en coche, E usa la actividad que tengas al lado) |
| F / clic | Disparar, golpear o lanzar granada (mantén para ráfaga). Con puños o bate, mantén para cargar un golpe fuerte |
| Clic derecho (mantener) | Apuntar por encima del hombro (tercera persona) |
| Q / rueda / 1-7 | Cambiar de arma |
| H | Claxon mientras lo mantienes (a pie, silbas) |
| T | Pedir un taxi libre cercano. Dentro: Espacio salta el trayecto y E te baja |
| C | Cámara normal / cenital |
| V | Primera o tercera persona (también en Pausa → Vista) |
| M | Mapa: zoom con la rueda o +/−, arrastrar para moverte, clic para marcar destino y clic derecho para quitarlo |
| Tab | Teléfono móvil |
| Retroceso | Cancelar la misión en curso (pulsa dos veces; también hay botón en pantalla y en la pausa) |
| En vuelo | W/S potencia o avance · A/D girar · Espacio/X subir o morro arriba/abajo · Z/C lateral (helicóptero) · E bajar cuando estés posado y parado |
| I | Mostrar u ocultar los controles en pantalla |
| P / Esc | Pausa, misiones, guardar/cargar y controles |

Los controles aparecen en pantalla al empezar (tecla I) y en el menú de pausa. En primera persona, el primer clic solo captura el ratón (no dispara); Esc lo suelta y abre la pausa. En móvil hay joystick, botones táctiles (Saltar y Agachar incluidos) y un botón «?» con la ayuda. En tercera persona, sin apuntar, el tiro va al objetivo más cercano; manteniendo el clic derecho apuntas por encima del hombro con mira. En primera persona se apunta con la mira del centro. Los avisos salen en una columna pequeña arriba a la derecha para no tapar el juego.

## Qué incluye

- **Centro real a escala 1:1**: de La Glorieta al carrer Aspe (Raval de Santa Teresa), con los datos de OpenStreetMap. Tiene 177 calles con su trazado, nombre y sentido, 488 edificios con su planta real, plazas (Plaça de Baix, plaça Santa Maria, Glorieta…), parques, el cauce real del Vinalopó y los puentes d'Altamira, de Canalejas y de Santa Teresa. Entre los monumentos están la Basílica de Santa Maria (cúpula y campanario), el Ajuntament con la Calendura, la Torre de la Calaforra, el Palau d'Altamira y la Dama d'Elx en La Glorieta. Hay tráfico que respeta los sentidos únicos y peatones por las aceras.
- **Resto de Elche estilizado**: el río Vinalopó cruza la ciudad por un cauce hundido, con 6 puentes, y las avenidas de Novelda, Alicante y Santa Pola.
- **Barrios donde están de verdad**: la capa de barrios se ha generado con geocodificación inversa de OpenStreetMap. Cada manzana y cada celda de 55 m del centro llevan el barrio real de ese punto; fuera del centro la ciudad está comprimida pero respeta las direcciones. Quedan así: El Toscar al noroeste más allá de Carrús; Pisos Azules al suroeste del centro; El Pla y Sector V al oeste y suroeste; L'Asil y El Raval al sur; La Rata y Candalix al norte; Altabix al noreste; Los Palmerales, San Antón y La Portalada al este y sureste. El Hospital General está en La Portalada, el estadio Martínez Valero al este y el Campus UMH en Candalix. Cada distrito tiene su estilo de edificios.
- **Monumentos**: Basílica de Santa María (cúpula azul), Palacio de Altamira, Torre de la Calahorra, Ayuntamiento con la Calendura, La Glorieta, Mercado Central, Parque Municipal, Huerto del Cura con la Palmera Imperial, Estadio Martínez Valero, Campus UMH, Hospital General, Comisaría y Estación.
- **Unas 2.800 palmeras**: palmerales, huertos y las orillas del río.
- **Callejero**: cada calle tiene nombre (C/ Corredora, Paseo de la Estación, C/ Reina Victoria, Av. de la Libertad...). Se ven en placas de azulejo en los cruces, en el HUD y en el mapa.
- **Más detalle urbano**: balcones, toldos y rótulos de tiendas, semáforos (el tráfico los respeta), bancos, papeleras, quioscos, paradas de autobús, ficus y una réplica de la Dama de Elche.
- **Armas**: empiezas con una Desert Eagle y 35 balas. En el Palmeral hay además bate, pistola, subfusil, escopeta, granadas y chaleco antibalas. Cada arma se ve en la mano, con animación de golpe con el bate, puñetazo y lanzamiento de granada. Puedes disparar desde el coche.
- **Botín**: todo NPC que matas suelta dinero y, a veces, un botiquín, chaleco, munición, un paquete o una pistola. Los policías sueltan siempre su arma (pistola, subfusil o escopeta, según el nivel de búsqueda).
- **Mercado negro en el Palmeral**: en la armería clandestina de «El Chatarrero» compras armas, munición y chaleco. En el trapicheo de «El Rata» compras paquetes de droga para revenderlos a clientes repartidos por la ciudad (marcados en morado). Si la policía te ve vendiendo caen 2 estrellas, y si te detienen te lo requisan.
- **Vehículos**: utilitarios, sedanes, deportivos, taxis, furgonetas, furgonetas de reparto, pick-ups, camiones y autobuses urbanos que paran en las paradas. Todos se pueden robar y conducir.
- **Bicicletas**: en «Bicis Elx» (La Glorieta, cuadrado verde del mapa) compras una bici por 10 € y sales pedaleando.
- **Carretera al aeropuerto**: sale de la ronda de Levante hacia el este y llega al Aeropuerto de Alicante-Elche (El Altet), con terminal, torre de control, pista, aviones aparcados, uno despegando cada poco y aparcamiento.
- **Combate cuerpo a cuerpo**: golpes con los dos brazos (directos, ganchos, uppercuts). Un golpe normal hace tambalearse al NPC; el golpe cargado (mantén el botón) puede tumbarlo.
- **Daño por zonas**: la cabeza hace mucho más daño, las piernas hacen cojear o caer y los brazos y el torso hacen tambalearse.
- **Robo de coches con animación**: abres la puerta, sacas al conductor a rastras (cae al suelo, se levanta y huye) y te subes. No puedes robar un coche en marcha rápida.
- **Atropellos realistas**: el resultado depende de la velocidad, el ángulo y el peso del vehículo. A poca velocidad solo empujas; los golpes fuertes tumban y los muy fuertes matan. En bici te pueden disparar, te caes en choques fuertes o explosiones y la bici queda en el suelo.
- **Testigos, cámaras y policía**: la policía solo sabe lo que ve o lo que le cuentan. Los testigos tardan unos segundos en llamar (se ve en el HUD) y hay cámaras de seguridad en monumentos, tiendas y comercios. Sin testigos no hay estrellas; un ruido sin testigos solo hace que la policía investigue la zona. La policía persigue lo que ve o tu última posición conocida y después rastrea la zona, también a pie. Para escapar: rompe la línea de visión, métete en callejones y plazas peatonales, agáchate, aprovecha la noche o cambia de vehículo.
- **Actividades para ganar dinero** (marcadores azules): Reparto Exprés (paquetes urgentes, vale la bici), Logística Vinalopó en las naves de Sector V (transporte con camión y mozo de almacén), Parada de taxis de la Estación (carreras encadenadas), Taller de Carrús (asistencia en carretera, reparar, comprar y vender coches), Carreras clandestinas de Candalix (de noche, con apuesta), Inmobiliaria Glorieta (negocios que hacen caja cada día de juego) y encargos de NPC que te llaman por la calle. Los comercios naranjas (estanco, gasolinera, joyería) se pueden atracar con un arma de fuego.
- **Mapa con zoom y destinos**: el mapa (M) se amplía de forma suave hasta ver cada calle con su nombre y se puede desplazar. Al pulsar un icono (misiones, trabajos, tiendas, negocios, la gasolinera, monumentos) o cualquier punto se marca un destino: aparece la ruta por las calles en el mapa y en el minimapa, una columna de luz en el mundo y una flecha con la distancia en el HUD. El destino dura hasta que llegas, lo quitas o eliges otro.
- **Taxis**: los taxis blancos con luz verde se pueden parar (T). Eliges el destino en el mapa, ves el precio (bajada de bandera + €/km), pagas y el taxista te lleva respetando el tráfico y los sentidos únicos. Puedes saltar el trayecto o bajarte antes. Si te busca la policía, no te lleva.
- **Peatones que reaccionan**: ven tu arma si está a la vista (según distancia, su campo de visión, paredes y luz) y te miran, retroceden, se alejan o huyen gritando y avisando a otros. Si les apuntas, huyen, levantan las manos o se agachan. Los testigos sacan el móvil y llaman a la policía durante unos segundos: si te acercas o les atacas antes de que terminen, cuelgan y ese aviso no llega. Al chocar andando o corriendo con alguien, se aparta o se tambalea y notas el golpe.
- **Estrellas que se van apagando**: cuando la policía deja de verte, la estrella de arriba parpadea unos segundos antes de perderse, una a una.
- **Cámara que no atraviesa paredes**: se acerca o se pone sobre el hombro cuando hay una pared detrás y nunca deja ver el interior de los edificios.
- **Sonido por vehículo**: cada tipo tiene su claxon (turismo, utilitario, furgoneta, autobús, camión con bocina de aire, timbre de bici) y las patrullas llevan su propia sirena; todo suena desde la posición del vehículo.
- **Tráfico que no choca constantemente**: los coches tienen una capa de navegación propia. Planifican su trayectoria por el carril con antelación (esquinas en el cruce de carriles y persecución pura con curvatura) y respetan la holgura real de cada tramo, calculada con los contornos de los obstáculos. Solo circulan por la red de tramos con sentido desde la que se puede seguir sin medias vueltas ni giros que no caben. Además:
  - piden paso en cruces y calles estrechas;
  - siguen al de delante según su huella real;
  - rodean los coches parados o abandonados;
  - las patrullas que solo investigan circulan como uno más.

  Los choques quedan como algo ocasional: en las mediciones, entre 0 y 1 incidente por cada 2 minutos y zona, frente a cientos de contactos antes. Los peatones caminan por las aceras, cruzan la calle y huyen si pasa algo.
- **Sistema de búsqueda de 5 estrellas**: la policía te persigue calculando rutas por las calles. Con 2 o más estrellas dispara y se baja del coche para perseguirte a pie. Te detiene si te quedas quieto y las estrellas bajan cuando pasa un rato sin verte.
- **Daños y coches destruidos**: los coches echan humo, se incendian y explotan.
  - Antes de explotar, conductor y pasajeros abren la puerta y huyen con pánico. Si el fuego lo has causado tú, son testigos.
  - Si explota antes de que salgan, mueren y el cuerpo se queda un rato.
  - El daño de la explosión cae con la distancia para peatones, jugador y otros coches.
  - Los restos se retiran cuando no los ves y el tráfico vuelve a salir.
- **Ambulancias**: los atropellos, las explosiones con víctimas y los heridos graves generan un aviso al 112.
  - Sale una ambulancia con sirena, llega por las calles y aparca lo más cerca posible.
  - Dos sanitarios atienden: el herido se levanta y se va, y el fallecido se retira.
  - Después se marchan sin sirena.
- **Delincuencia por barrios**: Los Palmerales (trapicheo y atracos) y San Antón (peleas y vandalismo) tienen más actividad; Carrús, El Raval y La Rata, algo; el resto, poca.
  - Solo una parte de la gente es camello, macarra (algunos armados) o vándalo.
  - De vez en cuando pasa algo cerca: una venta, una discusión que acaba en pelea, un atraco a un peatón, un grafiti que se queda en la pared o un coche con la alarma sonando.
  - Los testigos denuncian y acude una patrulla. El sospechoso huye, se entrega o, si va armado y la cosa escala, se lía a tiros con la policía.
  - Un macarra armado al que apuntas puede dispararte.
- **Aviones y helicópteros**: en el aeropuerto Miguel Hernández hay una avioneta junto al hangar y un helicóptero en el helipuerto; en el Hospital General hay otro.
  - Con la avioneta despegas por la pista, vuelas por todo el mapa y aterrizas (o te estrellas).
  - El helicóptero despega en vertical, avanza, gira y se desplaza de lado.
  - Hay colisiones con suelo y edificios, daños, y una cámara que no atraviesa nada.
  - No puedes bajarte en el aire ni a velocidad peligrosa.
  - Un helicóptero de la policía patrulla la ciudad y, con 3 o más estrellas, te sigue desde el aire. Es la base para despegues y aterrizajes automáticos y tráfico aéreo.
- **5 misiones**: Dátiles para la abuela, Taxi al Martínez Valero, Carrera del Palmeral, El deportivo del míster y La Nit de l'Albà (termina con fuegos artificiales).
- **12 dátiles de oro** escondidos, a 100 € cada uno.
- **Primera persona**: modo shooter con mira, arma en primer plano con retroceso, ratón con captura del puntero (o arrastrando en el móvil) y vista desde el asiento del conductor.
- **Saltar y agacharse**: escalones y bordillos se suben solos. Saltando superas bancos, cajas y muretes y te subes al techo de los coches (si arranca, te lleva encima). Agachado vas más despacio, disparas con más precisión y la policía te acierta la mitad de veces.
- **Personajes y coches modelados**: los peatones tienen cuerpo humano (cara, pelo, torso, codos y rodillas que se doblan) y variantes de hombre y mujer, ropa corta o larga y falda. Los coches tienen carrocería con silueta real, llantas, parachoques y retrovisores.
- **Gráficos**: cielo con sol y estrellas, corrección de color cinematográfica, asfalto y aceras con textura, fachadas con persianas y marcos, cornisas, coches con pintura brillante y halos de luz de farolas y faros por la noche. El menú de pausa permite elegir calidad alta, media o baja.
- **Ciclo de día y noche**: amanece a las 7:00 y anochece hacia las 21:00. De noche se iluminan ventanas, farolas y faros.
- **Interacción con E**: un único sistema muestra «[E] Verbo · Nombre» para lo que tengas delante (entrar, hablar, atracar, empezar misión, vender, robar, pilotar…) y nada se activa por pisar un círculo.
- **Misión activa**: con una misión en curso, el minimapa y el mapa solo muestran el objetivo actual, el siguiente y el destino final, con ruta GPS y flecha. El botón «Cancelar misión» (clicable, con confirmación) quita objetivo, ruta y marcadores.
- **Teléfono móvil** (Tab o 📱): mapa, misiones (marcar ruta o cancelar), cartera, contactos (llamar o ir), mensajes (los encargos llegan aquí), taxi que viene a buscarte, guardar, cargar y datos del personaje. Las apps se registran en una lista, así que se pueden añadir llamadas, negocios o actividades nuevas.
- **Guardar y cargar**: ranura automática y tres manuales, desde la pausa, el título o el teléfono.
  - Guarda posición, hora, salud, blindaje, arma, vehículo (tipo, color, si es tuyo, daño), dinero, armas, munición, misiones, dátiles y negocios.
  - Autoguardado cada 3 minutos y al terminar misiones, cuando se puede (sin misión en curso, sin policía, parado y en tierra).
  - Amplía el guardado de siempre en localStorage.

El centro (La Glorieta – carrer Aspe) es real. El resto del mapa se basa en la geografía de Elche, pero sus calles siguen una cuadrícula.

## Datos del centro real

- Fuente: © colaboradores de OpenStreetMap, licencia ODbL (https://www.openstreetmap.org/copyright).
- `data/elche-centro.json` es el extracto ya convertido y va incrustado en `index.html`.
- Para regenerarlo o ampliar la zona:
  ```bash
  curl -o zona.osm "https://api.openstreetmap.org/api/0.6/map?bbox=-0.7040,38.2620,-0.6935,38.2680"
  python3 tools/osm_to_game.py zona.osm data/elche-centro.json
  ```
  Después hay que sustituir el contenido de `<script id="elx-data">` en `index.html` por el nuevo JSON. Si cambias la caja, ajusta también `RZ` en el script.

## Ideas para seguir

- Ampliar la zona real a más barrios (Parque Municipal, Huerto del Cura, Carrús…).
- Bomberos (el sistema de avisos y la sirena ya están preparados), aviones con despegue y aterrizaje automáticos y tráfico aéreo.
- Más tipos de misiones, radio con música y modelos de coche más detallados.
- Multijugador.
