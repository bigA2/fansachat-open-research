# Persona teams from real job data (no AI): O*NET task statements + task importance + technology skills.
# Builds a 10-person agency (Team tier) and a 50-person small business (Scale tier): boss, sector heads, workers,
# each with real tasks (highest importance first) and the software that occupation really uses, mapped to our
# 744-app catalog. O*NET data (c) National Center for O*NET Development, CC BY 4.0 - see README.
import csv, io, json, os, re, sys, urllib.request, zipfile
from collections import defaultdict

OUT = 'results'; os.makedirs(OUT, exist_ok=True)
def onet_zip():
    for v in ['30_1', '30_0', '29_3', '29_2', '29_1', '29_0']:
        try:
            print('trying O*NET', v, flush=True)
            return zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(f'https://www.onetcenter.org/dl_files/database/db_{v}_text.zip', timeout=120).read())), v
        except Exception as e: print(' ', e, flush=True)
    sys.exit('no O*NET download')
z, ver = onet_zip()
def table(name):
    f = next(n for n in z.namelist() if n.endswith('/' + name))
    return list(csv.DictReader(io.TextIOWrapper(z.open(f), 'utf-8'), delimiter='\t'))
titles = {r['O*NET-SOC Code']: r['Title'] for r in table('Occupation Data.txt')}
tasks = defaultdict(dict)
for r in table('Task Statements.txt'): tasks[r['O*NET-SOC Code']][r['Task ID']] = (r['Task'], r.get('Task Type', ''))
imp = {}
for r in table('Task Ratings.txt'):
    if r['Scale ID'] == 'IM': imp[r['Task ID']] = float(r['Data Value'])
tech = defaultdict(list)
for r in table('Technology Skills.txt'): tech[r['O*NET-SOC Code']].append((r['Example'], r.get('Hot Technology', 'N') == 'Y'))

CAT = json.load(open('data/catalog_apps.json', encoding='utf-8'))   # slug -> [name, aliases]
def to_catalog(example):
    e = example.lower()
    for slug, (name, als) in CAT.items():
        for a in [name.lower()] + als:
            if len(a) >= 4 and re.search(r'(^|[^a-z0-9])' + re.escape(a) + r'([^a-z0-9]|$)', e): return name
    return None

def role(soc, title=None, n_tasks=12):
    t = sorted(tasks.get(soc, {}).items(), key=lambda kv: -imp.get(kv[0], 0))
    sw = tech.get(soc, [])
    apps = sorted({a for a in (to_catalog(x) for x, _ in sw) if a})
    return {'soc': soc, 'occupation': titles.get(soc, '?'), 'title': title or titles.get(soc, '?'),
            'tasks': [{'task': x[0], 'type': x[1], 'importance': imp.get(k)} for k, x in t[:n_tasks]],
            'software_onet': [x for x, hot in sw if hot][:15] or [x for x, _ in sw][:15],
            'catalog_apps': apps[:20]}

FIRST = ['Amara', 'Bilal', 'Chen', 'Dalia', 'Elif', 'Farhan', 'Grace', 'Hiro', 'Isha', 'Jonas', 'Kofi', 'Lena', 'Mateo', 'Nadia', 'Omar',
         'Priya', 'Quinn', 'Rafael', 'Sana', 'Tomas', 'Uma', 'Victor', 'Wen', 'Ximena', 'Yusuf', 'Zara', 'Arjun', 'Bea', 'Carlos', 'Divya',
         'Emeka', 'Fatima', 'Gabriel', 'Hana', 'Ivan', 'Jia', 'Kemal', 'Lucia', 'Malik', 'Noor', 'Olu', 'Paula', 'Reza', 'Sofia', 'Tariq',
         'Vera', 'Wanjiru', 'Yara', 'Zubair', 'Anika']
LAST = ['Rahman', 'Okafor', 'Lindqvist', 'Moreau', 'Tanaka', 'Haddad', 'Novak', 'Mensah', 'Costa', 'Ibrahim', 'Kowalski', 'Santos', 'Ahmed',
        'Duarte', 'Nakamura', 'Osei', 'Petrov', 'Quiroga', 'Rossi', 'Sato', 'Turner', 'Usman', 'Varga', 'Wolfe', 'Yilmaz', 'Zhou', 'Bose',
        'Castillo', 'Dlamini', 'Eriksen', 'Farouk', 'Gupta', 'Hughes', 'Iyer', 'Jensen', 'Khan', 'Lopez', 'Mwangi', 'Nguyen', 'Ortiz',
        'Park', 'Qureshi', 'Reyes', 'Silva', 'Tran', 'Ueda', 'Vargas', 'Watanabe', 'Xu', 'Young']
names = iter(f'{FIRST[i % len(FIRST)]} {LAST[(i * 7 + i // len(FIRST)) % len(LAST)]}' for i in range(500))   # 60+ unique, fictional

