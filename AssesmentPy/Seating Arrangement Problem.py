'''1. Seating Arrangement Problem
You have N guests attending a dinner party. Each guest has exactly two preferred neighbors they'd
like to sit next to. Write a Python function that:
• Accepts the number of guests and their neighbor preferences.
• Determines a valid circular seating arrangement satisfying all preferences.
• If no arrangement is possible, clearly state that.
Input Example:
guests = {
 'Alice': ['Bob', 'Carol'],
 'Bob': ['Alice', 'David'],
 'Carol': ['Alice', 'David'],
 'D'''

from itertools import permutations

def valid(guests):
    names=list(guests.keys())

    for arrange in permutations(names):
        valid = True
        n = len(arrange)
        
        for i in range(n):
            left=arrange[(i-1)%n]
            right=arrange[(i+1)%n]
            guest=arrange[i]
            preferred=guests[guest]
            
            if not (left in preferred and right in preferred):
                valid = False
                break

        if valid:
            return list(arrange)  

    return "No valid arrangement possible."

guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

result = valid(guests)
print("Seating arrangement:", result)
