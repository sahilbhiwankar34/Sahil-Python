import pandas as pd

# Load CSV
df = pd.read_csv("books.csv")

print("\nAll Books:")
print(df)

# Books by author
author = input("Enter author name: ")
print(df[df['author'] == author])

# Books by publisher
pub = input("Enter publisher: ")
print(df[df['publisher'] == pub])

# Cheapest and costliest
print("\nCheapest Book:")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:")
print(df.loc[df['price'].idxmax()])

# Sort by year
print("\nSorted by Year:")
print(df.sort_values(by='year'))
