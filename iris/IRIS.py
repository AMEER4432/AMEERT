import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
dict1={'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.9', 'sepal_width': '3', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.7', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '4.6', 'sepal_width': '3.4', 'petal_length': '1.4', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.4', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.4', 'sepal_width': '2.9', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.9', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '5.4', 'sepal_width': '3.7', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.8', 'sepal_width': '3.4', 'petal_length': '1.6', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.8', 'sepal_width': '3', 'petal_length': '1.4', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '4.3', 'sepal_width': '3', 'petal_length': '1.1', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '5.8', 'sepal_width': '4', 'petal_length': '1.2', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.7', 'sepal_width': '4.4', 'petal_length': '1.5', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '5.7', 'sepal_width': '3.8', 'petal_length': '1.7', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.8', 'petal_length': '1.5', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '5.4', 'sepal_width': '3.4', 'petal_length': '1.7', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.7', 'petal_length': '1.5', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '4.6', 'sepal_width': '3.6', 'petal_length': '1', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.3', 'petal_length': '1.7', 'petal_width': '0.5', 'species': 'Iris-setosa'}
{'sepal_length': '4.8', 'sepal_width': '3.4', 'petal_length': '1.9', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3', 'petal_length': '1.6', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.4', 'petal_length': '1.6', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '5.2', 'sepal_width': '3.5', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.2', 'sepal_width': '3.4', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.6', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.8', 'sepal_width': '3.1', 'petal_length': '1.6', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.4', 'sepal_width': '3.4', 'petal_length': '1.5', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '5.2', 'sepal_width': '4.1', 'petal_length': '1.5', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '5.5', 'sepal_width': '4.2', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.9', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.2', 'petal_length': '1.2', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.5', 'sepal_width': '3.5', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.9', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.1', 'species': 'Iris-setosa'}
{'sepal_length': '4.4', 'sepal_width': '3', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.4', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.5', 'petal_length': '1.3', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '4.5', 'sepal_width': '2.3', 'petal_length': '1.3', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '4.4', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.5', 'petal_length': '1.6', 'petal_width': '0.6', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.8', 'petal_length': '1.9', 'petal_width': '0.4', 'species': 'Iris-setosa'}
{'sepal_length': '4.8', 'sepal_width': '3', 'petal_length': '1.4', 'petal_width': '0.3', 'species': 'Iris-setosa'}
{'sepal_length': '5.1', 'sepal_width': '3.8', 'petal_length': '1.6', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '4.6', 'sepal_width': '3.2', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5.3', 'sepal_width': '3.7', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '5', 'sepal_width': '3.3', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'}
{'sepal_length': '7', 'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '5.7', 'sepal_width': '2.8', 'petal_length': '4.5', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '4.7', 'petal_width': '1.6', 'species': 'Iris-versicolor'}
{'sepal_length': '4.9', 'sepal_width': '2.4', 'petal_length': '3.3', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '6.6', 'sepal_width': '2.9', 'petal_length': '4.6', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.2', 'sepal_width': '2.7', 'petal_length': '3.9', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '5', 'sepal_width': '2', 'petal_length': '3.5', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.9', 'sepal_width': '3', 'petal_length': '4.2', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '6', 'sepal_width': '2.2', 'petal_length': '4', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '6.1', 'sepal_width': '2.9', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '5.6', 'sepal_width': '2.9', 'petal_length': '3.6', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.7', 'sepal_width': '3.1', 'petal_length': '4.4', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '5.6', 'sepal_width': '3', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '4.1', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '6.2', 'sepal_width': '2.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '5.6', 'sepal_width': '2.5', 'petal_length': '3.9', 'petal_width': '1.1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.9', 'sepal_width': '3.2', 'petal_length': '4.8', 'petal_width': '1.8', 'species': 'Iris-versicolor'}
{'sepal_length': '6.1', 'sepal_width': '2.8', 'petal_length': '4', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.3', 'sepal_width': '2.5', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '6.1', 'sepal_width': '2.8', 'petal_length': '4.7', 'petal_width': '1.2', 'species': 'Iris-versicolor'}
{'sepal_length': '6.4', 'sepal_width': '2.9', 'petal_length': '4.3', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.6', 'sepal_width': '3', 'petal_length': '4.4', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '6.8', 'sepal_width': '2.8', 'petal_length': '4.8', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '6.7', 'sepal_width': '3', 'petal_length': '5', 'petal_width': '1.7', 'species': 'Iris-versicolor'}
{'sepal_length': '6', 'sepal_width': '2.9', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '5.7', 'sepal_width': '2.6', 'petal_length': '3.5', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.5', 'sepal_width': '2.4', 'petal_length': '3.8', 'petal_width': '1.1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.5', 'sepal_width': '2.4', 'petal_length': '3.7', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '3.9', 'petal_width': '1.2', 'species': 'Iris-versicolor'}
{'sepal_length': '6', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.6', 'species': 'Iris-versicolor'}
{'sepal_length': '5.4', 'sepal_width': '3', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '6', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'Iris-versicolor'}
{'sepal_length': '6.7', 'sepal_width': '3.1', 'petal_length': '4.7', 'petal_width': '1.5', 'species': 'Iris-versicolor'}
{'sepal_length': '6.3', 'sepal_width': '2.3', 'petal_length': '4.4', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.6', 'sepal_width': '3', 'petal_length': '4.1', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.5', 'sepal_width': '2.5', 'petal_length': '4', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.5', 'sepal_width': '2.6', 'petal_length': '4.4', 'petal_width': '1.2', 'species': 'Iris-versicolor'}
{'sepal_length': '6.1', 'sepal_width': '3', 'petal_length': '4.6', 'petal_width': '1.4', 'species': 'Iris-versicolor'}
{'sepal_length': '5.8', 'sepal_width': '2.6', 'petal_length': '4', 'petal_width': '1.2', 'species': 'Iris-versicolor'}
{'sepal_length': '5', 'sepal_width': '2.3', 'petal_length': '3.3', 'petal_width': '1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.6', 'sepal_width': '2.7', 'petal_length': '4.2', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.7', 'sepal_width': '3', 'petal_length': '4.2', 'petal_width': '1.2', 'species': 'Iris-versicolor'}
{'sepal_length': '5.7', 'sepal_width': '2.9', 'petal_length': '4.2', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.2', 'sepal_width': '2.9', 'petal_length': '4.3', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '5.1', 'sepal_width': '2.5', 'petal_length': '3', 'petal_width': '1.1', 'species': 'Iris-versicolor'}
{'sepal_length': '5.7', 'sepal_width': '2.8', 'petal_length': '4.1', 'petal_width': '1.3', 'species': 'Iris-versicolor'}
{'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6', 'petal_width': '2.5', 'species': 'Iris-virginica'}
{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'}
{'sepal_length': '7.1', 'sepal_width': '3', 'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.5', 'sepal_width': '3', 'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
{'sepal_length': '7.6', 'sepal_width': '3', 'petal_length': '6.6', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '4.9', 'sepal_width': '2.5', 'petal_length': '4.5', 'petal_width': '1.7', 'species': 'Iris-virginica'}
{'sepal_length': '7.3', 'sepal_width': '2.9', 'petal_length': '6.3', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.7', 'sepal_width': '2.5', 'petal_length': '5.8', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '7.2', 'sepal_width': '3.6', 'petal_length': '6.1', 'petal_width': '2.5', 'species': 'Iris-virginica'}
{'sepal_length': '6.5', 'sepal_width': '3.2', 'petal_length': '5.1', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '6.4', 'sepal_width': '2.7', 'petal_length': '5.3', 'petal_width': '1.9', 'species': 'Iris-virginica'}
{'sepal_length': '6.8', 'sepal_width': '3', 'petal_length': '5.5', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '5.7', 'sepal_width': '2.5', 'petal_length': '5', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '5.8', 'sepal_width': '2.8', 'petal_length': '5.1', 'petal_width': '2.4', 'species': 'Iris-virginica'}
{'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '5.3', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '6.5', 'sepal_width': '3', 'petal_length': '5.5', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '7.7', 'sepal_width': '3.8', 'petal_length': '6.7', 'petal_width': '2.2', 'species': 'Iris-virginica'}
{'sepal_length': '7.7', 'sepal_width': '2.6', 'petal_length': '6.9', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '6', 'sepal_width': '2.2', 'petal_length': '5', 'petal_width': '1.5', 'species': 'Iris-virginica'}
{'sepal_length': '6.9', 'sepal_width': '3.2', 'petal_length': '5.7', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '5.6', 'sepal_width': '2.8', 'petal_length': '4.9', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '7.7', 'sepal_width': '2.8', 'petal_length': '6.7', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '6.3', 'sepal_width': '2.7', 'petal_length': '4.9', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.7', 'sepal_width': '3.3', 'petal_length': '5.7', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '7.2', 'sepal_width': '3.2', 'petal_length': '6', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.2', 'sepal_width': '2.8', 'petal_length': '4.8', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.1', 'sepal_width': '3', 'petal_length': '4.9', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.4', 'sepal_width': '2.8', 'petal_length': '5.6', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '7.2', 'sepal_width': '3', 'petal_length': '5.8', 'petal_width': '1.6', 'species': 'Iris-virginica'}
{'sepal_length': '7.4', 'sepal_width': '2.8', 'petal_length': '6.1', 'petal_width': '1.9', 'species': 'Iris-virginica'}
{'sepal_length': '7.9', 'sepal_width': '3.8', 'petal_length': '6.4', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '6.4', 'sepal_width': '2.8', 'petal_length': '5.6', 'petal_width': '2.2', 'species': 'Iris-virginica'}
{'sepal_length': '6.3', 'sepal_width': '2.8', 'petal_length': '5.1', 'petal_width': '1.5', 'species': 'Iris-virginica'}
{'sepal_length': '6.1', 'sepal_width': '2.6', 'petal_length': '5.6', 'petal_width': '1.4', 'species': 'Iris-virginica'}
{'sepal_length': '7.7', 'sepal_width': '3', 'petal_length': '6.1', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '6.3', 'sepal_width': '3.4', 'petal_length': '5.6', 'petal_width': '2.4', 'species': 'Iris-virginica'}
{'sepal_length': '6.4', 'sepal_width': '3.1', 'petal_length': '5.5', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6', 'sepal_width': '3', 'petal_length': '4.8', 'petal_width': '1.8', 'species': 'Iris-virginica'}
{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '5.4', 'petal_width': '2.1', 'species': 'Iris-virginica'}
{'sepal_length': '6.7', 'sepal_width': '3.1', 'petal_length': '5.6', 'petal_width': '2.4', 'species': 'Iris-virginica'}
{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '5.1', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'}
{'sepal_length': '6.8', 'sepal_width': '3.2', 'petal_length': '5.9', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '6.7', 'sepal_width': '3.3', 'petal_length': '5.7', 'petal_width': '2.5', 'species': 'Iris-virginica'}
{'sepal_length': '6.7', 'sepal_width': '3', 'petal_length': '5.2', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '6.3', 'sepal_width': '2.5', 'petal_length': '5', 'petal_width': '1.9', 'species': 'Iris-virginica'}
{'sepal_length': '6.5', 'sepal_width': '3', 'petal_length': '5.2', 'petal_width': '2', 'species': 'Iris-virginica'}
{'sepal_length': '6.2', 'sepal_width': '3.4', 'petal_length': '5.4', 'petal_width': '2.3', 'species': 'Iris-virginica'}
{'sepal_length': '5.9', 'sepal_width': '3', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'Iris-virginica'}
df=pd.Dataframes(dict1)
x=df.iloc[:,0:4].values
y=df.iloc[:,4].values
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy_score(y_pred,y_test)*100
st.title('iris prediction model')
st.write('---------------------------------------------------')
sepal_l=st.number_input(label='enter the sepal length')
sepal_w=st.number_input(label='enter the sepasl width')
petal_l=st.number_input(label='enter the petal length')
petal_w=st.number_input(label='enter the petal width')
pred=model.predict([[sepal_l,sepal_w,petal_l,petal_w]])
if st.button('predict result'):
     st.success(f'{pred}')
