import pandas

d = [[1, 2, 3, 4, 5], [1, 2, 4, 8, 9]]
df1 = pandas.DataFrame(d, index=['Jak liczy dorosły', 'Jak liczy Franeczek'])
print(type(df1))
print(df1)