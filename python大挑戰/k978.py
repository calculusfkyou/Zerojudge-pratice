while True:
    try:
        t=int(input())
        l=list(input().split())
        n=int(input())
        count=0
        temp=[]
        maxlen=len(l[0])
        for i in range(len(l)):
            if len(l[i])>maxlen:
                maxlen=len(l[i])
        for i in range(len(l)):
            if len(l[0])!=maxlen:
                count+=1
                temp.append(l[0])
                l.pop(0)
            else:
                l.append(l[0])
                l.pop(0)
        l.sort(key=lambda l:l[n-1])
        if count==0:
            print(*l)
        elif count==1:
            print(temp[0],end=" ")
            print(*l)
        else:
            print(*l,end=" ")
            temp.sort(reverse=1)
            temp.sort(key=lambda temp:temp[-1],reverse=1)
            print(*temp)
    except EOFError:
        break