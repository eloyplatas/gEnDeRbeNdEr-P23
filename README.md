# gEnDeRbeNdEr-P23
GenderBender generative sequencer for Soma Pulsar 23


<img width="855" height="469" alt="Captura de pantalla_2026-10-27_01-25-48" src="https://github.com/user-attachments/assets/c1e160fd-395f-44dd-bf93-4814d760955c" />

GenderBender P23 is a MIDI drum-pattern generator for REAPER (JSFX), built to play the four voices of the SOMA Pulsar-23 drum machine: BD, BASS, SD and HHT. It is based on GenderBender, the original 7-voice pattern generator by Sergio Millán (GPL v3), and it sends MIDI only: the sound comes from the Pulsar.
 
What it does
 
Each of the four channels loads a style: 9 patterns of up to 32 steps, with levels that separate essential hits from ornaments. An XY pad blends the patterns, from intro and base to energy, variation and fill. A density control removes or adds notes, and swing, per-channel slide and automatic breaks (rolls and stutters at the end of each phrase) shape the groove. Every note is scheduled to the exact sample, with no hung notes on stop, loop or seek.


 
What is new compared with the original GenderBender
 
- Four channels mapped to the Pulsar-23. Each channel takes one or two voices from a style: kick to BD, snare and clap to SD, closed and open hat to HHT, and the toms as a bass line on BASS. The second voice (ALT) has its own gate, and on the BASS it can play an octave or any interval above.

- Fixed MIDI output ready for the Pulsar: BD, SD and HHT on channel 10 (notes 36, 38, 42) and BASS on channel 2 (note 36). A TEST button per channel sends the note for the Pulsar's MIDI learn (LRN).

- Gate in milliseconds, used as the Pulsar's sustain: short gates are hits, long gates turn a voice into a tone or noise. The open hat is a long gate that the next closed hat cuts.

- Velocity from the pattern (DYN): accents and ghost notes in the style become dynamics, which the original did not do.

- A new density engine. 25 % plays the pattern as written; below that, hits are removed one by one, weakest first; above it, ornaments, hits borrowed from the style's other patterns and fills enter one by one. What density adds changes from bar to bar over an 8-bar cycle while the skeleton stays fixed. The knob has hundreds of distinct positions instead of 4.

- Meters: styles can be in 4/4, 3/4, 6/8, 5/8 or 7/8, and each channel loops with the right length. Different meters on different channels give polymeter.

- 162 new styles, 193 in total: Galician traditional rhythms (muiñeira nova and vella, ribeirana, carballesa, xota, foliada, alborada, pasodobre, mazurca and more), world music (flamenco, Balkans, Maghreb, Africa, Latin America, India), techno, house, trance, jungle and drum & bass, club, hip hop, trip hop, industrial, breakcore, IDM, experimental and ambient.

- A new interface: per-channel step view of what is playing now, a real XY pad, activity LEDs, style menus, and random style buttons (one style for all channels, or one per channel).

- Robust style handling: styles are opened by name, projects recall styles by name even if the list changes, and a backup style list is used when the host cannot list the folder.

- Style tools: make_style.py accepts a meter line, and the fingerprints page shows every pattern of every style.

- PDF Manual in English, Galego and Castellano

GenderBender P23 is free software under the GNU GPL v3.





- Style tools: make_style.py accepts a meter line, and the fingerprints page shows every pattern of every style.
 
GenderBender P23 is free software under the GNU GPL v3.
