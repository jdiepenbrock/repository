"""Build the offline study tool and printable guide using only the standard library."""
from collections import Counter
from html import escape
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)


def load(name):
    return json.loads((ROOT / 'content' / name).read_text())


data = load('lessons.json')
questions = load('questions-practice.json') + load('questions-a.json') + load('questions-b.json')
data['questions'] = questions
topics = {t['id']: t for t in data['topics']}
assert set(topics) == {'sampling', 'mean-ci', 'proportion-ci', 'testing', 'two-sample', 'chi-square'}
assert len({q['id'] for q in questions}) == len(questions), 'Duplicate question IDs'
for q in questions:
    assert q['topic'] in topics, q['id']
    assert len(q['options']) == len(q['wrongReasons']) == 4, q['id']
    assert len(set(q['options'])) == 4, q['id']
    assert isinstance(q['answer'], int) and 0 <= q['answer'] < 4, q['id']
    assert q['kind'] in {'original', 'practice'}, q['id']
    assert q['difficulty'] in {'core', 'stretch'}, q['id']
    assert q['prompt'] and q['explanation'] and q['source'], q['id']
assert len({c['id'] for c in data['flashcards']}) == len(data['flashcards'])
assert all(c['topic'] in topics for c in data['flashcards'])
assert sorted(q['practiceNumber'] for q in questions if q['kind'] == 'practice') == list(range(1,31))
original_counts = Counter(q['topic'] for q in questions if q['kind'] == 'original')
required = {'sampling':3, 'mean-ci':3, 'proportion-ci':3, 'testing':4, 'two-sample':3, 'chi-square':4}
assert all(original_counts[t] >= n for t,n in required.items()), original_counts

template = (ROOT / 'study-tool.template.html').read_text()
marker = '/*__STUDY_DATA__*/'
assert template.count(marker) == 1, 'Missing or duplicate data marker'
serialized = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
(OUT / 'study-tool.html').write_text(template.replace(marker, 'window.STUDY_DATA = ' + serialized + ';'))

md = [
    '# Inference Lab — your Exam 2 study guide',
    'Based on all six supplied slide decks and the supplied 30-question practice exam. Worked practice answers are independently derived; no official answer key was supplied.',
    '## How to use this',
    'First try mixed practice without notes. For each miss, name the trap, study that lesson, and redo a similar question. Use flashcards to recall formulas before revealing them. Finish with a 20-question, 70-minute mock exam. A strong practice target is at least 17/20 on fresh mixed questions plus being able to explain each mistake; this is a study goal, not a guaranteed grade.',
    'The mock topic mix is a study choice, not a prediction. The supplied PDF calls the practice exam slightly easier than the real exam. Practice concepts and choices, not just the letters in the supplied key.',
    '## Choose the method before calculating',
    '| Situation | Method | First check |',
    '|---|---|---|',
    '| One numeric population mean, σ known | z mean interval/test | SE = σ/√n |',
    '| One numeric population mean, σ unknown | t interval/test | SE = s/√n; df = n−1 |',
    '| One binary population proportion | z proportion methods | CI SE uses p̂; null test SE uses p₀ |',
    '| Two independent numeric means, σ₁ and σ₂ known | Two-sample z | Add variances of means inside √ |',
    '| Two independent numeric means, unknown equal variances | Pooled two-sample t | Weight sample variances by nᵢ−1; df = n₁+n₂−2 |',
    '| Two independent numeric means, equal variances not assumed | Welch t | Separate variance terms; adjusted df |',
    '| Same people before/after or matched pairs | Paired t on differences | Count pairs; df = number of pairs−1 |',
    '| Two independent binary proportions | Two-proportion z | Equality test uses pooled p̂; CI uses unpooled SE |',
    '| One categorical variable against specified probabilities | χ² goodness of fit | E = n pᵢ; df = k−1 when probabilities fully specified |',
    '| Two categorical variables cross-classified | χ² independence | E = row×column/grand; df = (r−1)(c−1) |',
    '## Printed-reference practice',
    'The supplied exam provides two-sided z*: 90% = 1.645; 95% = 1.960; 99% = 2.576. At α = .05, right-tail χ² cutoffs: df 1: 3.841; 2: 5.991; 3: 7.815; 4: 9.488; 5: 11.070; 6: 12.592; 12: 21.026. Needed t-critical values are supplied within questions.',
    '## A repeatable MCQ routine',
    '1. Identify whether the outcome is numeric, binary, or categorical counts.',
    '2. Identify the parameter (μ, p, a difference, or association), number of groups, and whether observations are independent or paired.',
    '3. For a test, write Hₐ first to determine the tail. For a CI, identify the confidence level and correct multiplier.',
    '4. Write the SE before calculating. Most numerical traps replace √n with n, use SD instead of SE, or pool when they should not.',
    '5. For a test, compute (estimate − null value)/SE and compare p with the stated α. For a CI, use estimate ± critical × SE.',
    '6. Eliminate choices with the wrong units, center, tail, df, or Excel argument. Interpret the conclusion in context.',
    '7. Budget about 3.5 minutes per question on average. Bank time on concept questions, flag slow calculations, and return to them.',
    '## Suggested study blocks',
]
for step in data.get('plan', []):
    md += [f"### {step['title']} ({step['minutes']} minutes)", step['description']]
for topic in data['topics']:
    md += [f"## {topic['title']}", topic['summary']]
    for section in topic['sections']:
        md += [f"### {section['title']}", section['body']]
        for field,label in [('formula','Formula'),('example','Worked example'),('trap','MCQ trap'),('source','Source')]:
            if section.get(field): md.append(f"**{label}:** {section[field]}")
