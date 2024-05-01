import sentiment

# Test with positive sentiment
text = "I love this product. It's amazing!"
result = sentiment.calculatesentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {result}")

# Test with negative sentiment
text = "This is the worst product I've ever used."
result = sentiment.calculatesentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {result}")

# Test with neutral sentiment
text = "This product is okay."
result = sentiment.calculatesentiment(text)
print(f"Text: {text}")
print(f"Sentiment: {result}")
