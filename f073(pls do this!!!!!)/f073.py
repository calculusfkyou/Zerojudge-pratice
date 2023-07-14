while True:
    try:
        n=int(input())
        cards=list(input().split())
        k=int(input())
        temp,temp2=cards[:k],cards[k:]
        cards=temp2+temp
        print(*cards)
    except EOFError:
        break