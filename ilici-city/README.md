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
- **Fase de mejora gráfica** (ver `AUDITORIA_GRAFICA.md`). Misma ciudad y mismo juego, visualmente más cuidados.
  - **Personas** con más detalle y el mismo esqueleto de animación: manos, zapatillas, ropa variada y uniforme policial. El protagonista lleva la camiseta del Elche CF.
  - **Coches** con reflejos del cielo, pasos de rueda, matrículas, rotulación de servicio, luces de freno e intermitentes.
  - **Fachadas** con comercios, portales, balcones con barandilla y cornisa, y escaparates que se iluminan de noche.
  - **Calles**: asfalto realista, bordillos, farolas con brazo y semáforos que muestran el estado real.
  - **Palmeras** datileras con anillos, hojas arqueadas y LOD.
  - **Luz** con más contraste y exposición según la hora.
  - **Detalles**: sombras de contacto bajo peatones y coches, agua con oleaje (Vinalopó y fuentes), Basílica de Santa María con cúpula azul nervada y campanario detallado, y unos 1.700 comercios con rótulo (nombres inventados) que se iluminan de noche.
  - **Monumentos** con sillería y saeteras (Calaforra, Basílica, Mercé, Salvador), edificios nobles sin tiendas (Ajuntament, Gran Teatre) y el **Palau d'Altamira** recuperado con su torreón y almenas.
  - **Cielo con nubes** que se mueven y dejan ver las estrellas de noche.
  - **Rendimiento**: la mitad de triángulos en pantalla gracias al troceado de mallas por zonas, al recorte de palmeras fuera de cámara y al LOD de peatones.
- **Helicóptero en tejados**: se posa sobre la superficie real de los patines, sin hundirse, rebotar ni deslizarse, aunque quede al borde. Al bajar apareces en el tejado, no en la calle. El rotor no atraviesa paredes y el despegue es normal.
- **Mezcla de audio**: cada categoría de sonido tiene su bus (interfaz, efectos, explosiones, sirenas, vehículos) y hay un limitador final.
  - Hay un máximo de voces simultáneas por categoría, y las explosiones y los disparos bajan un momento sirenas y motores.
  - Sirenas: suenan como mucho 3, con prioridad para la más cercana, y cada una tiene su tono y su ritmo. Si hay muchas patrullas juntas, cada una suena más baja: ya no se satura.
  - Los disparos de la policía y de los NPC suenan desde donde se disparan.
- **Cámara y ratón**: el ratón queda capturado (sin cursor) en primera y en tercera persona, y la cámara gira con el movimiento del ratón.
  - En tercera persona se orbita e inclina, y la cámara no se recoloca sola mientras mueves el ratón.
  - El primer clic solo captura: no dispara.
  - Esc pausa y muestra el cursor. Al volver del menú, el mapa o el teléfono, se recaptura.
- **Muerte y heridas**:
  - Al morir, el cuerpo se dobla y cae con gravedad (de espaldas o de bruces, según el disparo), con una cámara que se aleja alrededor del cuerpo.
  - La sangre es moderada, y cada herida da un destello rojo en pantalla; con poca vida, la pantalla late.
  - Los NPC reaccionan según la zona y su aguante (se doblan, se agarran el brazo, hincan la rodilla o caen) y dejan un charco al morir.
- **Peatones con carácter**: cada persona tiene edad y personalidad. Si les pegas, pueden contraatacar, cubrirse, huir, llamar a la policía, pedir ayuda (y acuden vecinos) o apartarse.
- **Población por barrios**: hay presencia gitana en El Palmeral y San Antón y magrebí en Carrús y El Toscar, con nombres, aspecto y ropa propias. El comportamiento de cada uno se decide por persona y barrio, nunca por su origen.
- **Conversaciones**: lo que dice cada vecino depende de:
  - su carácter y su edad;
  - su forma de hablar;
  - la hora y el barrio;
  - lo que pasa (sirenas, disparos, si te busca la policía, si vas armado o herido);
  - vuestra relación: se acuerda de si le pegaste, se cansa si insistes y algunos te cuentan historias en varias veces y se presentan.
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

## Fase de sistemas y calidad

- **Estrellas por gravedad**: cada delito tiene un peso y un tope propios. Una pelea callejera se queda en 1 o 2 estrellas; disparar, matar o atracar puede llegar a 3; atacar a la policía, a 4; matar agentes, a 5. Varios golpes a la misma persona cuentan como un solo incidente, y solo cuenta lo que la policía sabe (lo ha visto, o un testigo o una cámara te han identificado).
- **Perder la búsqueda**: mientras la policía tenga pista se mantienen las estrellas. Cuando la pierde, empieza una búsqueda activa y, si sigues oculto, todas las estrellas parpadean y desaparecen a la vez. Cuesta unos 20 s con 1 estrella, unos 60 s con 3 y unos 145 s con 5.
- **Helicóptero policial**: espera en la comisaría y despega con 3 estrellas. Busca alrededor de la última pista sin saber dónde estás y solo te ve si tiene línea de visión (peor de noche). Lleva foco de búsqueda, rotativos y sonido de rotor, y vuelve a la base al bajar el nivel.
- **Blindados**: solo con 5 estrellas y como mucho 2. Persiguen, apuntan con la torreta, disparan el cañón y aplastan coches; se retiran al bajar el nivel.
- **Puñetazos por fases**: preparación, giro del torso, paso del peso, extensión hacia el objetivo, contacto sincronizado y vuelta a la guardia. Hay directo, gancho, uppercut y golpe cargado, y los NPC que pelean usan la misma animación.
- **Aeropuerto**: base aérea vallada con guardias, refugio y un caza. Entrar sin permiso acaba en aviso a la policía y robar el caza da 4 estrellas. El helicóptero del aeropuerto se denuncia si te ven robarlo, y la avioneta del aeroclub es libre.
- **Autobuses con pasajeros**: los vecinos esperan en las paradas, suben, viajan visibles tras las ventanas y bajan en su parada. Si robas el bus, siguen dentro.
- **Acciones animadas**: bajar del coche por la puerta, sacar el móvil y recargar con cargador (tecla R).
- **Armería y trapicheo** trasladados de verdad al palmeral del barrio Los Palmerales.
- **Personajes más humanos**: brazos y piernas con volumen muscular, codos y rodillas sin huecos, pelo que deja la frente despejada y cejas finas (ya no parecen gafas de sol).
- **Calles**: contenedores de reciclaje junto al bordillo.
- **Rendimiento en vuelo**: no se dibuja nada más allá de la niebla ni los peatones lejanos, lo que reduce las llamadas de dibujo en un 40 % desde el aire.

