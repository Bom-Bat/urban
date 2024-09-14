import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a = np.array([1, 2, 3, 4, 5, 6])
print(a,'\n')
a = np.linspace(-5, 5, 11)
print(a,'\n')
print(a*a,'\n')
print(a-a,'\n')
a = np.random.rand(10)*10
print(a,'\n')
a = np.zeros((3, 3), 'str')
print(a,'\n')
a[0][0] = 'x'
a[1][1] = 'x'
a[2][2] = 'x'
print(a,'\n')

x = np.random.rand(10)*10
y = np.random.rand(10)*10

plt.scatter(x, y)
plt.show()
plt.plot(x, y, color='green', marker='o', markersize=7)
plt.show()

a = np.arange(36)
print(a,'\n')
b = a.reshape(6, 6)
print(b,'\n')



def sigmoid(alpha):
    return 1 / (1 + np.exp(- alpha * a))


dpi = 20
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi) )
a = np.linspace(-5, 5, 100)
plt.plot(a, sigmoid(0.5), 'ro-')
plt.plot(a, sigmoid(1.0), 'go-')
plt.plot(a, sigmoid(2.0), 'bo-')

plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc='upper left')

fig.savefig('sigmoid.png')

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df,'\n')
print(df['Name'],'\n')
print(df.iloc[1],'\n')
print(df.loc[2],'\n')

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Month': ['January', 'January', 'January', 'February', 'February', 'February'],
    'Sales': [250, 300, 200, 400, 500, 300]
}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(values='Sales', index='Name', columns='Month', aggfunc='sum')
print(pivot_table)

