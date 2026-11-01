# Laya (no LLM tokens, CPU): for every real task of every persona, how likely an app-to-app automation can do or
# help it. Output: results/AUTOMATION.md (best automation candidates per person) + results/automation.json.
import json
import laya

T = json.load(open('results/teams.json', encoding='utf-8'))
Q = {'automatable': 'Could software apps connected by an automation workflow do this task or most of it without a person?',
     'repetitive': 'Is this a repeated routine task (daily or weekly) rather than a one-off judgement call?'}
m = laya.load('convaiinnovations/laya', device='cpu')
cache, rows = {}, []
def people(org):
    yield 'Boss', org['boss']
    for s in org['sectors']:
        yield s['sector'] + ' head', s['head']
        for w in s['workers']: yield s['sector'], w
for tier in ('team_tier', 'scale_tier'):
    org = T[tier]
    for where, p in people(org):
        for t in p['tasks']:
            k = t['task']
            if k not in cache:
                a = m.predict(k, {q: {'type': 'noul', 'instructions': s} for q, s in Q.items()})['answers']
                cache[k] = {q: round(a[q]['noul'], 3) for q in Q}
            rows.append({'tier': tier, 'company': org['company'], 'where': where, 'person': p['name'], 'title': p['title'],
                         'task': k, **cache[k], 'apps': p['catalog_apps']})
for p in T.get('solo', []):
    for t in p['tasks']:
        k = t['task']
        if k not in cache:
            a = m.predict(k, {q: {'type': 'noul', 'instructions': s} for q, s in Q.items()})['answers']
            cache[k] = {q: round(a[q]['noul'], 3) for q in Q}
        rows.append({'tier': 'solo', 'company': p['plan'], 'where': p['plan'], 'person': p['name'], 'title': p['title'],
                     'task': k, **cache[k], 'apps': p['catalog_apps']})
json.dump(rows, open('results/automation.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
L = ['# Which real tasks FansaChat can automate (Laya yes/no scores, 0-1)', '',
     'automatable = could connected apps do it; repetitive = routine. Ranked by automatable x repetitive. Not a promise: a test list.', '']
T['solo'] = {'company': 'Starter and Pro people', 'tier': 'Starter / Pro'}
for tier in ('solo', 'team_tier', 'scale_tier'):
    L += [f"## {T[tier]['company']} ({T[tier]['tier']})", '', '| person | role | task | auto | routine | apps |', '|---|---|---|---|---|---|']
    best = sorted((r for r in rows if r['tier'] == tier), key=lambda r: -(r['automatable'] * r['repetitive']))
    seen = set()
    for r in best:
        if (r['title'], r['task']) in seen: continue
        seen.add((r['title'], r['task']))
        L.append(f"| {r['person']} | {r['title']} | {r['task']} | {r['automatable']} | {r['repetitive']} | {', '.join(r['apps'][:5])} |")
        if len(seen) >= 60: break
    L.append('')
open('results/AUTOMATION.md', 'w', encoding='utf-8').write('\n'.join(L))
print('scored', len(cache), 'unique tasks')
