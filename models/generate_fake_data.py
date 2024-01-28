from faker import Faker
from uuid import uuid4
from random import randint, choice
import csv
from datetime import datetime, timedelta, date

def generate_customers():
    """ 
    Function to generate fake customers 
    Write to csv file
    """
    
    fake = Faker()
    
    cities = ["Paris", "Nantes","Lyon","Lille","Marseille","Bordeaux","Toulouse","Rennes","Rouen","Paris","Paris","Paris","Lille","Lille","Lyon","Lyon","Paris"]  # List of cities
    header = ["CustId","CustFirstName","CustLastName","CustCity"]  # Header for the CSV file
    with open('../data/customers.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Writing the header row
        for id in range(1, 101):  # Generating data for 100 customers
            row = []
            row.append(id)
            fname = fake.first_name()
            row.append(fname)
            lname = fake.last_name()
            row.append(lname)
            city = choice(cities)  # Randomly selecting a city
            row.append(city)
            writer.writerow(row)  # Writing the customer data row
            
def generate_products():
    """
    Generates synthetic product data and writes it to a CSV file.
    """
    brands = ["HP", "Acer", "Dell", "Visio", "Thinkpad", "Mac Pro", "Asus"]  # List of product brands
    rams = ["X32", "X64", "X128"]  # List of RAM sizes
    disks = ["SSD", "HDD"]  # List of disk types
    header = ["ProdId", "ProdCode", "ProdBrand", "ProdCost", "ProdPrice"]  # Header for the CSV file
    costs = [300, 400, 500, 600, 700, 800]  # List of product costs
    prices = [900, 1000, 1200, 1500, 2000, 2500]  # List of product prices

    with open("data_generated/products.csv", mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Writing the header row
        for id in range(1, 41):  # Generating data for 40 products
            row = []
            row.append(id)
            brand = choice(brands)  # Randomly selecting a brand
            ram = choice(rams)  # Randomly selecting a RAM size
            disk = choice(disks)  # Randomly selecting a disk type
            x = uuid4()
            code = brand + "-" + ram + "-" + disk + "-" + str(x)
            row.append(code)
            row.append(brand)
            cost = choice(costs)  # Randomly selecting a cost
            row.append(cost)
            price = choice(prices)  # Randomly selecting a price
            row.append(price)
            writer.writerow(row)  # Writing the product data row
            
def generate_orders_stocks():
    """
    Generates synthetic order and stock data and writes them to CSV files.
    """
    header = ["StockDate","ProdId","StockQty"]  # Header for the stocks CSV file
    with open("data_generated/stocks.csv", mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Writing the header row
        for i in range(1, 41):  # Generating data for 40 stock items
            row = []
            row.append("2019-12-31")  # Setting a fixed stock date
            row.append(i)
            row.append(100)  # Setting the stock quantity to 100
            writer.writerow(row)  # Writing the stock data row

    s = [100 for i in range(40)]  # Initializing the stock quantities for each product
    qtes = [1, 2, 5, 6, 8, 10, 12, 14, 15, 20, 25]  # List of order quantities
    debut = datetime(2020, 1, 1).date()  # Setting the start date for generating orders
    header = ["OrderId","OrderDate","ProdId","CustId","Qty","IsHonored"]  # Header for the orders CSV file
    id = 0
    with open("data_generated/orders.csv", mode="w") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Writing the header row
        while debut != date.today():
            for index, item in enumerate(s):
                if item < 15:  # Checking if the stock quantity is less than 15
                    s[index] = 50  # Replenishing the stock quantity to 50
            n = randint(500, 1000)  # Randomly generating the number of orders for the current day
            for i in range(n):
                row = []
                id += 1
                row.append(id)
                row.append(debut)
                product = randint(1, 40)  # Randomly selecting a product
                row.append(product)
                customer = randint(1, 100)  # Randomly selecting a customer
                row.append(customer)
                qty = choice(qtes)  # Randomly selecting an order quantity
                row.append(qty)
                if s[product - 1] > qty:  # Checking if the stock is sufficient for the order
                    IsHonored = True
                    s[product - 1] -= qty  # Updating the stock quantity
                else:
                    IsHonored = False
                row.append(IsHonored)
                writer.writerow(row)  # Writing the order data row

            with open("data_generated/stocks.csv", mode="a") as stocks:
                writer_stock = csv.writer(stocks)
                for index, product in enumerate(s):
                    stock = []
                    stock.append(debut)
                    stock.append(index + 1)
                    stock.append(product)
                    writer_stock.writerow(stock)  # Writing the stock data row

            debut += timedelta(days=1)
            
