while True:
    try:
        n=list(input().split())
        s=list(map(int,input().split()))
        temp=[]
        for i in range(len(n)):
            temp.append([n[i],s[i]])
        temp.sort(key=lambda temp:temp[1])
        for i in range(len(temp)-1):
            print(temp[i][0],end=" ")
        print(temp[-1][0])
    except EOFError:
        break