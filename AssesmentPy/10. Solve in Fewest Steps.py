'''10. Solve in Fewest Steps
Given a string consisting of letters and digits, write a Python program to separate and sort letters
and digits individually and then concatenate them, letters first and digits after, with each group
sorted individually.
Your solution should be concise yet clear.
Example:
• Input: "B4A1D3"
• Output: "ABD134" '''

def Fewest(A):
    digits=""
    st=""
    for i in A:
       #if digit
      if i.isdigit():
         digits+=i
      else:
       # if string
         st+=i
    #both sort
    d=sorted(digits)
    e=sorted(st)
    # temporory var
    x=""
    for i in e:
       x+=i
    for i in d:
       x+=i
    return x

A=input(str("enter the string: "))
print(Fewest(A))