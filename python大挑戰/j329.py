while True:
    try:
        a=input()
        b=input()
        c=input()
        if c=="yes":
            print(a+"想和"+b+"絕交")
        else:
            print(a+"不想和"+b+"絕交")
    except EOFError:
        break