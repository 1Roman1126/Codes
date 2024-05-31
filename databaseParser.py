# IMPORT
import sqlite3 as sqlite
def addToDatabase(symbol,data):
    # *
    pathToDatabase = "./database/database.db"

# Connecting to sqlite database
    conn = sqlite.connect(pathToDatabase)
    cursor = conn.cursor()

# Executions logics
    # Creating table query
    tableQuery = f"""CREATE TABLE IF NOT EXISTS {symbol} (ID INTEGER PRIMARY KEY,
    SECURITYNAME TEXT ,OPENPRICE REAL, HIGHPRICE REAL, LOWPRICE REAL,CLOSEPRICE REAL,
    TOTALTRADEDQUANTITY REAL, TOTALTRADEDVALUE REAL,
    PREVIOUSDAYCLOSEPRICE REAL,
    TOTALTRADES REAL,
    AVERAGETRADEDPRICE REAL,
    DATE DATE 
    )"""
    # Inserting data query
    dataQuery = f"""
    INSERT INTO {symbol}
        (SECURITYNAME, OPENPRICE, HIGHPRICE, LOWPRICE, CLOSEPRICE,
        TOTALTRADEDQUANTITY, TOTALTRADEDVALUE, PREVIOUSDAYCLOSEPRICE,
        TOTALTRADES, AVERAGETRADEDPRICE, DATE)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

    # Executing query
    cursor.execute(tableQuery)
    cursor.execute(dataQuery,list(data.values()))
    # Commit to database
    conn.commit()
    # Close connection
    conn.close()





