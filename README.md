# Predict Car Prices with Mileage

In this project, I scrape the [TrueCar](https://www.truecar.com) website to gather data on various cars, including their mileage and prices. Then, I insert this data into my local MySQL database. Finally, I use a Decision Tree algorithm to analyze the data and predict car prices.

This project consists of four Python files:

1. `database.py` contains the `Database` class, which allows connecting to the local database and executing queries using the `mysql.connector` package.
2. `fetch.py` utilizes the `requests`, `re`, and `BeautifulSoup` packages to scrape the required data from the website and insert it into the database.
3. `ml.py` involves selecting data from the database and using the `scikit-learn` package to analyze and learn from the data.
4. `main.py` serves as an example of how to use these files in conjunction.
