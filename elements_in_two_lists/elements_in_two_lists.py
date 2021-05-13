File1 = input()
File2 = input()
#  print(File1,File2)
Fp1=open(File1,'r',encoding='utf-8')
Fp2=open(File2,'r',encoding='utf-8')
T1=[]
T2=[]
while True:
    temp=Fp1.readline()
    if not temp:
        break
    else:
        T1.append(temp.strip('\n'))

while True:
    temp=Fp2.readline()
    if not temp:
        break
    else:
        T2.append(temp.strip('\n'))
#  print(T1,T2)
Fp2.close()
Fp1.close()

All=[]
Only1=[]
Only2=[]
for i in T1:
    if i in T2:
        All.append(i)
    else:
        Only1.append(i)
for i in T2:
    if i not in All:
        Only2.append(i)
print("In both files:",All,"count",len(All))
print("Only in the first file:", Only1,"count",len(Only1))
print("Only in the second file:", Only2,"count",len(Only2))