nulist=[]
with open("AOA2.txt") as f:
    for line in f:
        #print(line)
        nulist.append(int(line))
for num1 in nulist:
    for num2 in nulist:
        for num3 in nulist:
         if num1+num2+num3==2020:
            print(num1*num2*num3)
