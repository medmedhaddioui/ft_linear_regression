import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

def display_data(mileage, price):

    plt.scatter(mileage, price, label="Data Points")
    plt.title("Price/Mileage Graph")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def plot_regression_line(theta0, theta1, min_x, max_x, mileage, price):
    plt.scatter(mileage, price, color="blue", label="Data Points")
    
    x_line = np.linspace(min_x, max_x, 100)
    normalized_x = (x_line - min_x) / (max_x - min_x)
    y_line = estimate_price(theta0, theta1, normalized_x)
    
    plt.plot(x_line, y_line, color="red", linewidth=2, label="Regression Line")
    plt.title("Linear Regression Line Within Data")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()



def save_thetas(theta0, theta1, filename="thetas.json"):
    data = {
        "theta0": theta0,
        "theta1": theta1
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def estimate_price(theta0 , theta1, mileage): # linear operation to be performed 
    return theta0 + (theta1 * mileage)

def prediction_price(theta0, theta1, min_x, max_x, mileage):
    normalized_x = (mileage - min_x) / (max_x - min_x)
    return estimate_price(theta0, theta1, normalized_x)

def training_model(theta0, theta1, mileage, price, number_of_samples):

    learning_rate = 0.1
    min_x =  min(mileage)
    max_x  = max(mileage)
    if min_x == max_x:
        raise ValueError("Error mileage are identical")
    for _ in range(1000):
        error_sum_theta1 = 0
        error_sum_theta0 = 0
        for x, y in zip(mileage, price):
            normalized_x = (x - min_x) / (max_x - min_x)
            prediction = estimate_price(theta0, theta1, normalized_x)
            error_sum_theta0 += prediction - y
            error_sum_theta1 += (prediction - y) * normalized_x
        
        tmp_theta0 = (learning_rate * error_sum_theta0) / number_of_samples
        tmp_theta1 = (learning_rate * error_sum_theta1) / number_of_samples
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1, min_x, max_x

def read_dataset(filename):

    df = pd.read_csv(filename)
    if df.empty:
        raise ValueError("Error on data File")
    mileage  = df["km"].to_list()
    price = df["price"].to_list()
    if len(mileage) != len(price):
        raise ValueError("Rows are not equal")
    return mileage, price

def main():
    try:
        mileage, price = read_dataset("data.csv")
        print(mileage, price)
        value = input("Do you want to visualise your data into a graph: (Y/N) ?\n").lower()
        if value == "y":
            display_data(mileage, price);
        theta0, theta1 = 0, 0
        theta0, theta1, min_x, max_x = training_model(theta0 , theta1, mileage, price, len (mileage))
        unnorm_theta1 = theta1 / (max_x - min_x)
        unnorm_theta0 = theta0 - (theta1 * min_x) / (max_x - min_x)
        save_thetas(unnorm_theta0, unnorm_theta1)

        value = input("Do you want to visualise your linear regression within your data: (Y/N)\n").lower()
        if value == "y":
            plot_regression_line(theta0, theta1, min_x, max_x, mileage, price)
        print(f"Model parameters saved to '{"thetas.json"}': theta0 = {theta0:.4f}, theta1 = {theta1:.4f}") 
    
    except ValueError as error:
        print("ValueError: ", error)
    except Exception:
        print("Error been raised")
    except KeyboardInterrupt:
        print("Error")

if __name__ == "__main__":
    main()