import pandas as pd
import numpy

dic1={
    "name":['Anshu','Pardu','Chini'],
    "marks":[8,9,10],
    "city":['ktm','shilling','antarctica'],
    "age": [10,21,30]

}
#thislist=["ktm",'shilling','antarctica']

x = pd.DataFrame(dic1) #converts to excel sheet 
x.index = ['first','second','third']  #changing type of index

#print(x)
x.to_csv('new.csv', index=False) #index = False se index nahi dega 0,1,2x.head
print(x.head(2))  #prints 2 rows from head
print(x.tail(2))  #prints 2 rows from tail
print(x.describe())  #gives mean ,count,etc. for numerical values
#print(pd.read_csv("new.csv"))
#print(x['name'])
x['marks']['first'] = 10   #updating the values  accessing like multidimensional array but first column then row
print(x[0])
x.to_csv('new.csv',index=False)


