while True:
    try:
        nums=list(map(int,input().split()))
        print(sum(nums))
    except EOFError:
        break