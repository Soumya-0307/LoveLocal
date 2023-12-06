def findmajority(arr,n):
    flag=0
    for i in range(n):
        count=0
        for j in range(i,n):
            if (arr[i] == arr[j]):
                count+=1

        if (count > int(n/3)):
            print(arr[i],end=" ")
            flag=1

    if (flag == 0):
        print("[ ]")


lists=[2,1]
n=len(lists)

# while True:
#     lists.append(int(input()))

findmajority(lists,n)


