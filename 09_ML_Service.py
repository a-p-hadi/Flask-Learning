import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r'C:\train.csv')
df_ = df.copy()

def outlier_management(x):
    df = x.copy()
    for column in df.columns:
        if (df[column].dtype!=object):
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            df[column] = df[column].apply(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)
            # df[column] = df[column].clip(lower_bound, upper_bound)
    return df

df_train_ = outlier_management(df_.iloc[:,:-1])

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
df_train_nd = imputer.fit_transform(df_train_)
df_train = pd.DataFrame(df_train_nd, columns=df_train_.columns)

import pickle
filename = 'Miss_model.pkl'
pickle.dump(imputer, open(filename, 'wb'))

from sklearn.preprocessing import MinMaxScaler
X = df_train
Y = df_['Outcome']
MMS = MinMaxScaler()
XNorm = pd.DataFrame(MMS.fit_transform(X), columns=X.columns)
filename = 'MMS_model.pkl'
pickle.dump(MMS, open(filename, 'wb'))

from sklearn.preprocessing import MinMaxScaler
X = df_train
Y = df_['Outcome']
MMS = MinMaxScaler()
XNorm = pd.DataFrame(MMS.fit_transform(X), columns=X.columns)
filename = 'MMS_model.pkl'
pickle.dump(MMS, open(filename, 'wb'))

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score
skf = StratifiedKFold(n_splits=10)
from sklearn.neural_network import MLPClassifier
MLP = MLPClassifier(random_state=3657, early_stopping=True, n_iter_no_change=5)
MLP_Par = [
            {
                'hidden_layer_sizes':[(a, b) for a in range(6, 8) for b in range(8, 10)],
                'max_iter':[20, 50, 90],
                'learning_rate_init':[0.08, 0.1, 0.15],
                'learning_rate':['invscaling', 'constant'],
                'activation':['tanh', 'relu', 'logistic']
            }
          ]
models[MLP] = MLP_Par
GS = GridSearchCV(model, param_grid=Param, cv=skf, scoring='f1_macro')
GS.fit(XNorm, Y)
best_model = GS.best_estimator_


filename = 'Pred_model.pkl'
pickle.dump(best_model, open(filename, 'wb'))

