import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns


url = 'https://raw.githubusercontent.com/Data-Science-East-AFrica/Exploratory-Data-Analysis-Using-Python/main/train.csv'
train=pd.read_csv(url)

# train.info()
# train.head()
# train.describe()

# train.isnull()
# train.shape()
# print(train)
print(sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis'))