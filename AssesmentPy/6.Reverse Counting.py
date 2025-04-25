''''
Write a Python program that prints numbers from 1000 down to 1 without using any loops (for,
while) or the any built-in functions like range()
'''

def rec(n):
    if n>0:
        print(n)
        rec(n-1)
        
value=int(input("Enter the value: "))
if value<=0:
    print("Invalid")
else:
    print(rec(value))