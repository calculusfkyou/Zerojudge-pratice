while True:
    try:
        t,x,y=map(int,input().split())
        count=0
        if t==1:
            count=x
        else:
            count+=1*(t-1)+x
        print(count)
    except EOFError:
        break