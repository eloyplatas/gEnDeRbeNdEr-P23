#!/usr/bin/env python3
"""Genera drum_styles_v_genres.txt: una linea "Familia<TAB>archivo.txt" por estilo.

  python3 tools/make_genres.py

Las familias salen de la tabla "Included styles" del README (como docs/fingerprints.html).
GenderBender P23 lee este archivo (en Data/) para su selector de genero.
"""
import glob
import os

from make_style import ROOT
from view_styles import families

OUT = os.path.join(ROOT, 'drum_styles_v_genres.txt')
# familias pequenas de la tabla original que en el selector van con su familia grande
MERGE = {'House': 'House & disco', 'Drum & bass': 'Breaks, jungle & drum & bass'}


def render():
    names = sorted(os.path.basename(p)[:-4] for p in glob.glob(os.path.join(ROOT, 'drum_styles_v', '*.txt')))
    lines, used = [], set()
    order = []
    for family, entries in families():
        for base, bpm in entries:
            for n in names:
                if n not in used and (n == base or (bpm and n == f'{base} {bpm}')):
                    used.add(n)
                    fam = MERGE.get(family, family)
                    if n.startswith(('DUBSTEP ', 'BROSTEP ')):
                        fam = 'Dubstep'
                    lines.append((fam, n))
        fam = MERGE.get(family, family)
        if fam not in order:
            order.append(fam)
    for n in names:
        if n not in used:
            lines.append(('Other', n))
    # agrupado por familia, en el orden del README
    out = []
    for fam in order + (['Other'] if 'Other' not in order else []):
        out += [f'{f}\t{n}.txt' for f, n in lines if f == fam]
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(render())
    print('ok ->', os.path.relpath(OUT, ROOT))
