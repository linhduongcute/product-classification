import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

def clean_text(text):
    text = text.lower() 
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text) 
    return text

train['clean_product_name'] = train['product_name'].apply(clean_text)
test['clean_product_name'] = test['product_name'].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    train['clean_product_name'], train['label'], test_size=0.2, random_state=42
)
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = SVC(kernel='linear')
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))

X_test = test.drop(columns = ["product_name", "url_thumbnail", "url"])
X_test_tfidf = vectorizer.transform(test["clean_product_name"])
test_predictions = model.predict(X_test_tfidf)

submission = pd.DataFrame({"ID": test["ID"], "label": test_predictions})
submission.to_csv("submission.csv", index=False)

