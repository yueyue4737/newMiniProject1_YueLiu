# !/usr/bin/env/python3
# Copyright 2019 YueLiu liuyue2@bu.edu
# Program Goal: using Google NLP API to do sentiment analysis
# next step 1: avoid global variables
# next step 2: name the parameters in a stable way
# next step 3: use command line tool
# next step 4:put the function into a class, split it into 2 if necessary

# calling the Natural Language API by using client library
# import the Google client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account
import os
from sys import argv
# getting the credentials
credentials_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "[FILE_NAME].json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# setting up authentication in the cloud console
client = language.LanguageServiceClient(credentials=credentials)

def sentiment_analysis(file_name):
    """
    Sentiment Analysis by using Google Natural Language API
    :param file_name:
    :return: string-reaction
    """
    # fetch the file for analysis
    # sentiment analysis by the basic methods
    with open(file_name, 'r') as file:
        content = file.read()
    document = types.Document(content=content, type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # measure the tweets by using score and magnitude
    score = sentiment.score
    magnitude = sentiment.magnitude
    reaction = 'Neutral'
    if score > 0.3:
        reaction = 'Positive'
    elif score <= -0.3:
        reaction = 'Negative'
    else:
        if magnitude > 3:
            reaction = 'Mixed'
    return reaction

file_name = '' # file name with format
res = sentiment_analysis(file_name)
print(res)

# if __name__ == 'main':
#     file_name = ''
#     res = sentiment_analysis(file_name)
#     print(res)
