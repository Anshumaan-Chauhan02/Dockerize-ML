from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

data, target = load_iris(return_X_y=True)
train_X, test_X, train_Y, test_Y = train_test_split(data, target, test_size=0.2, random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(train_X, train_Y)
pred_Y = classifier.predict(test_X)
print(f"Accuracy Score: {accuracy_score(pred_Y, test_Y)}")
pickle.dump(classifier, open('./classifier_model','wb'))
