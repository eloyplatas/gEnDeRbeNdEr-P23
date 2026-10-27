# GenderBender P23

Versión de GenderBender con 4 canales para la **SOMA Pulsar-23**: **BD**, **BASS**, **SD** y **HHT**. Usa los mismos estilos de 7 voces de `drum_styles_v/`, el mismo pad XY, la misma densidad, el mismo break y el mismo groove (swing y slide). Manda MIDI a la Pulsar por su entrada DIN.

## Qué cambia respecto a GenderBender

| | GenderBender | P23 |
|---|---|---|
| Canales | 7 (kick … lotom) | 4 (BD, BASS, SD, HHT) |
| Estilo | uno por voz | uno por canal |
| Voces del estilo | cada voz es un canal | cada canal toma una o dos voces del estilo (**SOURCE**) |
| Densidad | umbral sobre 4 niveles (4 puntos de cambio) | cuenta golpes de uno en uno, distinto en cada compás de un ciclo de 8; 25 % = patrón escrito |
| Compás | siempre 32 pasos (4/4) | 4/4, 3/4, 6/8, 5/8 y 7/8 según el estilo |
| Velocidad | fija por voz | fija o sacada del patrón (**DYN**) |
| Duración | ticks | ms (**GATE**): en la Pulsar es el sustain |
| Notas | `basenote` + voz, canal 1 | fijas: BD 36, SD 38, HHT 42 (canal 10) · BASS 36 (canal 2) |
| Learn | — | botón **TEST** por canal |

### SOURCE: qué voz del estilo toca cada canal

| SOURCE | Voz principal | Voz ALT |
|---|---|---|
| KICK, SNARE, CLAP, HH CL, HH OP, HI TOM, LO TOM | esa voz | — |
| SN+CLAP | snare | clap |
| HH CL+OP | hat cerrado | hat abierto |
| TOMS | tom bajo | tom alto |

Valores por defecto (botón **SRC RST**): BD ← KICK, BASS ← TOMS, SD ← SN+CLAP, HHT ← HH CL+OP.

Si en un paso suenan las dos voces, gana la ALT. Un golpe ALT usa su propio gate (**ALT GT**; **OPEN** en el HHT). En el BASS, además, suma **ALT +** semitonos a la nota. En BD, SD y HHT la voz ALT usa la misma nota, porque esos módulos de la Pulsar solo responden a la nota aprendida. Así es como salen:

- **Hat abierto:** el HHT con un gate largo (**OPEN GT**, 250 ms por defecto). Como la envolvente de la Pulsar mantiene el sustain mientras dura la nota, un gate largo es un hat abierto. Si llega un hat cerrado antes de que acabe, lo corta, igual que un hi-hat real.
- **Línea de bajo:** el tom bajo toca la nota del BASS y el tom alto, esa nota + 12 (ajustable). Necesita la BASS en modo MIDI.

## Puesta en marcha con la Pulsar

1. **REAPER:** inserta *MIDI GenderBender P23* en una pista. En el botón de ruteo de la pista, pon la **salida MIDI por hardware** en el interfaz MIDI que va a la Pulsar. El plugin solo genera notas con el transporte en marcha (salvo el botón TEST).
2. **Learn en la Pulsar (una vez):** mantén pulsado **LRN** del módulo (BD, SD, HHT, BASS) y pulsa **TEST** en el canal correspondiente del plugin. La Pulsar guarda la asignación al apagarla.
3. **Canales MIDI (fijos):** BD, SD y HHT salen por el canal 10 con las notas 36, 38 y 42, y el BASS por el canal 2 con la nota 36 (más ALT + en los golpes ALT). El BASS va en un canal propio porque en modo MIDI toca cromático todo lo que llega por su canal.
4. **BASS:** con el conmutador en **MIDI** toca la nota que manda el plugin, incluido el intervalo ALT +. En **CV** solo responde a la tecla aprendida: pon ALT + a 0 o los golpes ALT no sonarán. En **PRC**, según el manual de SOMA, sigue el tono si su canal es distinto del de la batería; compruébalo en tu unidad.
5. **Velocidad:** la Pulsar responde a la velocidad. **VEL** fija el máximo y **DYN** cuánto pesan los niveles del estilo (X=255, x=170, o=120, -=60). Con DYN 0, todos los golpes van a VEL.
6. **Gate:** **GATE** es el tiempo que la nota mantiene la envolvente abierta. Las ruedas **ATT** y **REL** de cada módulo de la Pulsar siguen dando forma al sonido. Gates muy largos (cientos de ms) convierten BD, SD o HHT en tonos o ruido sostenido.

### Reloj

El plugin sigue el tempo de REAPER y no necesita que la Pulsar esté sincronizada. Los looper-recorders de la Pulsar no graban MIDI, solo lo que se toca en sus sensores. Si además quieres los divisores y los loopers de la Pulsar a tempo, activa en REAPER el envío de reloj MIDI al dispositivo (Preferencias → MIDI Devices → salida → *Send clock/SPP*). En la Pulsar, pon el conmutador de reloj en **MIDI** y conecta **LRST** con **0.25**, como recomienda su manual.

## Controles

Por canal:

