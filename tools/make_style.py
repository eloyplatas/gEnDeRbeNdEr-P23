#!/usr/bin/env python3
"""Genera y decodifica estilos de GenderBender (drum_styles_v/*.txt).

  python3 tools/make_style.py build styles_src/cumbia_colombiana_95.style [salida.txt]
  python3 tools/make_style.py decode "drum_styles_v/GQOM.txt" [salida.style]

Formato .style:
  # comentario                    (tambien al final de una linea)
  name: CUMBIA COLOMBIANA 95      (nombre del .txt de salida por defecto)
  [p4 p5]                         (las lineas siguientes se aplican a esos patrones)
  kick   X... .... X... ....      (16 caracteres = semicorcheas, 32 = fusas; espacios ignorados)

  meter: 6/8                      (opcional, antes de los bloques: 4/4 por defecto)

  Escala: X=255 x=170 o=120 -=60 .=0, o [n] para un valor 0-255 exacto.
  Compases: 4/4 = 16 o 32 caracteres por compas; 3/4 y 6/8 = 12 o 24; 5/8 = 10 o 20; 7/8 = 14 o 28.
  Con un compas distinto de 4/4 se usan los primeros pasos (24, 20 o 28) y el resto queda a 0;
  el nombre recibe la etiqueta "(6-8)", "(3-4)", "(5-8)" o "(7-8)", que GenderBender P23 lee
  para hacer el bucle con esa longitud. El GenderBender original siempre recorre 32 pasos.
  Voces: bdrum|kick, sdrum|snare, clap, hhclosed|hhc, hhopen|hho, hitom, lotom.
  Un bloque posterior sobrescribe las voces que nombra; lo no definido queda a 0.
"""
import os
import sys

VOICES = ['bdrum', 'sdrum', 'clap', 'hhclosed', 'hhopen', 'hitom', 'lotom']
ALIASES = {'kick': 'bdrum', 'snare': 'sdrum', 'hhc': 'hhclosed', 'hho': 'hhopen'}
SCALE = {'X': 255, 'x': 170, 'o': 120, '-': 60, '.': 0}
SYMBOL = {v: k for k, v in SCALE.items()}
PATTERNS = 9
STEPS = 32
# compas -> (pasos del bucle a resolucion de fusa, etiqueta del nombre)
METERS = {'4/4': (32, ''), '3/4': (24, '(3-4)'), '6/8': (24, '(6-8)'),
          '5/8': (20, '(5-8)'), '7/8': (28, '(7-8)')}
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


class StyleError(Exception):
    pass


def parse_grid(text, lineno, steps=STEPS):
    vals, i = [], 0
    text = text.replace(' ', '').replace('\t', '')
    while i < len(text):
        c = text[i]
        if c == '[':
            end = text.find(']', i)
            if end < 0:
                raise StyleError(f'linea {lineno}: falta "]"')
            try:
                v = int(text[i + 1:end])
            except ValueError:
                raise StyleError(f'linea {lineno}: valor no numerico "{text[i:end + 1]}"')
            if not 0 <= v <= 255:
                raise StyleError(f'linea {lineno}: valor fuera de 0-255: {v}')
            vals.append(v)
            i = end + 1
        elif c in SCALE:
            vals.append(SCALE[c])
            i += 1
        else:
            raise StyleError(f'linea {lineno}: caracter no valido "{c}"')
    if len(vals) == steps // 2:
        expanded = [0] * STEPS
        expanded[0:steps:2] = vals
        return expanded
    if len(vals) == steps:
        return vals + [0] * (STEPS - steps)
    raise StyleError(f'linea {lineno}: la cuadricula tiene {len(vals)} pasos '
                     f'(deben ser {steps // 2} o {steps})')


