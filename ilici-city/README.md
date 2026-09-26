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
| E / Enter | Entrar, robar un coche o salir |
| Espacio | Freno de mano (en coche) / correr (a pie) |
| F / clic | Puñetazo |
| H | Claxon |
| C | Cámara normal / cenital |
| M | Mapa |
| P / Esc | Pausa y lista de misiones |

En móvil aparecen un joystick y botones táctiles.

## Qué incluye

- **Mapa de Elche estilizado**: el río Vinalopó cruza la ciudad por un cauce hundido, con 6 puentes. Hay barrios con su propio estilo de edificios (Centro Histórico, El Raval, Carrús, El Toscar, El Pla, Altabix, Los Palmerales y el polígono) y las avenidas de Novelda, Alicante y Santa Pola.
- **Monumentos**: Basílica de Santa María (cúpula azul), Palacio de Altamira, Torre de la Calahorra, Ayuntamiento con la Calendura, La Glorieta, Mercado Central, Parque Municipal, Huerto del Cura con la Palmera Imperial, Estadio Martínez Valero, Campus UMH, Hospital General, Comisaría y Estación.
- **Unas 2.800 palmeras**: palmerales, huertos y las orillas del río.
- **Tráfico y peatones**: los coches circulan por la derecha y siguen la red de calles. Los peatones caminan por las aceras, cruzan la calle y huyen si pasa algo.
- **Sistema de búsqueda de 5 estrellas**: la policía te persigue calculando rutas por las calles. Te detiene si te quedas quieto y las estrellas bajan si la despistas.
- **Daños**: los coches echan humo, se incendian y explotan.
- **5 misiones**: Dátiles para la abuela, Taxi al Martínez Valero, Carrera del Palmeral, El deportivo del míster y La Nit de l'Albà (termina con fuegos artificiales).
- **12 dátiles de oro** escondidos, a 100 € cada uno.
- **Ciclo de día y noche**: las ventanas se iluminan de noche y hay farolas y faros.
- **Progreso guardado** en el navegador (localStorage).

El mapa se basa en la geografía real de Elche, pero no es un plano exacto. Las calles siguen una cuadrícula para que el juego funcione bien.

## Ideas para seguir

- Cargar las calles reales de Elche desde OpenStreetMap (requiere acceso a la API de Overpass).
- Armas, más tipos de misiones, radio con música y modelos de coche más detallados.
- Multijugador.
