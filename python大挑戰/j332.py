while True:
    try:
        n=list(map(int,input().split()))
        s=int(input())
        c=n.count(s)
        print(c)
        print(c*s)
    except EOFError:
        break