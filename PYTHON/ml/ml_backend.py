import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

import constants

train = constants.train_file


def clean_dataframes(df_train):
    to_repl = 'Kharif     '
    val = 'Autumn     '
    to_repl2 = 'Rabi       '
    val2 = 'Winter     '
    df_train['Yield_per_area'] = df_train['Production'] / df_train['Area']
    df_train.replace(to_replace=to_repl, value=val, inplace=True)
    df_train.replace(to_replace=to_repl2, value=val2, inplace=True)
    return df_train


def get_train_test_kaggle(df_in, features):
    X_train = df_in[features]
    y_train = df_in.Yield_per_area
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=1)
    return X_train, X_test, y_train, y_test


def accuracy(y_test_diff, error=25):
    total_len = len(y_test_diff)
    print(total_len)

    correct_len = len(y_test_diff.loc[y_test_diff <= error])
    print(correct_len)

    accuracy = (correct_len * 100 / total_len)
    print("Accuracy: ", accuracy)

    return accuracy


def get_prediction(model, test_1, features, area):
    columns = list(features)
    test = pd.DataFrame(index=[0], columns=columns)
    test = test.fillna(0)
    for column in test_1.keys():
        test[column] = test_1[column]
    X_test = np.array(test)
    pred = model.predict(X_test)
    print("Prediction on test", pred)
    return pred

def load_data():
    df_yield = pd.read_csv(train)
    df_yield = clean_dataframes(df_yield)

    df_yield1 = pd.get_dummies(df_yield, columns=['Season', 'Crop', 'District_Name', 'State_Name'], drop_first=True)

    df_yield1 = df_yield1[:5000]

    non_numeric = ['Id','State_Name','District_Name','Crop_Year','Season','Crop', 'Area', 'Production', 'Yield_per_area']
    features = list(set(df_yield1.columns) - set(non_numeric))
    
    return df_yield1, features


def get_model(df_yield1, features):

    #df_yield1, features = load_data()

    X_train, X_test, y_train, y_test = get_train_test_kaggle(df_yield1, features)

    # Normalization
    scaler = preprocessing.MinMaxScaler().fit(X_train)
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    y_train1 = np.log1p(y_train)

    reg = RandomForestRegressor(n_estimators=200, criterion='mse', random_state=1, n_jobs=10, verbose=1)

    reg.fit(X_train,y_train)
    return reg

def test_model(reg, X_test, y_test):
    # Make predictions using the testing set
    y_pred = reg.predict(X_test)

    y_test_diff = (y_pred - y_test).abs()*100/y_test

    # print results
    accuracy(y_test_diff)

    # prediction
    test_1 = {'Crop_Urad': 1, 'State_Name_Meghalaya': 1}
    area = 1000
    get_prediction(reg, test_1, features, area)
    return



if __name__=="__main__":
    df, features = load_data()
    reg = get_model(df, features)
    print(df.head())
    print(len(features))




