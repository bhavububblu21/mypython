# sum untill negative number
total = 0

while True:
    num = int(input("Enter a number "))
    if num < 0:
        break
    total += num

print("The sum of all entered positive numbers is:", total)
