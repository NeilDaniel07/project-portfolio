# -*- coding: utf-8 -*-
"""HeartPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KqHVxbkLFmZLLpqy4G1Z8Bz5pylCQrWB
"""



import pandas as pd
from sklearn.tree import DecisionTreeClassifier

train = pd.read_csv("Prediction.csv")
vars = train.drop(columns=['target'])
y = train['target']
#vars_train, vars_test, y_train, y_test = train_test_split(vars, y, test_size = 0.15)

model = DecisionTreeClassifier()
model.fit(vars.values, y)
#expected = model.predict(vars_test)
#score = accuracy_score(y_test, expected)
#print(score * 100)


age = input("Age: ")
sex = input("Sex (Enter 0 if female, 1 if male): ")
cp = input("Chest pain type: (0 if typical angina, 1 if atypical angina, 2 if non-anginal pain, 3 if asymptomatic) ")
bp = input("Resting Blood Pressure: (Systolic Pressure/Top Number) ")
chol = input("Cholesterol (mg/dl): ")
fbp = input("Is your fasting blood pressure greater than 120 mg/dl (0 for false, 1 for true): ")
ekg = input("EKG Results (0 if normal, 1 if wave abnormaility, 2 if ventricular hypertrophy; Enter 0 if unaware): ")
maxhr = input("Maximum heart rate you observed: ")
angina = input("Do you have exercise inducded angina (1 for yes, 0 for no): ")
thal = input("Thalassemia (1 for none, 2 for moderate, 3 for major) ")

prediction = model.predict([[age, sex, cp, bp, chol, fbp, ekg, maxhr, angina, thal]])

print(prediction == 1)