md += ['## Excel recognition: translate the words into an area',
       '| Task | Recognize this Excel pattern |', '|---|---|',
       '| Sample mean probability below a | NORM.DIST(a, μ, σ/SQRT(n), TRUE) |',
       '| Sample mean probability above a | 1 − NORM.DIST(a, μ, σ/SQRT(n), TRUE) |',
       '| Left-tail z p-value | NORM.S.DIST(z, TRUE) |',
       '| Right-tail z p-value | 1 − NORM.S.DIST(z, TRUE) |',
       '| Two-tail z p-value | 2*(1 − NORM.S.DIST(ABS(z), TRUE)) |',
       '| Left-tail t p-value | T.DIST(t, df, TRUE) |',
       '| Right-tail t p-value | 1 − T.DIST(t, df, TRUE) |',
       '| Two-tail t p-value | T.DIST.2T(ABS(t), df) |',
       '| Positive two-sided t critical value | T.INV.2T(α, df), equivalently T.INV(1−α/2, df) |',
       '| Positive two-sided z critical value | NORM.S.INV(1−α/2) |',
       '| χ² p-value | CHISQ.DIST.RT(statistic, df) |',
       '| χ² critical value | CHISQ.INV.RT(α, df) |',
       '| Paired / pooled / Welch two-sided t p-values | T.TEST(A, B, 2, type), type 1 / 2 / 3 respectively |',
       'TRUE (or 1) means cumulative area in NORM.DIST/T.DIST. INV functions turn a probability into a critical statistic; DIST functions turn a statistic into a probability. For directional tests based on T.TEST, check whether the observed difference points toward Hₐ before halving a two-sided p-value.',
       '## The five traps to know cold',
       '- SD describes individuals; SE describes statistics across samples. Divide SD by √n, not n.',
       '- Unknown σ means use t for usual inference about a mean, even when n ≥ 30; t approaches z as df grows.',
       '- More confidence means a wider interval. More data means a narrower interval, all else equal.',
       '- Hₐ determines the tail. A statistic pointing opposite a one-sided Hₐ produces a large p-value.',
       '- Chi-square checks EXPECTED counts. GOF and independence use different df formulas.',
       '## Corrections to the slides',
       (ROOT/'SOURCE_NOTES.md').read_text().split('## Corrections and interpretation notes',1)[1].strip(),
       '## Supplied practice exam — worked answer key',
       'Try the supplied questions first. These are independently worked answers, not an official instructor key. Numbers refer to your uploaded practice PDF.']
for q in questions:
    if q['kind']=='practice':
        md += [f"### Question {q['practiceNumber']}: {'ABCD'[q['answer']]} — {q['options'][q['answer']]}",q['explanation']]
markdown=''
for i, block in enumerate(md):
    separator = '' if i == 0 else '\n' if block.startswith('|') and md[i-1].startswith('|') else '\n\n'
    markdown += separator + block
markdown += '\n'
(OUT/'study-guide.md').write_text(markdown)

# A tiny controlled Markdown renderer: content is escaped; no external package needed.
def inline(s):
    import re
    return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',escape(s))

parts=[]
table=[]
def flush_table():
    if not table: return
    rows=[]
    for i,row in enumerate(table):
        cells=row.strip().strip('|').split('|')
        if i==1 and all(set(c.strip())<=set('-: ') for c in cells): continue
        tag='th' if i==0 else 'td'
        rows.append('<tr>'+''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in cells)+'</tr>')
    parts.append('<table>'+''.join(rows)+'</table>')
    table.clear()
for line in markdown.splitlines():
    if line.startswith('|'):
        table.append(line); continue
    flush_table()
    if not line.strip(): continue
    if line.startswith('#'):
        level=len(line)-len(line.lstrip('#'))
        parts.append(f'<h{level}>{inline(line[level:].strip())}</h{level}>')
    elif line.startswith('- '): parts.append('<p class="bullet">• '+inline(line[2:])+'</p>')
    else: parts.append('<p>'+inline(line)+'</p>')
flush_table()
guide='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inference Lab · Study Guide</title><style>
body{font:16px/1.55 system-ui,sans-serif;color:#202338;max-width:900px;margin:40px auto;padding:0 24px}h1{font-size:36px;line-height:1.1;color:#4338ca}h2{font-size:26px;margin-top:42px;border-bottom:2px solid #e0def4;padding-bottom:8px}h3{font-size:19px;margin-top:26px}p{white-space:pre-line}table{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}th,td{border:1px solid #d7d9e5;padding:10px;text-align:left;vertical-align:top}th{background:#f0efff}.print{padding:12px 18px;background:#4338ca;color:white;border:0;border-radius:8px;font:inherit;cursor:pointer}.bullet{padding-left:10px}@page{size:A4;margin:16mm}@media print{body{font-size:10pt;margin:0;padding:0;max-width:none}h1{font-size:26pt}h2{font-size:17pt;break-after:avoid}h3{font-size:12pt;break-after:avoid}th,td{font-size:9pt;padding:6px}tr{break-inside:avoid}.print{display:none}}
</style><button class="print" onclick="window.print()">Print / Save as PDF</button>'''+''.join(parts)+'</html>'
(OUT/'study-guide.html').write_text(guide)
with zipfile.ZipFile(OUT/'inference-lab.zip','w',zipfile.ZIP_DEFLATED) as archive:
    for file in ['study-tool.html','study-guide.html','study-guide.md']:
        archive.write(OUT/file,file)
    for file in ['SOURCE_NOTES.md','README.md']:
        archive.write(ROOT/file,file)
print(f'Built {len(questions)} questions ({len(questions)-30} original, 30 supplied), {len(data["flashcards"])} flashcards, {len(topics)} topics.')
print('Original coverage:',dict(original_counts))
print('Output:',OUT)
