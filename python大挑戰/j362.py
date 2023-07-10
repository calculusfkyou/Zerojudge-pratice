while True:
    try:
        n=int(input())
        s=input()
        count=0
        check=0
        if s=="print":
            for i in range(1,n+1):
                if n%i==0:
                    print(i)
                    count+=i
                    check+=1
            print("%d的因數的個數是%d，%d的因數的總和是%d"%(n,check,n,count))
        else:
            for i in range(2,n):
                if n%i==0:
                    print(i)
                    count+=i
                    check+=1
            print("%d的因數的個數是%d，%d的因數的總和是%d"%(n,check,n,count))
    except EOFError:
        break