| Control | Qué hace |
|---|---|
| STYLE | estilo del canal (‹ ›, rueda o clic para la lista) |
| SOURCE | voces del estilo que toca el canal |
| DENS | 0–100 %, en pasos de 0,1. **25 % = el patrón tal como está escrito.** Por debajo se quitan golpes de uno en uno (primero los más débiles; los fuertes se quedan) y en 0 % no suena nada. De 25 a 100 % se añaden, de uno en uno, los adornos (x, o, -), después golpes "prestados" de los otros patrones del estilo y al final rellenos en los pasos vacíos, hasta llenar todos los pasos en 100 % |
| DIV | velocidad de la rejilla (x1 = el patrón tal cual, 32 pasos por compás) |
| BREAK | rejilla que usa el canal en la ventana de break (OFF = sin break) |
| VEL / DYN | velocidad máxima / peso del nivel del patrón |
| GATE / ALT GT | duración en ms del golpe principal / del ALT (OPEN en el HHT) |
| SWING | cuánto del swing global usa el canal |
| SLIDE | adelanta o retrasa el canal ±30 ms |
| ALT + | solo BASS: semitonos que se suman en los golpes ALT |
| TEST | manda la nota del canal (para el LRN de la Pulsar) |

Debajo de cada canal se muestra su salida MIDI fija.

**Cómo ordena DENS los golpes.** Cada paso tiene una prioridad según su nivel en el patrón: X > x > o > - > golpe prestado (la voz tiene golpe en ese paso en alguno de sus otros 8 patrones) > vacío. Dentro del mismo nivel van primero los pulsos del compás, luego las corcheas, las semicorcheas y las fusas, y en empate decide un orden pseudoaleatorio. El orden se recalcula con la posición del pad.

**Variedad en el tiempo.** Las X del patrón siguen siempre el mismo orden, así que el esqueleto del ritmo se mantiene. Lo que DENS añade cambia de orden en cada par de compases de un ciclo de 8. Además, cada golpe nuevo entra primero en un compás del ciclo, luego en otro…, así que el knob tiene cientos de posiciones distintas y el groove evoluciona en vez de repetir el mismo bucle. A 0, 25 y 100 % todos los compases son iguales. Los golpes añadidos suenan más flojos que los del patrón (con DYN > 0) y con una pequeña variación de velocidad.

Los rellenos en pasos vacíos solo los pone la voz principal; la ALT llega hasta sus golpes prestados.

### Compases

Algunos estilos están en otro compás, indicado en su nombre: `(3-4)`, `(6-8)`, `(5-8)` o `(7-8)`. El canal hace entonces el bucle con 24, 20 o 28 pasos en lugar de 32, el compás aparece junto a STYLE y la tira de pasos muestra solo los del bucle. Pon el compás del proyecto de REAPER igual (por ejemplo, 6/8 para la muiñeira) para que coincidan las barras. El tempo del nombre está en negras: una muiñeira a 180 es negra con puntillo = 120. Si cada canal lleva un compás distinto, sale polimetría.

Globales: **XY PAD** (mezcla de los 9 patrones; clic derecho o ctrl+clic = centro), **SWING** (50–75 %, tipo MPC) y **BREAK**: cada cuántos tiempos (EVERY), cuántos dura (LENGTH), a partir de qué tiempo (OFFSET) y RANDOM. Durante el break, el canal usa el 75 % de su DENS menos un aleatorio de hasta RANDOM puntos.

Knobs: se arrastran en vertical, con shift para ajuste fino o con la rueda. Clic derecho o ctrl+clic vuelve al valor por defecto. Todo es automatizable desde REAPER.

La tira de 32 celdas de cada canal muestra el patrón que suena con el pad, la densidad y el compás actuales. Color = suena, blanco = golpe ALT, color corto = relleno en un paso vacío, tenue = golpe del patrón que la densidad deja fuera.

La cabecera indica cuántos estilos ha encontrado el plugin en `Data/drum_styles_v`. Si pone *no styles found*, la carpeta de estilos no está donde REAPER la busca.

## Detalles

- El pad reproduce exactamente las fórmulas de GenderBender, así que las zonas de cada estilo (centro = p4/p5, etc.) son las mismas. Una diferencia mínima: con X < 0 e Y = 0 exacto, el original conservaba el cuadrante anterior y aquí siempre se usa el cuadrante inferior izquierdo.
- El proyecto guarda el nombre de archivo de cada estilo. Si añades estilos y cambia el orden de la lista, el proyecto recupera los mismos estilos.
- El planificador es el de GenderBender: notas con precisión de sample, swing por deformación de la corchea, slide con 30 ms de anticipación, re-disparo sin notas colgadas y NoteOff de todo al parar.

## Instalación

`sh tools/install.sh` copia el plugin en `Effects/GenderBenderP23/` y los estilos en `Data/drum_styles_v/`, y genera `Data/drum_styles_v_list.txt` con la lista de estilos.

A mano, copia:
- `GenderBenderP23/genderbender_p23.jsfx` en `Effects/GenderBenderP23/`;
- los estilos en `Data/drum_styles_v/`;
- `drum_styles_v_list.txt` en `Data/`.

### Cómo encuentra los estilos

El plugin lee la lista de la carpeta `Data/drum_styles_v` a través de un slider de archivo oculto. Si eso no funciona en tu host, usa `Data/drum_styles_v_list.txt` (un nombre de archivo por línea). La cabecera indica cuántos estilos hay y si vienen de la lista (*list file*). Si añades estilos a mano y la cabecera dice *list file*, vuelve a ejecutar `install.sh` o añade el nombre a esa lista.

El estilo de cada canal es un parámetro numérico (su posición en la lista), igual que los knobs. Los archivos se abren por su nombre, y el proyecto guarda el nombre: si la lista cambia, recupera el mismo estilo.

El color del nombre del estilo indica su estado: **blanco** = cargado; **gris** = pendiente (se carga en el siguiente bloque de audio); **rojo** = no se pudo abrir el archivo.
