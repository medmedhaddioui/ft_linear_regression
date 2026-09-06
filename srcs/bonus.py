import matplotlib.pyplot as plt
import numpy as np
from mandatory.training import read_dataset

def display_data():
    plt.q

def display_graph():
    mileage, price = read_dataset("data.csv")
    x = np.array(mileage)
    y = np.array(price)
    print( x, y)
    display_data(mileage, price)
    pass
if __name__ == "__main__":
    display_graph