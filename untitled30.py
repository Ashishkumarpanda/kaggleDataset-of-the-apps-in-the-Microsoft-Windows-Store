#importing liabraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn import metrics
#read dataset

data=pd.read_csv("msft.csv")

#converting catagorical data into numerical data

le=LabelEncoder()
data.drop(axis=0,index=5321,inplace=True)
data['Category']=le.fit_transform(data['Category'])
data['Name']=le.fit_transform(data['Name'])
data['Rating']=le.fit_transform(data['Rating'])
data['No of people Rated']=le.fit_transform(data['No of people Rated'])
data['Date']=le.fit_transform(data['Date'])
data['Price']=le.fit_transform(data['Price'])
data

x=data.iloc[:,0:5].values
y=data.iloc[:,5].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

lr=LogisticRegression(random_state=0)
lr.fit(x_train,y_train)

value=metrics.accuracy_score(y_test,lr.predict(x_test))
p=value*100
print("accuracy is=",str(p)+" %")

plt.plot(x_train,y_train,'*')
label=data.columns
plt.xlabel("Details")
plt.ylabel("Book Price")
plt.title("Model")
plt.legend(label)
plt.show()















