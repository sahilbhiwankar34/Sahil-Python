states = []

# Input 5 states
for i in range(5):
    name = input("State name: ")
    area = float(input("Area: "))
    pop = int(input("Population: "))
    states.append([name, area, pop])

# Display all
print("\nAll States:")
for s in states:
    print(s)

# Largest area
largest_area = max(states, key=lambda x: x[1])
print("Largest Area State:", largest_area[0])

# Largest population
largest_pop = max(states, key=lambda x: x[2])
print("Largest Population State:", largest_pop[0])

# Population density
densities = []
for s in states:
    density = s[2] / s[1]
    densities.append((s[0], density))

# Highest density
highest_density = max(densities, key=lambda x: x[1])
print("Highest Density State:", highest_density[0])
