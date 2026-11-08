"""Rebuild rules.md from index.html.

Run from anywhere:  python3 make_standard_digest.py
Standard library only. The HTML is the source of truth; this file just re-derives the digest.
"""
import collections
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'index.html'
OUT = HERE / 'rules.md'


def clean(x):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x))).strip()


s = SRC.read_text(encoding='utf-8')
secs = [(m.start(), m.group(1)) for m in re.finditer(r'<section id="([^"]+)">', s)]
titles = {}
for pos, sid in secs:
    h = re.search(r'<h2>(.*?)</h2>', s[pos:pos + 600], re.S)
    titles[sid] = clean(h.group(1)) if h else sid


def sec_of(pos):
    cur = None
    for p, sid in secs:
        if p <= pos:
            cur = sid
    return cur


rules = [(m.start(), m.group(1), m.group(2), clean(m.group(3))) for m in re.finditer(
    r'<div class="rule" id="([^"]+)"><div class="rulehead">.*?<span class="level">(\w+)</span></div><p>(.*?)</p></div>', s, re.S)]
c = collections.Counter(r[2] for r in rules)

out = ['# Rule reference\n',
       'Every rule in the Dashboard Design Standard (version 1.0.0), by section, plus the color palette. '
       'The full standard, with the reasoning and every example, is [index.html](index.html). '
       'This page is generated from it by `make_rules.py`, so the two always match.\n',
       '## Rule levels\n',
       '- **MUST**: release gate. Fix any failure before shipping, or record why the rule does not apply.',
       '- **SHOULD**: expected practice. Record a reason, tradeoff and mitigation for each departure. The reviewer agrees before release.',
       '- **GUIDANCE**: a suggested technique.\n',
       '**How levels are assigned.** MUST when breaking it can mislead a reader, hide a signal the decision needs, block access, or skip a release control. '
       'SHOULD when it is a strong default with legitimate exceptions, or a MUST rule elsewhere already enforces its core. GUIDANCE for judgment calls. '
       'Use the same test for any new rule.\n',
       '**Counts:** %d rules — %d MUST, %d SHOULD, %d GUIDANCE.\n' % (len(rules), c['MUST'], c['SHOULD'], c['GUIDANCE']),
       '## All rules\n']
cur = None
for pos, rid, lvl, txt in rules:
    sid = sec_of(pos)
    if sid != cur:
        out += ['\n### %s\n' % titles[sid], '| ID | Level | Rule |', '|---|---|---|']
        cur = sid
    out.append('| %s | %s | %s |' % (rid, lvl, txt.replace('|', '/')))

i = s.find('Palette and approved pairings')
j = s.find('</table>', i)
out += ['\n## Palette (light)\n', '| Role | Hex | Approved use and contrast |', '|---|---|---|']
for r in re.findall(r'<tr>(.*?)</tr>', s[i:j], re.S):
    cells = [clean(x) for x in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.S)]
    if len(cells) == 3 and '#' in cells[1]:
        out.append('| %s | `%s` | %s |' % (cells[0], re.search(r'#[0-9A-Fa-f]{6}', cells[1]).group(0), cells[2]))

OUT.write_text('\n'.join(out) + '\n', encoding='utf-8')
print('wrote %s: %d rules (%s)' % (OUT.name, len(rules), dict(c)))
