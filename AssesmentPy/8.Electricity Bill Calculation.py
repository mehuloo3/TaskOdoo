'''An electricity provider charges consumers based on slabs of electricity usage:
Usage (kWh) Price per unit ( ) ₹
0-100 5
101-300 7
301-500 10
Above 500 15
Write a Python program that:
• Accepts electricity usage (in kWh) from the user.
• Clearly calculates and displays the bill, explaining the charges for each slab separately'''

use = int(input("Enter the Amount (in kWh): "))
total = 0
if use > 0:
    usable = min(use, 100)
    cost = 5 * usable
    total += cost
    print(f"0-100 units @ 5/unit = {cost} ₹")

if use > 100:
    usable = min(use - 100, 200)
    cost = 7 * usable
    total += cost
    print(f"101-300 units @ 7/unit = {cost} ₹")
    
if use > 300:
    usable = min(use - 300, 200)
    cost = 10 * usable
    total += cost
    print(f"301-500 units @ 10/unit = {cost} ₹")

if use > 500:
    usable = use - 500
    cost = 15 * usable
    total += cost
    print(f"Above 500 units @ 15/unit = {cost} ₹")

print(f"\nTotal Bill: {total} ₹")