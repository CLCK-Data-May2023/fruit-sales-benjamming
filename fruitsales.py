import pandas as pd

data = {"Apples":[35, 41], "Bananas": [21, 34]}

fruit_sales = pd.DataFrame(data, 
             index=("2017 Sales", "2018 Sales"))


if __name__ == "__main__":
    fruit_sales.to_csv("fruit.csv")