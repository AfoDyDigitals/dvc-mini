import pandas as pd, pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
df = pd.read_csv("data/clean.csv")
train, _ = train_test_split(df, test_size=0.2, random_state=0)
model = make_pipeline(CountVectorizer(), LogisticRegression())
model.fit(train.text, train.label)
pickle.dump(model, open("model.pkl", "wb"))
