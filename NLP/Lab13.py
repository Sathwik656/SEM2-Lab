import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

reviews = [
    "The smartphoe is okay for normal use.",
    "Worst smartphone i have ever used.",
    "Amazing performance and very smooth display.",
    "Battery life is terrible, very disappointed.",
    "The camera quality is fantastic, I love it!",
    "Not worth the price, very bad experience.",
    "Decent phone but could be better in terms of design.",
    "Great value for money, highly recommended!",
    "The phone overheats quickly and lags a lot.",
]

for review in reviews:
    score = sia.polarity_scores(review)
    if score['compound'] >= 0.05:
        sentiment = "Positive"
    elif score['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print("Review: ", review)
    print("Sentiment: ", sentiment)
    print("Scores: ", score)
    print("\n")