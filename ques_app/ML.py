from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

import pandas as pd

def Idator(dataset,post_data):
    print("Comming to Idator")
    #print(dataset)
    formatted_dataset=[]
    for i in dataset:
        temp=[]
        temp.extend((i['avg_time'],i['avg_marked'],i['ans_right'],i['avg_clicks'],i['stu_class']))
        formatted_dataset.append(temp)
    #print(formatted_dataset)
    names=['Average time to solve each questions','No of questions marked for review','No of questions right','Average no of clicks in each page']
##    for col in cols:
##        try:
##            dataset[col] = float(dataset[col])
##        except:
##            pass
##    print(dataset.values)
    df=pd.DataFrame(formatted_dataset)
    print(df.values)
    array = df.values
    array=array[1:]
    #print(array)
    X = array[:,0:4]
    Y = array[:,4]
    #print(X)
    #print(Y)
    knn = KNeighborsClassifier()
    knn.fit(X, Y)
    predictions = knn.predict(post_data)
    temp={}
    temp['knn']=predictions[0]
    print("predictions",predictions)
    #print(accuracy_score(Y_validation, predictions))
    #print(confusion_matrix(Y_validation, predictions))
    #print(classification_report(Y_validation, predictions))

    model = DecisionTreeClassifier()
    model.fit(X, Y)
    # make predictions
    predictions = model.predict(post_data)
    #prediction = model.predict([[2.8,15,18,180]])
    #print("prediction",prediction)
    # summarize the fit of the model
    print("predictions",predictions)
    temp['dtree']=predictions[0]
    return temp
    #print(accuracy_score(Y_validation, predictions))
    #print(confusion_matrix(Y_validation, predictions))
    #print(classification_report(Y_validation, predictions))
