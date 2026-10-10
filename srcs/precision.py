import json
from ft_linear_regression import read_dataset

mileage, prices = read_dataset("data.csv")
try:
    with open("thetas.json", "r") as file:
        thetas = json.load(file)
except Exception:
    print("Error")
predictions = [thetas["theta0"] + thetas["theta1"] * km for km in mileage]
average = sum(prices) / len(prices)
total_error = sum((price - prediction) ** 2 for price, prediction in zip(prices, predictions))
total_variation = sum((price - average) ** 2 for price in prices)

precision = 1 - total_error / total_variation
print(f"Precision: {precision * 100:.2f}%")
