# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 00:39:00 2021

@author: 4471082
"""

# Load labraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Breast Cancer Data Exploration
from sklearn.datasets import load_breast_cancer

def main():
    # Get both data and target
    breast = load_breast_cancer()
    
    # Get data only
    breast_data = breast.data
    print('breast_data shape:',breast_data.shape)
    print(breast_data)
    
    # Take a look at target values even if we will not use it
    breast_labels = breast.target
    print('breast_labels shape:',breast_labels.shape)
    print(breast_labels)
    
    # Get the feature names
    features = breast.feature_names
    print(features)
    
    # Convert to DataFrame
    breast_dataset = pd.DataFrame(breast_data)
    breast_dataset.columns = features
    print(breast_dataset)
    
    # Add Label column
    breast_dataset['label'] = breast_labels.T # breast_labels transpose before adding to dataframe, to get it vertical
    print(breast_dataset)
    
    # Since the original labels are in 0,1 format, we will change the labels to benign and malignant using .replace function.
    # We will use inplace=True which will modify the dataframe breast_dataset.
    breast_dataset['label'].replace(0, 'Benign',inplace=True)
    breast_dataset['label'].replace(1, 'Malignant',inplace=True)
    print(breast_dataset.tail())
    
    from sklearn.preprocessing import StandardScaler
    x = breast_dataset.loc[:, features].values
    x = StandardScaler().fit_transform(x) # normalizing the features
    
    print(x.shape)
    
    # Let's check whether the normalized data has a mean of zero and a standard deviation of one.
    print(np.mean(x),np.std(x))
    
    # Let's convert the normalized features into a tabular format with the help of DataFrame.
    feat_cols = ['feature' + str(i) for i in range(x.shape[1])]
    normalised_breast = pd.DataFrame(x,columns=feat_cols)
    print(normalised_breast.tail())
    
    from sklearn.decomposition import PCA
    pca_breast = PCA(n_components=2)
    principalComponents_breast = pca_breast.fit_transform(x)
    
    # Next, let's create a DataFrame that will have the principal component values for all 569 samples.
    principal_breast_Df = pd.DataFrame(data = principalComponents_breast
             , columns = ['principal component 1', 'principal component 2'])
    principal_breast_Df.tail()
    
    print('Explained variation per principal component: {}'.format(pca_breast.explained_variance_ratio_))
    
    plt.figure()
    plt.figure(figsize=(10,10))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=14)
    plt.xlabel('Principal Component - 1',fontsize=20)
    plt.ylabel('Principal Component - 2',fontsize=20)
    plt.title("Principal Component Analysis of Breast Cancer Dataset",fontsize=20)
    targets = ['Benign', 'Malignant']
    colors = ['r', 'g']
    for target, color in zip(targets,colors):
        indicesToKeep = breast_dataset['label'] == target
        plt.scatter(principal_breast_Df.loc[indicesToKeep, 'principal component 1']
               , principal_breast_Df.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)

    plt.legend(targets,prop={'size': 15})
    plt.show()
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    