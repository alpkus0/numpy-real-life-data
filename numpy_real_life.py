"""
🎯 Objective:
In this assignment, you will generate, analyze and visualize some real-life data with NumPy.
"""

import numpy as np
import matplotlib.pyplot as plt


print("📊 PART 1: Company Salary Analysis\n")


# Seed for fixing randomness
np.random.seed(42)

# Generate salaries for 500 employees randomly between 3000 $ and 15000 $
salary = np.random.randint(3000, 15001, 500)

# Calculate the average, maximum, and minimum salary
avg_salary = np.mean(salary)
max_salary = np.max(salary)
min_salary = np.min(salary)

# Print the results
print("*** ENJA COMPANY SALARY ***"
      f"\nAverage Salary = {avg_salary} $"
      f"\nMax Salary = {max_salary} $"
      f"\nMin Salary = {min_salary} $\n")

# Visualize the salary distribution with a histogram
plt.figure(figsize=(10, 6))
plt.hist(salary, bins=10, edgecolor="black", alpha=0.8)
plt.xlabel("Salary ($)", fontweight="bold")
plt.ylabel("Number of Employees\n", fontweight="bold")
plt.title("Enja Company Salary\n", fontweight="bold")
plt.grid(axis="y")
plt.show()

# Assign 500 employees to 3 different departments randomly
# 1 = Engineering, 2 = Accounting, 3 = Marketing
dept = np.random.choice([1, 2, 3], 500)
dept_names = ["Engineering", "Accounting", "Marketing"]
print("\n*** ENJA'S COMPANY DEPARTMENT AVERAGE SALARY ***")


# Function to calculate the average salary by department
def mean_salary(dept_id):
    dept_salaries = salary[dept == dept_id]
    return np.mean(dept_salaries)


# Calculate average salary for each department
avg_salary_engineering = mean_salary(1)
avg_salary_accounting = mean_salary(2)
avg_salary_marketing = mean_salary(3)

# Print the results for each department
print(f"Average Engineering Salary = {avg_salary_engineering:.2f} $"
      f"\nAverage Accounting Salary = {avg_salary_accounting:.2f} $"
      f"\nAverage Marketing Salary = {avg_salary_marketing:.2f} $")

# We visualize the average salary for each department with a bar chart
plt.figure(figsize=(10, 6))
dept_avg_salary = [avg_salary_engineering, avg_salary_accounting, avg_salary_marketing]
plt.title("Average Salary by Department at Enja Company\n", fontweight="bold")
plt.xlabel("\nDepartments", fontweight="bold")
plt.ylabel("Average Salary ($)\n", fontweight="bold")
plt.bar(dept_names, dept_avg_salary, color="r", edgecolor="black")
plt.grid(axis="y")
plt.show()


print("\n📈 PART 2: Generating and Analyzing Weather Data")

# Generate random temperature data for 365 days ranging from -10°C to 40°C
temperature_data = np.random.uniform(-10, 40, 365)

# Calculate the average, minimum, and maximum temperature
avg_temperature = np.mean(temperature_data)
min_temperature = np.min(temperature_data)
max_temperature = np.max(temperature_data)

# Print the results: average, minimum, and maximum temperature
print(f"\n*** Yearly Temperature Data (365 Days) ***"
      f"\nAverage Temperature = {avg_temperature:.2f}°C"
      f"\nMinimum Temperature = {min_temperature:.2f}°C"
      f"\nMaximum Temperature = {max_temperature:.2f}°C")

# Create a plot to visualize the temperature fluctuations over the year
plt.figure(figsize=(10, 6))
plt.plot(temperature_data, color="b", marker="o", markersize=5, markerfacecolor="yellow")
plt.title("Yearly Temperature Fluctuations\n", fontweight="bold")
plt.xlabel("Days", fontweight="bold")
plt.ylabel("Temperature (°C)", fontweight="bold")
plt.grid(axis="y")
plt.show()


print("\n📉 PART 3: Product Sales Analysis")

# Products List
product_name = ["Phone", "Computer", "Headphones", "Watch", "Tablet"]

# We generate 30 days of random sales data for each product and store it in a dictionary
sales_data = {product: np.random.randint(10, 101, 30) for product in product_name}

# We calculate total sales
total_sales = {product: np.sum(sales) for product, sales in sales_data.items()}

# We calculate average sales
avg_sales = {product: np.mean(sales) for product, sales in sales_data.items()}

# Print the results
print("\n      ***** PRODUCTS ******\n")

for product in product_name:
    print(f"|{product.upper()}|")
    print(
        "|---------------------------------|"
        f"\n| Monthly Total Sales = {total_sales[product]} $    |"
        f"\n| Monthly Average Sales = {avg_sales[product]:.2f} $ |"
        "\n|---------------------------------|\n\n")

# We visualize the total sales of products with a bar chart
plt.figure(figsize=(10, 6))
plt.bar(product_name, list(total_sales.values()), color="skyblue", edgecolor="black", width=0.6)
plt.xlabel("\nProducts", fontweight="bold")
plt.ylabel("Total Sales Amount\n", fontweight="bold")
plt.title("Monthly Sales Data of Products\n", fontweight="bold")
plt.grid(axis="y")
plt.show()
