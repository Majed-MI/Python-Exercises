# News Reading Jarvis
# function of speak with str value
def speak(str):
    # pywin32 module calling and import dispatch to voice on
    from win32com.client import Dispatch
    # voice on syntax
    speak = Dispatch("SAPI.spVoice")
    # voice on for the str values
    speak.speak(str)

# only applicable for the following functions
if __name__ == '__main__':
    # importing modules
    import requests
    import json
    # taking the url from newsapi
    url = ("https://newsapi.org/v2/top-headlines?"
           "sources=bbc-news&"
           "apiKey=c7ad330bf13c4d36be48d0813f09e088")
    # getting the request from the url
    response = requests.get(url)
    # getting the request in text format
    text = response.text
    # converting string to dictionary format
    my_json = json.loads(text)
    # newsapi stores only 10 news so range is 0 to 10
    for i in range(0,11):
        # speak function calling with values of dictionary from the news and voice for the title
        speak(my_json['articles'][i]['title'])
