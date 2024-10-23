import tweepy
from textblob import TextBlob
import pandas as pd

# Autenticação no Twitter
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SEU_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Autenticando com o Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Define hashtag e número de tweets a serem analisados
hashtag = "#AIinMarketing"
num_tweets = 100

# Função para realizar análise de sentimento
def get_tweet_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity == 0:
        return 'neutro'
    else:
        return 'negativo'

# Coletar tweets com a hashtag
tweets_data = []
for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, lang="pt", tweet_mode='extended').items(num_tweets):
    parsed_tweet = {}
    parsed_tweet['usuario'] = tweet.user.screen_name
    parsed_tweet['tweet'] = tweet.full_text
    parsed_tweet['sentimento'] = get_tweet_sentiment(tweet.full_text)
    tweets_data.append(parsed_tweet)

# Criar dataframe para visualização dos resultados
df = pd.DataFrame(tweets_data)

# Exibir resumo de sentimentos
print(df['sentimento'].value_counts())

# Exibir os primeiros 5 tweets coletados
print(df.head())
