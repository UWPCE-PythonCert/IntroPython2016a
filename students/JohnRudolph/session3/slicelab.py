s1 = list(range(1,20))

#1
def exchange(lst):
	fst = lst[-1]
	mid = list(lst[1:-1])
	fin = lst[0]
	print(fst, mid, fin)

print(exchange(s1))
#2
def everyother(lst):
	for n in lst:
		if n % 2 == 0:
			print(n)

print(everyother(s1))
#3
def everyother4(lst):
	lst2 = lst[3:-4]
	for n in lst2:
		if n % 2 == 0:
			print(n)

print(everyother4(s1))

print(s1[::2])

#4
print(s1[::-1])

#5
def thirds(lst):
	countlst = len(lst)
	fst = lst[0:int(countlst/3)]
	mid = lst[int((countlst/3)):int((2*countlst/3))]
	fin = lst[-int(2*countlst/3):-int(countlst/3)]
	print(fin,mid,fst)
	

print(thirds(s1))