def parse_style(source):
    """Devuelve (nombre, patrones[voz][patron][paso])."""
    name = None
    data = [[[0] * STEPS for _ in range(PATTERNS)] for _ in VOICES]
    block = None
    steps, tag = METERS['4/4']
    for lineno, raw in enumerate(source.splitlines(), 1):
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        if line.lower().startswith('name:'):
            name = line[5:].strip()
            continue
        if line.lower().startswith('meter:'):
            meter = line[6:].strip()
            if meter not in METERS:
                raise StyleError(f'linea {lineno}: compas "{meter}" no soportado ({", ".join(METERS)})')
            if block is not None:
                raise StyleError(f'linea {lineno}: "meter:" debe ir antes de los bloques')
            steps, tag = METERS[meter]
            continue
        if line.startswith('['):
            if not line.endswith(']'):
                raise StyleError(f'linea {lineno}: cabecera de bloque mal cerrada')
            block = []
            for tok in line[1:-1].split():
                if not (tok[:1] == 'p' and tok[1:].isdigit() and int(tok[1:]) < PATTERNS):
                    raise StyleError(f'linea {lineno}: patron desconocido "{tok}" (p0-p8)')
                block.append(int(tok[1:]))
            if not block:
                raise StyleError(f'linea {lineno}: bloque sin patrones')
            continue
        voice, _, grid = line.partition(' ')
        voice = ALIASES.get(voice, voice)
        if voice not in VOICES:
            raise StyleError(f'linea {lineno}: voz desconocida "{voice}"')
        if block is None:
            raise StyleError(f'linea {lineno}: voz fuera de un bloque [pN]')
        vals = parse_grid(grid, lineno, steps)
        for p in block:
            data[VOICES.index(voice)][p] = list(vals)
    if name and tag and not name.endswith(tag):
        name = f'{name} {tag}'
    return name, data


def to_txt(data):
    # mismo formato que drummermenu.scd: patrones separados por tab, voces por '/', tab final
    out = ''
    for vi, voice in enumerate(VOICES):
        out += ''.join(f'{voice}{p}|' + ','.join(str(v) for v in data[vi][p]) + '\t'
                       for p in range(PATTERNS))
        if vi < len(VOICES) - 1:
            out = out[:-1] + '/'
    return out


def from_txt(text):
    voices = text.split('/')
    if len(voices) != len(VOICES):
        raise StyleError(f'se esperaban {len(VOICES)} voces y hay {len(voices)}')
    data = []
    for vi, chunk in enumerate(voices):
        entries = [e for e in chunk.split('\t') if e]
        if len(entries) != PATTERNS:
            raise StyleError(f'voz {VOICES[vi]}: {len(entries)} patrones (se esperaban {PATTERNS})')
        pats = []
        for p, entry in enumerate(entries):
            label, _, nums = entry.partition('|')
            if label != f'{VOICES[vi]}{p}':
                raise StyleError(f'etiqueta inesperada "{label}" (se esperaba {VOICES[vi]}{p})')
            try:
                vals = [int(n) for n in nums.split(',')]
            except ValueError:
                raise StyleError(f'{label}: valores no enteros "{nums[:30]}" (estilo corrupto)')
            if len(vals) != STEPS:
                raise StyleError(f'{label}: {len(vals)} pasos')
            pats.append(vals)
        data.append(pats)
    return data


def to_style(name, data):
    lines = [f'name: {name}', '# decodificado con tools/make_style.py decode', '']
    for p in range(PATTERNS):
        rows = [(v, data[vi][p]) for vi, v in enumerate(VOICES) if any(data[vi][p])]
        if not rows:
            continue
        lines.append(f'[p{p}]')
        for v, vals in rows:
            cells = [SYMBOL.get(x, f'[{x}]') for x in vals]
            lines.append(f'{v:<9}' + ' '.join(''.join(cells[i:i + 4]) for i in range(0, STEPS, 4)))
        lines.append('')
    return '\n'.join(lines)


def main(argv):
    if len(argv) < 2 or argv[0] not in ('build', 'decode'):
        print(__doc__)
        return 2
    cmd, src = argv[0], argv[1]
    try:
        with open(src, encoding='utf-8') as f:
            text = f.read()
        if cmd == 'build':
            name, data = parse_style(text)
            if len(argv) > 2:
                dst = argv[2]
            elif name:
                dst = os.path.join(ROOT, 'drum_styles_v', name + '.txt')
            else:
                raise StyleError('falta "name:" en la fuente y no se indico archivo de salida')
            with open(dst, 'w', encoding='utf-8', newline='') as f:
                f.write(to_txt(data))
            print(f'ok -> {os.path.normpath(dst)}')
        else:
            name = os.path.splitext(os.path.basename(src))[0]
            style = to_style(name, from_txt(text))
            if len(argv) > 2:
                with open(argv[2], 'w', encoding='utf-8') as f:
                    f.write(style)
            else:
                print(style)
    except StyleError as e:
        print(f'error ({src}): {e}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
