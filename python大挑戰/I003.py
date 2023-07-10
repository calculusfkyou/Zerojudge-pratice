temp=[]
while True:
    try:
        n=input()
        temp.append(n)
    except EOFError:
        break

new=[]
for i in range(len(temp)):
    if len(temp[i])>5:
        if temp[i][1:3]=="10" and temp[i][4:6]=="10":
            new.append([int(temp[i][1:3]),int(temp[i][4:6])])
        elif temp[i][1:3]=="10":
            new.append([int(temp[i][1:3]),int(temp[i][4])])
        elif temp[i][4:6]=="10":
            new.append([int(temp[i][1]),int(temp[i][4:6])])
    else:
        new.append([int(temp[i][1]),int(temp[i][3])])
field=[["-"for i in range(10)]for i in range(10)]
count=1
for i in range(len(new)):
    field[new[i][0]-1][new[i][1]-1]=count
    count+=1
for i in range(len(field)):
    print(*field[i])