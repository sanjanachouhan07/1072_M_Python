# Program to print right angle triangle using while loop

# number of rows
n = int(input("Enter number of rows: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")   # print star
        j += 1
    print()   # new line after each row
    i += 1
