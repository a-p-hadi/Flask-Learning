import pandas as pd
import numpy as np

df_train = pd.read_csv('http://dataqueez.ir/files/questions/22/Train.csv')
df_test = pd.read_csv('http://dataqueez.ir/files/questions/22/Test.csv')
df_train.head()

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

df_train_ = outlier_management(df_train.iloc[:,:-1])
df_train_['Income'].hist(bins=50)

df_train_ = outlier_management(df_train.iloc[:,:-1])

df_train_.drop(['Count_3.6_months_late', 'Count_6.12_months_late', 'Count_more_than_12_months_late'], axis=1, inplace=True)
df_test.drop(['Count_3.6_months_late', 'Count_6.12_months_late', 'Count_more_than_12_months_late'], axis=1, inplace=True)

def mv_management_mod(x):
    dfc = x
    mod = dfc.mode()
    dfc = dfc.fillna(mod[0])
    return dfc

def mv_management_mean(x):
    dfc = x
    mean = dfc.mean()
    dfc = dfc.fillna(mean[0])
    return dfc

df_train_['application_underwriting_score'] = mv_management_mod(df_train_['application_underwriting_score'])
df_test['application_underwriting_score'] = mv_management_mod(df_test['application_underwriting_score'])

from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def encoder(x, t):
    df = x.copy()
    dt = t.copy()
    LE = LabelEncoder()
    for c in df.columns:
        if df[c].dtypes=='object':
            df[c] = LE.fit_transform(df[c])
            dt[c] = LE.transform(dt[c])
    return df, dt

df_train_en, df_test_en = encoder(df_train_, df_test)

X = df_train_en
Y = df_train['renewal']

MMS = MinMaxScaler()
XNorm = pd.DataFrame(MMS.fit_transform(X), columns=X.columns)
df_test_Norm = pd.DataFrame(MMS.transform(df_test_en), columns=df_test_en.columns)

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score
skf = StratifiedKFold(n_splits=10)
models = dict()


from sklearn.naive_bayes import GaussianNB
GNB = GaussianNB()
pred = cross_val_predict(GNB, XNorm, Y, cv=skf)

best_model, (best_score, best_param) = max(results.items(), key=lambda x: x[1][0])
print(best_score, best_param)

best_model_ = best_model
best_model_.fit(XNorm, Y)
pred = best_model_.predict(df_test_Norm)



