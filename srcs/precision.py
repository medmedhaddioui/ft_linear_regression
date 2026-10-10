import json

from ft_linear_regression import read_dataset


def main():
    try:
        mileage, prices = read_dataset("data.csv")
        with open("thetas.json", "r") as file:
            thetas = json.load(file)

        theta0 = thetas["theta0"]
        theta1 = thetas["theta1"]

        predictions = [theta0 + theta1 * km for km in mileage]
        average = sum(prices) / len(prices)
        total_error = sum(
            (price - prediction) ** 2
            for price, prediction in zip(prices, predictions)
        )
        total_variation = sum((price - average) ** 2 for price in prices)

        if total_variation == 0:
            print("R squared (R2) is undefined when all prices are identical.")
            return

        r_squared = 1 - total_error / total_variation

        print(f"R squared (R2): {r_squared:.4f}")
        print(f"predicting the average price: {r_squared * 100:.2f}%")
    
    except FileNotFoundError as error:
        print(f"File not found: {error.filename}. Ensure data.csv exists and train the model first.")
    except Exception as error:
        print(f"Cannot calculate R squared: {error}")


if __name__ == "__main__":
    main()
