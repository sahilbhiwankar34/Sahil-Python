import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.plot(df['month_number'], df['total_profit'])
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()

plt.plot(df['month_number'], df['facecream'])
plt.plot(df['month_number'], df['facewash'])
plt.plot(df['month_number'], df['toothpaste'])
plt.plot(df['month_number'], df['bathingsoap'])
plt.plot(df['month_number'], df['shampoo'])
plt.plot(df['month_number'], df['moisturizer'])
plt.legend(['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer'])
plt.show()

plt.bar(df['month_number'], df['facecream'])
plt.bar(df['month_number'], df['facewash'])
plt.show()

labels = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

plt.pie(sales, labels=labels, autopct='%1.1f%%')
plt.show()
