def cong(n1, n2):
	if(len(n1)>len(n2)):
		for i in range(len(n1)-len(n2)):
			n2.insert(0,"0")
	else:
		for i in range(len(n2)-len(n1)):
			n1.insert(0,"0")
	new_num=list()
	for i in range(len(n1)-1, -1, -1):
		if int(n1[i])+int(n2[i])>=10:
			new_num.insert(0,str(int(n1[i])+int(n2[i])-10))
			n1[i-1]={"1": "2", "2":"3", "3":"4", "4":"5", "5":"6", "6": "7", "7":"8", "8":"9", "9": "10","0":"1"}[n1[i-1]]
			if i==0:
				new_num.insert(0, "1")
		else:
			new_num.insert(0,str(int(n1[i])+int(n2[i])))
	return new_num

def fibonancii(n):
	a1=["0"]
	a2=["1"]
	a3=[]
	for i in range(n):
		a3=cong(a1, a2)
		a1=a2
		a2=a3
	return a3
for n in range(300+1):
	print("Số fibo thứ {0}: ".format(n),''.join(fibonancii(n)))

# print(''.join(fibonancii(1000)))
