a=input("Enter 1st sentence = ")
b=input("Enter 2nd sentence = ")
a=a.split(" ")
b=b.split(" ")
c=1
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            
            print("common word ",c," : ",a[i])
            c+=1