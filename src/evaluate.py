import pandas as pd, pickle, json
from sklearn.model_selection import train_test_split
df = pd.read_csv("data/clean.csv")
_, test = train_test_split(df, test_size=0.2, random_state=0)
model = pickle.load(open("model.pkl", "rb"))
acc = (model.predict(test.text) == test.label).mean()
json.dump({"accuracy": round(acc, 3)}, open("metrics.json", "w"))
print(acc)
