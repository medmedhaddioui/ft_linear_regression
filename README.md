# Linear Regression

This project learns to estimate a car's price from its mileage. It uses a small dataset of cars and trains a simple linear model, which draws the best fitting straight line through the data.

The model uses this formula:

```text
estimated price = theta0 + (theta1 × mileage)
```

`theta0` and `theta1` are the values the training script learns from the data.

## Project files

- `srcs/data.csv` contains the example car mileages (`km`) and prices.
- `srcs/ft_linear_regression.py` trains the model and saves its learned values to `srcs/thetas.json`. It can also show graphs of the data and fitted line.
- `srcs/predict.py` asks for a mileage and estimates the car's price using the saved model values.
- `srcs/precision.py` compares the model's estimates with the dataset and prints its R² score. A score closer to 1 means the model fits the data better.
- `srcs/subject.pdf` contains the project subject.

## Requirements

Python 3 with `pandas`, `numpy`, and `matplotlib` installed:

```bash
python3 -m pip install pandas numpy matplotlib
```

## Run the project

Install the required Python libraries:

```bash
python3 -m pip install pandas numpy matplotlib
```

Then run the scripts from the `srcs/` directory, since they look for the data and model files there:

```bash
cd srcs
python3 ft_linear_regression.py
```

Answer the prompts to choose whether to display graphs. Training creates or updates `thetas.json`. After that, you can run:

```bash
python3 predict.py
python3 precision.py
```

Run the training script again whenever you change `data.csv` so the saved model matches the updated data.
