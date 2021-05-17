def solution(number):
	nb=bin(number).replace("0b", "")
	print(nb)
	nbs=str(nb)
	nbl=list(nbs)
	g=False
	m=0
	c=0
	for i in nbl:
		if i =="1":
			if m<c:
				m=c
			g=True
			c=0
		elif g:
			c+=1
	return m

solution(22)