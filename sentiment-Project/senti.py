from textblob import TextBlob

blob=TextBlob("It ios booad")
print(blob.sentiment.polarity)
print(blob.correct())
print(blob.detect_language())


