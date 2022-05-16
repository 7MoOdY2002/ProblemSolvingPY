rows,colloms = map(int, input().split())
k = 1
for value in range(1, rows+1):
    if value % 2 == 1:
        print("#"*colloms)
        continue
    elif value % 2 == 0:
        if k % 2 == 1:
            print("."*(colloms-1)+"#")
            k+=1
            continue
        else:
            print( "#"+"." * (colloms - 1) )
            k+=1
            continue

