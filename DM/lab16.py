#Display total and average of qty sold City-wise, Product-wise and Salesman-wise
import pandas as pd

data = {
    'SalesManName': ['Ravi','Prakash','Seema','Ravi','Anil','Seema','Prakash','Ravi'],
    'City': ['Delhi','Mumbai','Delhi','Mumbai','Delhi','Mumbai','Delhi','Mumbai'],
    'Product': ['Laptop','Mobile','Laptop','Mobile','Laptop','Mobile','Laptop','Mobile'],
    'Qty': [5, 10, 15, 20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# City-wise total and average
c = df.groupby('City')['Qty'].agg(['sum', 'mean'])
print("City-wise Total and Average:\n", c)

#Product-wise total and average
p = df.groupby('Product')['Qty'].agg(['sum', 'mean'])
print("Product-wise Total and Average:\n", p)

#Salesman-wise total and average
s = df.groupby('SalesManName')['Qty'].agg(['sum', 'mean'])
print("Salesman-wise Total and Average:\n", s)