## Vida en la calle y locales

- **Estrellas coherentes**: robar un vehículo es 1 estrella, aunque sea otra vez (un coche patrulla, 2). Lo que sube el nivel es la violencia, las armas y atacar a la policía.
- **Víctimas de un robo de coche**: según su carácter intentan recuperarlo (y pueden sacarte si te quedas parado), persiguen el coche, insultan, se quedan paralizadas, miran, piden ayuda, huyen o llaman a la policía.
- **Conductores atacados** (golpes, patadas, disparos o embestidas): pitan, se enfadan, se bajan a pelear y luego vuelven a su coche, huyen a toda velocidad, te atropellan para escapar, salen corriendo, se encierran o llaman a la policía. Cambia según el vehículo.
- **Patadas según el objetivo**: si está de pie, puñetazo; agachado, patada baja; en el suelo, pisotón; y contra un vehículo, patada a la puerta.
- **Autobuses con líneas** (L1, L2, L3…), con letrero luminoso y paradas en orden. Si robas uno con gente dentro, cada pasajero reacciona a su manera: pánico, suplicar, llamar a la policía, grabar o tirarse en marcha.
- **Motos**: scooter, naked y deportiva en el tráfico. Se inclinan en las curvas, la deportiva hace caballitos y al frenar se hunde el morro. Los pilotos llevan casco, y hay caídas en las que ruedas por el suelo. Los pilotos de la IA también caen.
- **Saltar de un vehículo en marcha**: sales con la inercia, ruedas por el asfalto y el daño depende de la velocidad (por encima de unos 110 km/h suele ser mortal). También se puede saltar de las aeronaves.
- **Apuntar desde el vehículo** (clic derecho): el ángulo es relativo al coche, sin saltos de cámara.
- **Río Vinalopó transitable** por escaleras entre los pretiles. El puente de Santa Teresa ya no tiene muros en la calzada.
- **Estancos, peluquerías y pensiones con interior**:
  - En el estanco se compra tabaco.
  - En la peluquería hay 15 cortes: te sientas y el barbero te corta; el corte se guarda.
  - En la pensión puedes dormir 8 horas y recuperar la salud.
- **Ruleta de acciones (U)**:
  - Acciones: fumar, sentarse, tumbarse, acostarse, bailar, gestos y otras.
  - Tiene en cuenta el contexto: bancos, sillas, sofás, camas y si llevas tabaco.

## Vehículos propios, daño y conducción

- **Concesionarios**:
  - Hay dos: Elx Motor (coches) y Motos Vinalopó.
  - El catálogo tiene 36 modelos en 7 categorías: utilitarios, berlinas, deportivos, SUV y 4x4, clásicos, furgonetas y pick-ups, y motos.
  - Cada modelo tiene su precio, velocidad punta, aceleración, frenada, agarre y dirección, y se nota al conducir.
  - La ficha muestra km/h, el 0-100, la frenada y el manejo. Puedes elegir color y el coche gira en la plataforma. Para añadir modelos basta con añadir una línea a `VEH_MODELS`.
- **Casa propia con garaje**:
  - Es refugio y punto de guardado, y se puede dormir.
  - El garaje está cerrado y tiene 6 plazas físicas.
  - Al subir a un vehículo guardado hay un fundido corto y apareces conduciendo en la calle. Para guardarlo, entras por la persiana.
- **Un solo vehículo personal activo**: su posición se guarda siempre y aparece con un icono azul de coche en el mapa. Sacar o recibir otro devuelve el anterior al garaje.
- **Alberto, el aparcacoches**:
  - Su contacto llega al teléfono con tu primera compra.
  - Por 50 € te trae el vehículo que elijas y te entrega las llaves.
  - Si dejas tu vehículo abandonado, lo devuelve al garaje.
- **Daño por zonas**:
  - Depende de la velocidad del impacto, de la resistencia del vehículo y de dónde golpea (frontal, trasero o laterales). La chapa se abolla en el punto del golpe y las lunas se agrietan.
  - Con el motor destrozado el coche deja de andar sin arder. El fuego solo llega con daño extremo.
- **Conducción**: el volante se centra solo al soltarlo, así que el coche va recto. La cámara va fija detrás del vehículo (el ratón no la mueve al conducir) y con **B** miras hacia atrás.

## Cómo seguir en local

Todo el juego está en `ilici-city/index.html`, un único archivo. Clona el repositorio, cambia a la rama `claude/gracious-babbage-rbramm` (o a `main` si ya has fusionado el PR) y abre el archivo en el navegador, o sirve la carpeta con `python -m http.server`. Necesita internet para cargar three.js desde el CDN.

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
