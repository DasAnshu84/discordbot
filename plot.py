import matplotlib.pyplot as pl
x=["python","c","c++","Java"]
y=[85,70,60,82]
pl.xlabel("language",fontsize=20)
pl.ylabel("Number of users")
pl.title("POPULARITY OF PROGRAMMING LANGUAGES",fontsize=50)
c=["y","b","m","g","r"]  #color list
pl.bar(x,y,width=0.1,color=c)  #color=c for assigning colors to each bar
pl.show()