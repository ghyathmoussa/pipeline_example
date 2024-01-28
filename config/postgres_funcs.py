from config import default_db
import csv
import time

def postgres_initialization_customers_products(db):
    
    cursor = default_db.cursor()

    create_customer = """
    CREATE TABLE Customers (
        CustId INT,
        CustFirstName VARCHAR(100),
        CustLastName VARCHAR(100),
        CustCity VARCHAR(100)
    )
    """

    create_prod = """
    CREATE TABLE Products (
        ProdId INT,
        ProdCode VARCHAR(100),
        ProdBrand VARCHAR(100),
        ProdCost INT,
        ProdPrice INT
    )
    """

    cursor.execute(create_customer)
    cursor.execute(create_prod)

    with open("../data/customers.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_query = "INSERT INTO Customers VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, row)

    with open("../data/products.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_query = "INSERT INTO Products VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, row)

    default_db.commit()
    cursor.close()
    default_db.close()
    print("Products and customers have been successfully uploaded")
    
    
def postgre_initial_orders_stocks(db):
    t0 = time.time()
    
    cursor = default_db.cursor()

    create_orders = """
    CREATE TABLE IF NOT EXISTS Orders (
        OrderId INT,
        OrderDate DATE,
        ProdId INT,
        CustId INT,
        Qty INT,
        IsHonored BOOLEAN
    )
    """

    create_stocks = """
    CREATE TABLE IF NOT EXISTS Stocks (
        StockDate DATE,
        ProdId INT,
        StockQty INT
    )
    """

    cursor.execute(create_orders)
    cursor.execute(create_stocks)

    with open("data_generated/orders.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_query = "INSERT INTO Orders VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, row)
    t1 = time.time()
    print(f"Orders took {t1-t0} s")
    with open("data_generated/stocks.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            insert_query = "INSERT INTO Stocks VALUES (%s, %s, %s)"
            cursor.execute(insert_query, row)

    default_db.commit()
    cursor.close()
    default_db.close()
    print(f"Stocks took {time.time()-t1} s")
    
