# GenderBender

A MIDI drum-pattern generator for REAPER (JSFX plugin). It plays 7 voices (kick, snare, clap, closed hat, open hat, high tom, low tom) from styles of 9 patterns each, blended with an XY pad.

**[See every style's patterns →](https://toast3r.github.io/genderbender/fingerprints.html)**

## Install

```sh
sh tools/install.sh                                   # macOS
REAPER_DIR="$APPDATA/REAPER" sh tools/install.sh     # Windows (Git Bash) or another folder
```

**SOMA Pulsar-23:** `GenderBenderP23/` is a 4-channel version (BD, BASS, SD, HHT) that sends MIDI to the Pulsar, with per-channel note/channel, velocity from the pattern and gate length as sustain. See [GenderBenderP23/README.md](GenderBenderP23/README.md).

In REAPER, add **MIDI GenderBender** to a track, send its MIDI to a drum sampler (base note 36), and press play. **ALL RND** picks a random style for all voices, **EACH RND** one per voice.

Other DAWs: load `Effects/GenderBender/genderbender.jsfx` in the [ysfx](https://github.com/JoepVanlier/ysfx) instrument plugin (VST3/AU/CLAP). Install with `REAPER_DIR=<some folder> sh tools/install.sh` so `Effects/` and `Data/` sit side by side.

## Writing a style

Write a `.style` file in `styles_src/`, build it, and check it:

```sh
python3 tools/make_style.py build styles_src/cumbia_villera_98.style    # -> drum_styles_v/CUMBIA VILLERA 98.txt
python3 tools/make_style.py decode "drum_styles_v/GQOM.txt"            # print an existing style as a grid
python3 tools/view_styles.py                                           # update docs/fingerprints.html
python3 tools/check_styles.py                                          # must print "ok"
```

```
name: MY STYLE 120
[p4 p5]                       # these patterns get the lines below
kick   X... .... X... ....    # 16 chars = 16ths, 32 = 32nds; spaces ignored
hhc    XXxX XXxX XXxX XXxX
```

- Levels: `X=255 x=170 o=120 -=60 .=0`, or `[n]` for 0–255. At default density only `X` plays.
- Voices: `kick`, `snare`, `clap`, `hhc`, `hho`, `hitom`, `lotom`.
- Never edit `drum_styles_v/*.txt` by hand: a bad file silences the plugin with no error.

## Layout

| Path | What it is |
|------|------------|
| `GenderBender/` | The plugin, its background and preset library |
| `GenderBenderP23/` | 4-channel version for the SOMA Pulsar-23 |
| `drum_styles_v/` | Styles the plugin loads |
| `styles_src/` | Readable style sources |
| `tools/` | Style build/check scripts and the installer |
| `docs/` | Style fingerprints page (GitHub Pages) |
| `editor/`, `presets/` | The original SuperCollider style editor and its presets |
| `openspec/` | Specs and change proposals |

## Included styles

| Family | Styles (BPM) |
|--------|--------------|
| Cumbia | CUMBIA COLOMBIANA (95), CUMBIA SONIDERA (92), CUMBIA VILLERA (98), CUMBIA DIGITAL (100), CUMBIA REBAJADA (72), CUMBIA PERUANA (100), CUMBIA TROPICAL (104), CUMBIA RAPIDITA (112) |
| Footwork / juke | 101 JUKE, Juke160 (160) |
| Reggaeton / dancehall | 101 RAGATON |
| House | Chicago.Jouse 125 (125), JetoHouse 135 (135), MIAMI BEIGE 135 (135) |
| UK garage / 2-step | Two-stepppo, uk_fungui, uk_garbage |
| Grime | GRIME140 (140), Grimer140 (140) |
| Dubstep | DUBSTEP140 (140), DubSteppo |
| Drum & bass | drumbass, DurumBass160 (160) |
| Techno | techAXX, TekkBooooring, TekkChungo, TekkThump |
| R&B / trap | RB, WCOAST R&B 110 (110), VAPORTRAP |
| Gqom | GQOM |
| Galicia | MUINEIRA NOVA 180 (6-8), MUINEIRA VELLA 172 (6-8), RIBEIRANA 186 (6-8), MUINEIRA GOLPE 132 (6-8), CARBALLESA 176 (6-8), MUINEIRA REDONDA 178 (6-8), CHOUTEIRA 182 (6-8), CONTRAPASO 168 (6-8), XOTA 168 (3-4), XOTA DE PANDEIRETA 160 (3-4), FOLIADA 150 (3-4), ALBORADA (100), ALBORADA 96 (3-4), PASODOBRE (116), POLCA (120), MAZURCA 132 (3-4), VALSE 160 (3-4), XOTIS (104), PASARRUAS (108), MUINEIRA TECHNO 180 (6-8), PANDEIRADA BASS 165 (6-8), XOTA DUB 82 (3-4), ALALA ESPAZO (60), MUINEIRA DE ROMARIA 186 (6-8) |
| Iberia & Mediterranean | SEVILLANAS 180 (3-4), RUMBA FLAMENCA (104), TANGOS FLAMENCOS (110), FANDANGO DE HUELVA 170 (3-4), TARANTELLA 190 (6-8), DABKE (125), MAQSUM (110), BALADI (100), MALFUF (140), AYOUB (120), GNAWA 120 (6-8), RUCENICA 140 (7-8), KALAMATIANOS 130 (7-8), PAIDUSHKO 160 (5-8), RUMBA CATALANA (110) |
| Africa | AFROBEAT (112), HIGHLIFE (128), SOUKOUS (140), MBALAX (125), KUDURO (140), KWAITO (112), AMAPIANO (113), AFRO HOUSE (122), SHANGAAN ELECTRO (186), SINGELI (210), AFROBEATS (104), RUMBA CONGOLESA (120), AFROBEAT FELA (120), JUJU (110) |
| Latin America & Caribbean | SALSA (95), GUAGUANCO (105), BOMBA SICA (115), PLENA (120), MERENGUE (130), SAMBA (100), BOSSA NOVA (130), BAIAO (95), MARACATU (90), AFOXE (100), FUNK CARIOCA (130), CANDOMBE (110), TANGO (120), MILONGA (110), REGGAE ONE DROP (76), REGGAE STEPPERS (76), DANCEHALL (100), SOCA (155), DEMBOW (115), MOOMBAHTON (108), REGGAETON CLASICO (95), REGGAETON PERREO (100), REGGAETON MODERNO (90), RUMBA YAMBU (90), RUMBA COLUMBIA 115 (6-8), TANGO CANYENGUE (110), TANGO NUEVO (115), TANGO ELECTRONICO (115), TANGO VALS 165 (3-4), VALS PERUANO 150 (3-4), SALSA DURA (105), SALSA ROMANTICA (92), SON CUBANO (100), MAMBO (110), CHA CHA CHA (120), TIMBA (105) |
| Asia & Middle East | DANGDUT (140), KEHERWA (100), TEENTAAL (120), DADRA 100 (6-8), BHANGRA (100) |
| Techno | DETROIT TECHNO (128), MINIMAL TECHNO (126), DUB TECHNO (120), ACID TECHNO (135), HARD TECHNO (150), RAVE TECHNO (145), HYPNOTIC TECHNO (130), TECH HOUSE (125) |
| House & disco | DEEP HOUSE (120), ACID HOUSE (124), GARAGE HOUSE (122), FRENCH FILTER HOUSE (124), DISCO (118), ITALO DISCO (120), NEW BEAT (110), PROGRESSIVE HOUSE (124), UK FUNKY (130), SPEED GARAGE (132), BASSLINE (136), MICROHOUSE (122) |
| Trance & hard dance | TRANCE (138), PSYTRANCE (145), DARK PSY (150), BIG ROOM (128), HARDSTYLE (150), GABBER (180), SPEEDCORE (230) |
| Breaks, jungle & drum & bass | AMEN JUNGLE (165), BREAKBEAT HARDCORE (150), JUMP UP (174), NEUROFUNK (172), LIQUID DNB (172), HALFTIME (170), NU SKOOL BREAKS (132), BIG BEAT (115) |
| Club & bass | MIAMI BASS (128), BALTIMORE CLUB (130), JERSEY CLUB (140), BALLROOM VOGUE (130), ELECTRO FUNK (110), SYNTHWAVE (110), HYPERPOP (160), DECONSTRUCTED CLUB (130), WITCH HOUSE (70), DRIFT PHONK (130), DUBSTEP HALFTIME (140), DUBSTEP RIDDIM (140), DUBSTEP TRIBAL (140), BROSTEP (150) |
| Hip hop | BOOM BAP (90), GOLDEN ERA (95), DILLA SWING (88), LO FI HIP HOP (78), G FUNK (94), CRUNK (76), UK DRILL (142), NY DRILL (142), TRAP (140), JAZZ HOP (90), FUNKY DRUMMER (100), ABSTRACT HIP HOP (86), OLD SCHOOL RAP (100), NEW ORLEANS BOUNCE (100), WEST COAST RAP (92), TRAP SOUL (65), TRAP LATINO (90), PLUGG (150), ATLANTA TRAP (135), CHICAGO DRILL (140) |
| Trip hop & downtempo | BRISTOL (88), TRIP HOP CINEMATIC (76), DARK TRIP HOP (72), TRIP HOP DUB (80), ILLBIENT (85), DOWNTEMPO BREAKS (95) |
| Industrial & dark | EBM (125), INDUSTRIAL METAL (110), METAL PERCUSSION (112), RHYTHMIC NOISE (150), POST PUNK (140), DEATH INDUSTRIAL (70) |
| Breakcore & extreme | BREAKCORE AMEN (180), RAGGA BREAKCORE (175), SNARECORE 170 (7-8), DRILL N BASS (180) |
| IDM & experimental | IDM GLITCH (110), BRAINDANCE (160), ALGORITMICA (98), WONKY (90), GLITCH HOP (105), MOTORIK (135), KRAUT FUNK (115), POLIRRITMO 3 CONTRA 4 (110), POLIRRITMO 5 CONTRA 4 (100), STOCHASTIC (100), NOISE BLASTS (140), CLAPPING MUSIC 160 (6-8), EUCLIDES (120) |
| Ambient | AMBIENT PULSE (70), AMBIENT TECHNO (115), AMBIENT DUB (70), DRONE PULSE (60) |
| Reggae, dub & rocksteady | SKA (160), ROCKSTEADY (80), ROOTS REGGAE (72), REGGAE ROCKERS (76), REGGAE FLYERS (78), NYABINGHI (70), DUB (70), UK DUB STEPPERS (140), LOVERS ROCK (74), DANCEHALL DIGITAL (95), DANCEHALL DIWALI (98) |
| Jazz & blues | SWING JAZZ (160), BEBOP (240), JAZZ BALLAD BRUSHES (70), JAZZ WALTZ 150 (3-4), HARD BOP (180), SONGO (110), AFRO CUBAN BEMBE 150 (6-8), MODAL JAZZ 150 (6-8), JAZZ FUNK (100), FREE JAZZ (120), COOL JAZZ (130), SECOND LINE (100), BLUES SHUFFLE (120), SLOW BLUES 82 (6-8), CHICAGO BLUES (110), TEXAS SHUFFLE (130), BOOGIE WOOGIE (160), DELTA BLUES (90) |
| Soul & funk | MOTOWN SOUL (120), NORTHERN SOUL (125), NEO SOUL (85), SOUL BALLAD 90 (6-8), FUNK JB (108), PHILLY SOUL (115) |
| Metal | BLACK METAL BLAST (220), BLACK METAL SKANK (180), ATMOSPHERIC BLACK (150), DOOM METAL (60), FUNERAL DOOM (40), SLUDGE (75), STONER ROCK (95), TECH DEATH BLAST (240), TECH DEATH 170 (7-8), DEATH METAL GROOVE (120), THRASH SKANK (200), THRASH GALLOP (180), THRASH DOUBLE BASS (170) |
| Flamenco | SOLEA 90 (6-8), ALEGRIAS 130 (6-8), BULERIAS 120 (6-8), SOLEA POR BULERIAS 100 (6-8), SIGUIRIYA 75 (6-8), GUAJIRA 110 (6-8), TANGUILLOS 170 (6-8), TIENTOS (70), FARRUCA (100) |
| European folk | VALS VIENES 180 (3-4), VALS LENTO 90 (3-4), VALS MUSETTE 160 (3-4), IRISH JIG 180 (6-8), IRISH REEL (200), IRISH HORNPIPE (150), IRISH SLIDE 190 (6-8), IRISH POLKA (130), POLSKA 120 (3-4), HUMPPA (130), HORA (136), AN DRO (120), JOTA ARAGONESA 200 (3-4), SARDANA 110 (6-8), STRATHSPEY (116), FADO (70), KOLO (140), LANDLER 120 (3-4) |
| African traditional | KUKU (120), DJOLE (125), KASSA (115), SOLI 90 (6-8), AGBEKO 90 (6-8), GAHU (120), KPANLOGO (120), BOBOBO (125), ADOWA 100 (6-8), MBIRA SHONA 120 (6-8), BIKUTSI 150 (6-8) |
| Other | ESTAIL, TEST2, ZZZZ BLACK |

This table also sets the families on the fingerprints page, so keep its format.

Styles tagged `(6-8)`, `(3-4)`, `(5-8)` or `(7-8)` are in that meter: GenderBender P23 loops them with the right length (24, 20 or 28 of the 32 steps). The original GenderBender always plays 32 steps, so they sound cut short there. In the sources, `meter: 6/8` adds the tag (see `tools/make_style.py`).

## Contributing

GenderBender is free software and contributions are welcome: new styles, bug fixes, ideas. Open an [issue](https://github.com/TOAST3R/genderbender/issues) to report a problem or suggest something, or fork the repo and send a pull request. For a new style, include its `.style` source and make sure `tools/check_styles.py` prints `ok`.

Bigger changes go through [OpenSpec](https://github.com/Fission-AI/OpenSpec) (`npm install -g @fission-ai/openspec@1.3.1`, then `/opsx:propose`, `/opsx:apply`, `/opsx:archive`). AI agents: read `AGENTS.md`.

## License

Original version by Sergio Millán. Released under the [GNU GPL v3](LICENSE): you can use, study, modify and share it, and modified versions you distribute must stay under the GPL.
