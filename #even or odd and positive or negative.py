even or odd and positive or negative
num=int(input("enter the number"))
if num >0:
  if num%2==0:
    print(" number is even and positive")
  else:
    print("number is odd and positive")
elif num<0:
  if num%2==0:
    print("number is even and negative")
  else:
    print("number is odd and negative")
else:
  print("not even or odd and positive or negative")
