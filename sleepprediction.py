# -*- coding: utf-8 -*-
"""SleepPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HSP1pYKYoBSYD0OJmBwfJRXJqcME_O4f
"""

from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
# define dataset
import warnings
warnings.simplefilter('ignore', UserWarning)
train = pd.read_csv("final.csv")
train = train.fillna(-10000)
X = train.drop(columns=['label'])
y = train['label']
X_train, y_train = X, y
model = DecisionTreeRegressor()
model.fit(X_train, y_train)
importance = model.feature_importances_
for i,v in enumerate(importance):
 print('Feature: %0d, Importance: %.3f' % (i,v * 100))
featurelist = ["Age", "Gender", "Sleep Duration", "REM Sleep %", "Deep Sleep %", "Light Sleep %", "Awakenings", "Caffeine Consumption", "Alcohol Consumption", "Smoker", "Exercise Frequency"]
pyplot.bar([featurelist[x] for x in range(len(importance))], importance * 100)
pyplot.xticks(rotation = 90)
pyplot.xlabel("Factors Influencing Sleep Quality")
pyplot.ylabel("Relative Importance Out Of 100")
pyplot.show()

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Define dataset
train = pd.read_csv("final.csv")
train = train.fillna(-10000)
X = train.drop(columns=['label'])

#print(X)
# Perform K-means clustering
model = KMeans(n_clusters=6, random_state=0)
model.fit(X)

# Calculate WCSS for each feature
wcss_scores = []
print(X.shape[1])
for i in range(X.shape[1]):
    feature = X.iloc[:, i].values.reshape(-1, 1)
    model_i = KMeans(n_clusters=6, random_state=0)
    model_i.fit(feature)
    wcss_scores.append(model_i.inertia_)

# Calculate relative importance as the percentage of WCSS contribution
total_wcss = np.sum(wcss_scores)
relative_importance = [score / total_wcss for score in wcss_scores]

# Get feature names
feature_names = X.columns

# Sort feature importance in descending order
sorted_indices = np.argsort(relative_importance)[::-1]
sorted_scores = np.array(relative_importance)[sorted_indices]
sorted_feature_names = feature_names[sorted_indices]

# Print and plot feature importance
for i, (name, score) in enumerate(zip(sorted_feature_names, sorted_scores)):
    print('Feature: %s, Relative Importance: %.5f' % (name, score * 100))

import matplotlib.pyplot as plt
plt.bar(range(len(sorted_feature_names)), sorted_scores)
plt.xlabel("Factors Influencing Sleep Quality")
plt.ylabel("Relative Importance Out Of 100")
plt.xticks(range(len(sorted_feature_names)), sorted_feature_names, rotation=90)
plt.show()