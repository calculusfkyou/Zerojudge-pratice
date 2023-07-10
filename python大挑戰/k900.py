while True: 
    try:
        h,x,y=map(int,input().split())
        count=0
        while h>0:
            h-=x
            count+=1
            if h<=0:
                break
            h+=y
        print(count)
    except EOFError:
        break