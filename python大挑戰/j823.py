while True:
    try:
        n=input()
        if n=="stop":
            break
        else:
            if n.isalpha():
                print("print(\""+n+"\")")
            else:
                print("print("+n+")")
    except EOFError:
        break