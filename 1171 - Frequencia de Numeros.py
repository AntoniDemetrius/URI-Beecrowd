qte = int(input())
list = {}
for i in range(qte):
	v = int(input())
	if(v in list):
		list[v] += 1
	else:
		list[v] = 1


keys = list.keys()
keys = sorted(keys)

for k in keys:
	print("%d aparece %d vez(es)" %(k,list[k]))
