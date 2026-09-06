import pandas as pd

def estimate_price(theta0 , theta1, mileage):
    return theta0 + (theta1 * mileage)

def prediction_price(theta0, theta1, min_x, max_x, mileage):
    normalized_x = (mileage - min_x) / (max_x - min_x)
    return estimate_price(theta0, theta1, normalized_x)

def training_model(theta0, theta1, mileage, price, number_of_samples):
    learning_rate = 0.01
    min_x =  min(mileage)
    max_x  = max(mileage)
    for _ in range(5000):
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

def train():
    try:
        mileage, price = read_dataset("data.csv")
        theta0, theta1 = 0, 0
        theta0, theta1, min_x, max_x = training_model(theta0 , theta1, mileage, price, len (mileage))
        print(theta0, theta1)
        return theta0, theta1, min_x, max_x
    
    except ValueError as error:
        print("ValueError: ", error)
    except Exception:
        print("Error been raised")

if __name__ == "__main__":
    train()