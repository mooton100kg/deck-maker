from medlist import MED_LIST1 as MED_LIST
from itertools import combinations
from random import sample

#MED_LIST = dict(list(MED_LIST.items())[:5])
runnum = 1
okset = 1
totalrun = len(set(combinations(MED_LIST.keys(),6)))
meduse = set()
typeuse = set()
indiuse = set()
adruse = set()
medlist = []
allcard = list()

for i in sample(list(combinations(MED_LIST.keys(), 6)),totalrun):
	medset = set(list(i))
	typeset = set()
	indiset = set()
	adrset = set()
	for j in i:
		typeset.update([MED_LIST[j][0]])
		indiset.update(MED_LIST[j][1])
		adrset.update(MED_LIST[j][2])
	if len(medset) + len(typeset) + len(indiset) + len(adrset) == 29:
		meduse = meduse.union(medset)
		medlist.append(list(medset))
		typeuse = typeuse.union(typeset)
		indiuse = indiuse.union(indiset)
		adruse = adruse.union(adrset)
		print(f'{runnum}/{totalrun} {okset}: {medset}')
		print(f'med: {len(meduse)}, type: {len(typeuse)}, indi: {len(indiuse)}, adr: {len(adruse)}')
		allcard.append([medset,typeset,indiset,adrset])
		okset += 1
	if okset == 20 and len(indiuse) == 31 and len(meduse) == 46 and len(adruse) == 35:
		break
	if okset == 20:
		break
	#print(len(medset)+len(otherset))
	runnum += 1


with open('allcard.txt','w') as f:
   f.write(str(allcard))
