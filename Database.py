import pyodbc

server = '192.168.15.47'
port = '1433'
database = 'AdventureWorks2017'
username = 'TDS'
password = 'TehranData@@'
ClientCharset = 'UTF-8'
ServerCharset = 'CP1252'
driver = '{FreeTDS}'

conn_string = (
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"PORT={port};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"ClientCharset={ClientCharset};"
    f"ServerCharset={ServerCharset};"
)
connection = pyodbc.connect(conn_string)

def get_data_from_database():
    query = "SELECT TOP(100) * FROM Purchasing.Vendor"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    res = dict()
    for row in rows:
        res[row[0]] = row[2]
    return res

def get_RFM(customer_id):
    query = '''
    SELECT
        DATEDIFF(DAY, MAX(soh.OrderDate), GETDATE()) AS Recency,
        COUNT(soh.SalesOrderID) AS Frequency,
        SUM(soh.TotalDue) AS Monetary
    FROM
        Sales.Customer c
            JOIN Sales.SalesOrderHeader soh 
                ON c.CustomerID = soh.CustomerID
    WHERE c.CustomerID = {}
    GROUP BY
        c.CustomerID;
    '''.format(customer_id)
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    res = dict()
    for row in rows:
        res['Recency'] = row[0]
        res['Frequency'] = row[1]
        res['Monetary'] = row[2]
    return res

def get_Total_RFM():
    query = '''
    SELECT
        c.CustomerID,
        DATEDIFF(DAY, MAX(soh.OrderDate), GETDATE()) AS Recency,
        COUNT(soh.SalesOrderID) AS Frequency,
        SUM(soh.TotalDue) AS Monetary
    FROM
        Sales.Customer c
            JOIN Sales.SalesOrderHeader soh 
                ON c.CustomerID = soh.CustomerID
    GROUP BY
        c.CustomerID;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    res_list = []
    for row in rows:
        res = dict()
        res['CustomerID'] = row[0]
        res['Recency'] = row[1]
        res['Frequency'] = row[2]
        res['Monetary'] = row[3]
        res_list.append(res)
    return res_list
