import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data, target = load_iris(return_X_y=True)
labels = {0:'Setosa', 1:'Versicolor', 2:'Virginica'}
train_X, test_X, train_Y, test_Y = train_test_split(data, target, test_size=0.2, random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(train_X, train_Y)
pred_Y = classifier.predict(test_X)
print(f"Accuracy Score: {accuracy_score(pred_Y, test_Y)}")
model_inputs = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
count = 0
inputs = []
while count<4:
    try:
        entered_value = float(input(f"Enter {model_inputs[count]} \n"))
        if entered_value <= 0:
            print("I1.2nvalid value")
        else:
            inputs.append(entered_value)
            count+=1
    except:
        print('Invalid data type for the value')
inputs = np.array(inputs).reshape(1,-1)
print(f"Prediction: {labels[classifier.predict(inputs)[0]]}")
