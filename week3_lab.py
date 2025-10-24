"""
This file contains the code for the Week 3 lab exercises,
focusing on for loops, while loops, and GitHub integration.
"""

for i in range(0, 20, 2):
    # prints the numbers between 1 and 20 each on their own line
    print(i+2)


costs = [15.00, 12.50, 3.75, 40.25, 6.99]
total_cost = 0
for cost in costs:
    total_cost += cost

print(f"{total_cost:.2f}")