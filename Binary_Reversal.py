def reverse(num):
    f = 0
    sum = 0
    list11 = []
    num = int(num)
    while num>0:
        num = int(num)
        k = int(num%2)
        list11.append(int(k))
        num = int(num/2)
    if len(list11)%8 == 0:
        pass
    else:
       f =  len(list11)
       while True:
           f +=1
           if f%8 ==0:
               break
    diff = f - len(list11)
    while diff>0:
        list11.append(0)
        diff -= 1
    index = len(list11)-1
    for ele in list11:
        sum += ele * pow(2,index)
        index -= 1
    print(sum)

reverse(input())