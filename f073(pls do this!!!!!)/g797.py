while True:
    try:
        n,m=map(int,input().split())
        cards=list(input().split())
        c1=cards[:(n//2)]
        c2=cards[(n//2):]
        cards.clear()
        for j in range(m):
            for i in range(len(c1)):
                cards.append(c1[i])
                cards.append(c2[i])
            c1=cards[:(n//2)]
            c2=cards[(n//2):]
            if j!=(m-1):
                cards.clear()
        print(*cards)
    except EOFError:
        break