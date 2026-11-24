import json, pathlib, random
p=pathlib.Path(__file__).parent
lines=p.joinpath('bank.txt').read_text().splitlines(); courses=[]
for i in range(0,len(lines),2):
    group,name,kind=lines[i].split('|'); pairs=[x.split('=',1) for x in lines[i+1].split(';')]; assert len(pairs)==14,(name,len(pairs))
    qs=[]
    for j,(term,meaning) in enumerate(pairs):
        rng=random.Random(i*100+j); others=rng.sample([x for x in pairs if x[0]!=term],3)
        for v,(prompt,answer,wrong) in enumerate([
            (f'Which concept matches this description? {meaning}.',term,[x[0] for x in others]),
            (f'Which description best explains {term}?',meaning,[x[1] for x in others]),
            (f'A student pairs {term} with a definition. Which pairing is accurate?',f'{term}: {meaning}',[f'{term}: {x[1]}' for x in others]),
            (f'Which term would you use to label the following idea in your notes: {meaning}?',term,[x[0] for x in reversed(others)])
        ]):
            choices=[answer]+wrong; rng.shuffle(choices); qs.append(dict(id=f'{i//2}-{j}-{v}',topic=term,prompt=prompt,choices=choices,answer=choices.index(answer),explanation=f'{term} refers to {meaning}.'))
    courses.append(dict(id=i//2,group=group,name='AP '+name,portfolio=kind=='P',questions=qs))
assert len(courses)==42
p.joinpath('data.js').write_text('window.COURSES = '+json.dumps(courses,ensure_ascii=False,separators=(',',':'))+';\n')
print(len(courses),sum(len(c['questions']) for c in courses))