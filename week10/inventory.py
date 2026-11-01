print("--- Exercise 1: Build a List ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # always grabs the first item in a list
print(inventory[-1]) # always grabs the last item in a list

middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs items at index 1, 2, and 3
print(inventory[-2])
print(inventory[::2]) # grabs every other item in the list

print("--- Exercise 4: List Methods ---")
inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print (f"Total sales:{total}")
print (f"Number of sales: {count}")
print (f"Average sale: {average}")
print (f"Best sale:{max(sales)}")
print (f"Worst sale:{min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print (f"Best sale (loop):{best}")
print (f"Worst sale (loop):{worst}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [0.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print (f"Average: {sum(high_sales)/len(high_sales):.2f}")

# SELF REFLECTION
# 1. What surprised me most is that lists are mutable, so methods like .sort()
# and .append() change the original list in place instead of making a new one.
# I expected sort() to hand back a sorted copy, but it actually returns None,
# so writing sorted_list = my_list.sort() would wipe out my data. Negative
# indexing and slicing were also different from what I expected, since the
# end of a slice is not included.
# 2. In a finance class, I could use a list to hold the daily closing prices
# for a stock and calculate returns, averages, or the best and worst days in
# a few lines. In Excel I would have to copy formulas down a column and fix
# the ranges every time the data changed. With a list, I can filter for days
# above a threshold or apply a change to every price with one loop, and rerun
# it on new data instantly.