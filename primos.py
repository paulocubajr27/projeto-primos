import math

numerosPrimos = []

def ehPrimo(numero):
	contDiv=0
	for i in range(1,int(math.sqrt(numero))+1):
		if(numero%i==0):
			contDiv+=i
		if contDiv>1:
			break
	if(contDiv==1):
		return True
	else:
		return False
numero=2
contador=0

while True:
	if(ehPrimo(numero)):
		numerosPrimos.append(numero)
		contador+=1
	numero+=1
	if(contador>1000000):
		break

with open("arquivo.txt","w") as arquivo:
	for primo in numerosPrimos:
		arquivo.write(str(primo)+"\n")

