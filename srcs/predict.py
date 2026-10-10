import json

def estimate_price(theta0 , theta1, mileage): # linear operation to be performed 
    return theta0 + (theta1 * mileage)

def predict_price(mileage):
    try:
        with open("thetas.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"theta0": 0.0, "theta1": 0.0}
    predicted_price = estimate_price(data["theta0"], data["theta1"], mileage)
    return predicted_price

def predict_price_by_mileage ():
    try:
        price_predcited = 0
        mileage = int (input("Enter a mileage to predict a price: "))
        if mileage < 0:
            raise ValueError("mileage must be a non-negative integer.")
        price_predcited = predict_price(mileage)
        print("price is:", price_predcited)
    
    except ValueError as error:
        print("Value:", error)
    except KeyboardInterrupt:
        print("\nInput cancelled.")
    except Exception:
        print("Error exception")
        return 

if __name__ == "__main__":
    predict_price_by_mileage()