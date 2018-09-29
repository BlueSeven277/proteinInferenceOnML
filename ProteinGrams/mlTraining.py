import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,average_precision_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split,cross_val_score

df = pd.read_csv('sigma_features.csv')
print df.head()
print df.describe()
df = df.drop('pID',axis=1)
plt.figure(figsize=(6,4))
sns.countplot(df['result'], hue = df['two'], palette = 'rainbow', edgecolor = [(0,0,0), (0,0,0)])
#plt.show()

# Split the dataframe into features (X) and labels(y)
frames = [df, df, df, df, df, df, df, df, df, df]
df= pd.concat(frames)
X = df.drop('result', axis=1)
y = df['result']

# Split the dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

feature_select = SelectKBest(chi2, k = 7)  #finding the top 6 best features
feature_select.fit(X_train, y_train)
score_list = feature_select.scores_
top_features = X_train.columns
uni_features = list(zip(score_list, top_features))
print(sorted(uni_features, reverse=True)[0:7])

#add more items of result==1 to training set
# dfone = df[df['result'] == 1]
# dfone = dfone.drop('result', axis=1)
#dfone = df.ix[df.result == 1]
# frames = [X_train, dfone]
# X_train = pd.concat(frames)
#
X_train_1 = feature_select.transform(X_train)
X_test_1 = feature_select.transform(X_test)

#random forest classifier with n_estimators=10 (default)
rf_clf = RandomForestClassifier()
rf_clf.fit(X_train_1,y_train)

rf_pred = rf_clf.predict(X_test_1)

accu_rf = accuracy_score(y_test, rf_pred)
print('Accuracy is: ',accu_rf)
pre=average_precision_score(y_test, rf_pred)
print ('Precision(TP/TP+FP) is: ',pre)
#cm_1 = confusion_matrix(y_test, rf_pred)
#sns.heatmap(cm_1, annot=True, fmt="d")
#plt.show()

#LogisticRegression

classifier=LogisticRegression()
classifier.fit(X_train_1,y_train)
scores=cross_val_score(classifier,X_train_1,y_train,cv=5)
print 'LogisticRegression:',np.mean(scores),scores

def precision_score(y_true, y_pred):
    return ((y_true==1)*(y_pred==1)).sum()/(y_pred==1).sum()