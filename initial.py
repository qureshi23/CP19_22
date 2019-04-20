def pattern(value01,value02,value03):
  i=1
  while(i<=length):
    j=length
    while(j>=i):
      print(" ",end=' ')
      j-=1
    k=1
    while(k<i*2):
      if(k==i or i==length):
        print(second_last,end=' ')
      else:
        print(last,end=' ')
      k+=1
    i+=1
    print("")
    
  i=length-1
  while(i>=1):
    j=length
    while(j>=i):
      print(" ",end=' ')
      j-=1
    k=1
    while(k<i*2):
      if(k==i):
        print(second_last,end=' ')
      else:
        print(last,end=' ')
      k+=1
    i-=1
    print("")
length=int(input("Enter shape length : "))
second_last=int(input("Enter your id 2nd last number : "))
last=int(input("Enter your id last number : "))
pattern(value01,value02,value03)