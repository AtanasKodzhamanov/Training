import pandas as pd
from textblob import TextBlob
import pandas as pd
from textblob import TextBlo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the news data and perform sentiment analysis
df = pd.read_csv("news_data.csv")
df["sentiment"] = df["headline"].apply(
    lambda x: TextBlob(x).sentiment.polarity)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    df["sentiment"], df["label"], test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train.to_numpy().reshape(-1, 1), y_train)

# Make predictions on the test set and calculate the accuracy
y_pred = model.predict(X_test.to_numpy().reshape(-1, 1))
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
