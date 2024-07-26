import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from datetime import datetime
from sklearn.decomposition import PCA
import os

import joblib

def predictData(time, amount, an, cn, cvv, doe, cs):
    data = {
        'Time': [100, 90, 60],
        'Amount': [10000, 20000, 50000],
        'Account Number': [1234567890123456, 5789456123789456, 123478978977974546],
        'Card Number': [213456789456, 8894545479789, 7895461200368],
        'CVV': [123, 456, 963],
        'Date of Expiry': ['1220', '0824', '1126'],
        'Credit Score': [400, 800, 300]
    }

    data['Time'].append(time)
    data['Amount'].append(amount)
    data['Account Number'].append(an)
    data['Card Number'].append(cn)
    data['CVV'].append(cvv)
    data['Date of Expiry'].append(doe)
    data['Credit Score'].append(cs)

    df = pd.DataFrame(data)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    val = np.array(X_scaled[-1]).reshape(1, -1)

    model = joblib.load(os.path.join('./FraudDetection/CC.pkl'))

    # print(model.predict(val))
    output = model.predict(val)

    return output