import json

def estimate_price(theta0 , theta1, mileage): # linear operation to be performed 
    return theta0 + (theta1 * mileage)

def predict_price(mileage):
    with open("thetas.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    predicted_price = estimate_price(data["theta0"], data["theta1"], mileage)
    return predicted_price

def predict_price_by_mileage ():
    try:
        value = input("Enter a mileage to predict a price: ")
        mileage = float (value)
        price_predcited = predict_price(mileage)
        print("price is:", price_predcited)
    
    except ValueError:
        print("Value must be an valid integer!")
    except KeyboardInterrupt:
        print("Error")
    except Exception:
        print("Error exception")

if __name__ == "__main__":
    predict_price_by_mileage()