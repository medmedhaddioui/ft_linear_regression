from training import train, prediction_price
def predict_price_by_mileage ():
    try:
        value = input("Enter a mileage to predict a price: ")
        mileage = float (value)
        theta0, theta1, min_x, max_x = train()
        price_predcited = prediction_price(theta0, theta1, min_x, max_x, mileage)
        print("price is:", price_predcited)
    
    except ValueError:
        print("Value must be an valid integer!")
    except KeyboardInterrupt:
        print("Error")
    except Exception:
        print("Error exception")

if __name__ == "__main__":
    predict_price_by_mileage()