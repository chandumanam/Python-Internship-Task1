# Average Temperature Calculator

print("Average Temperature Calculator")

n = int(input("How many temperature values do you want to enter? "))
temps = []

for i in range(n):
    temp = float(input(f"Enter temperature {i + 1}: "))
    temps.append(temp)

average = sum(temps) / n
print(f"\nAverage temperature from {n} readings is: {average:.2f}°")
