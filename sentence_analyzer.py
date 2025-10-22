from sklearn.feature_extraction.text import CountVectorizer  # convert text → numeric features
from sklearn.naive_bayes import MultinomialNB               # simple text classification AI model

# Short training data — add your own phrases to improve accuracy!
texts = ["I love this", "I hate this", "This is okay"]
labels = ["positive", "negative", "neutral"]

vectorizer = CountVectorizer()               # create object to turn words into numbers
X = vectorizer.fit_transform(texts)          # learn vocabulary and transform training data
model = MultinomialNB()                      # create the classifier
model.fit(X, labels)                          # train the model on our examples

print("🤖 SentimentBot: Type something (or 'quit' to stop).")
while True:
    user = input("You: ")                    # get user input
    if user.lower() == "quit": break         # exit condition
    X_test = vectorizer.transform([user])    # convert user text into numeric features
    prediction = model.predict(X_test)[0]    # predict the sentiment
    print("🤖 SentimentBot:", prediction)    # show result
