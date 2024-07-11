pip install matplotlib #first install the matplotlib library
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y)
plt.plot(x,y,linestyle="dotted",color = '#5D6D7E',linewidth ="7",marker="o",mfc="r",ms="10") or plt.plot(x,y,ls=":") #this will print dotted line

plt.plot(x,y,linestyle="dashed") or plt.plot(x,y,ls="--") 
plt.xlabel('X-axis')
plt.ylable('Y-axis')
plt.title('Simple Line Plot')
plt.show()
import numpy as np
y1=np.array([3,5,3,8])
y2=np.array([1,9,7,4])
plt.plot(y1)
plt.plot(y2)
plt.show

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.scatter(x,y,color="red")
plt.xlabel('sales')
plt.ylable('price')
plt.title('Simple Scatter Plot')
plt.show()

products = ['PC', 'TV', 'Ref', 'Micro']
sales = [4, 7, 1, 8]

plt.bar(products, sales, color="black",width=0.1) #it will create verticle ber graph
plt.barh(products, sales, color="black",width=0.1) #it will create horizontal ber graph. instead of bar I have written barh 
plt.xlabel('products')
plt.ylabel('Sales(in 1000s)')
plt.title('Simple Bar Plot')
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4) 
plt.xlabel('Value']
plt.ylabel('Frequency')
plt.title('Simple Histogram')
plt.show()

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2=[1, 4, 6, 8, 10]

fig, axs = plt.subplots(2)
axs[0].plot(x, y1)
axs[0].set_title('First Plot')
axs[1].plot(x, y2, 'tab:orang')
axs[1].set_title('Second Plot')

plt.tight_layout()
plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Annotations')
plt.annotate('Peak', xy=(5, 11), xytext=(4, 10), arrowprops=dict(facecolor='black', shrink=0.05)) #it will show peak written at 4,10 and a arrow pointing at 5,11
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

sns.lineplot(x=x, y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt. title('Simple Line Plot with Seaborn')
plt.show()

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]

sns.scatterplot(x=x1, y=y1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt. title('Simple Scatter Plot with Seaborn')
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

sns.barplot(x=categories, y=values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot with Seaborn')
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

sns.histplot(data, bins=4) 
plt.xlabel('Value']
plt.ylabel('Frequency')
plt.title('Simple Histogram with Seaborn')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris #Search about iris dataset

iris = load_iris()
iris_data = sns.load_dataset("iris")

sns.pairplot(iris_data, hue='species')
plt.title('Pair Plot with Seaborn')
plt.show()

import numpy as np

data = np.random.rand(10, 12)
sns.heatmap(data)
plt. title('Heatmap with Seaborn')
plt.show()