def team(company, kind, tier, boss, sectors):
    org = {'company': company, 'kind': kind, 'tier': tier, 'boss': {'name': next(names), **role(*boss)}, 'sectors': []}
    for sector, head, workers in sectors:
        s = {'sector': sector, 'head': {'name': next(names), **role(*head)}, 'workers': []}
        for soc, title, count in workers:
            for _ in range(count): s['workers'].append({'name': next(names), **role(soc, title, 8)})
        org['sectors'].append(s)
    org['headcount'] = 1 + sum(1 + len(s['workers']) for s in org['sectors'])
    return org

# Team tier: a 10-person design + web agency
TEAM = team('Northlane Studio', 'creative agency (design, web, social)', 'Team $149', ('11-1021.00', 'Founder & Managing Director'), [
    ('Design', ('27-1011.00', 'Creative Director'), [('27-1024.00', 'Graphic Designer', 2), ('15-1255.00', 'Web & Digital Designer', 1)]),
    ('Client services', ('11-2021.00', 'Account Director'), [('13-1199.04', 'Project Coordinator', 1), ('27-3031.00', 'Social Media Specialist', 1), ('27-3043.00', 'Copywriter', 1)]),
    ('Operations', ('43-3031.00', 'Bookkeeper'), [])])
# Scale tier: a 50-person growing small business (e-commerce home goods brand with in-house studio)
SCALE = team('Brightpath Home Co.', 'growing small business (e-commerce brand)', 'Scale $299', ('11-1011.00', 'CEO'), [
    ('Marketing', ('11-2021.00', 'Head of Marketing'), [('13-1161.01', 'SEO & Search Marketer', 2), ('13-1161.00', 'Market Research Analyst', 1),
        ('27-3031.00', 'Social Media Manager', 3), ('27-3043.00', 'Content Writer', 3), ('13-1161.00', 'Email Marketing Specialist', 1)]),
    ('Design', ('27-1011.00', 'Head of Design'), [('27-1024.00', 'Graphic Designer', 4), ('27-4032.00', 'Video Editor', 2), ('15-1255.00', 'Web Designer', 1), ('27-4021.00', 'Product Photographer', 1)]),
    ('Sales', ('11-2022.00', 'Head of Sales'), [('41-4012.00', 'B2B Sales Rep', 4), ('41-3091.00', 'Sales Development Rep', 1), ('41-3091.00', 'Wholesale Account Manager', 2)]),
    ('Customer support', ('43-1011.00', 'Head of Support'), [('43-4051.00', 'Customer Service Rep', 7)]),
    ('Operations', ('11-1021.00', 'Head of Operations'), [('13-1081.00', 'Logistics Coordinator', 2), ('43-5071.00', 'Warehouse & Shipping Clerk', 2),
        ('11-3071.04', 'Supply Chain Manager', 1), ('13-1023.00', 'Purchasing Agent', 1)]),
    ('Finance & people', ('11-3031.00', 'Head of Finance'), [('13-2011.00', 'Accountant', 1), ('43-3031.00', 'Bookkeeper', 1),
        ('13-1071.00', 'HR Specialist', 1), ('43-3051.00', 'Payroll Clerk', 1), ('15-1211.00', 'Systems & Analytics Analyst', 1)])])
assert SCALE['headcount'] == 50, SCALE['headcount']
assert TEAM['headcount'] == 10, TEAM['headcount']
json.dump({'onet_version': ver, 'team_tier': TEAM, 'scale_tier': SCALE}, open(f'{OUT}/teams.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

def md(org):
    L = [f"## {org['company']} ({org['kind']}) - {org['tier']}, {org['headcount']} people", '',
         f"**Boss: {org['boss']['name']}, {org['boss']['title']}** (O*NET: {org['boss']['occupation']})"]
    L += [f"- {t['task']}" for t in org['boss']['tasks'][:6]]
    for s in org['sectors']:
        h = s['head']; L += ['', f"### {s['sector']} - head: {h['name']}, {h['title']}", f"Apps they use (in our catalog): {', '.join(h['catalog_apps']) or '-'}"]
        L += [f"- {t['task']}" for t in h['tasks'][:6]]
        seen = set()
        for w in s['workers']:
            L.append(f"- **{w['name']}**, {w['title']}")
            if w['title'] in seen: continue
            seen.add(w['title'])
            L += [f"  - {t['task']}" for t in w['tasks'][:5]] + [f"  - apps: {', '.join(w['catalog_apps']) or '-'}"]
    return '\n'.join(L)
open(f'{OUT}/TEAMS.md', 'w', encoding='utf-8').write(
    f"# Persona teams for Team and Scale testing (O*NET {ver.replace('_', '.')}, real tasks + real software)\n\n"
    "Data: O*NET database, National Center for O*NET Development, CC BY 4.0. People and company names are fictional.\n\n"
    + md(TEAM) + '\n\n' + md(SCALE) + '\n')
print('teams ok', TEAM['headcount'], SCALE['headcount'])
