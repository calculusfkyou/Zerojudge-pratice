while True:
    try:
        n=input()
        print("Doraemon:\"Hi,%s!\""%(n))
    except EOFError:
        break