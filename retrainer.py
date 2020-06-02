import requests
import numpy as np
data = requests.get("https://api.covid19api.com/world")
import pandas as pd
import pickle as pkl
df = pd.read_json(data.text)
feature = 'TotalConfirmed'
target = 'TotalDeaths'
trainX = train[feature]
trainy = train[target]
trainX = trainX.to_numpy().reshape(-1,1)
trainy = trainy.to_numpy().reshape(-1,1)
pkl.dump(model,open( "model.pkl", "wb" ))
