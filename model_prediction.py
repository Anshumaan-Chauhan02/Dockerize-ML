import numpy as np
import pickle

classifier = pickle.load(open('./classifier_model', 'rb'))
labels = {0:'Setosa', 1:'Versicolor', 2:'Virginica'}
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