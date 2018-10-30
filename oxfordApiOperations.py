import requests
import json

# the file stores private parameter to call oxford dict. services
with open('config.json') as config_file:
    config = json.loads(config_file.read())

app_id = config["app_id"].replace(' ','')
app_key = config["app_key"].replace(' ','')
language = config["language"].replace(' ','')

def getWordList():
    '''
    return: this function returns a list. It includes 5000 word and word_id in a tuples
    [(word_id, word), (word_id, word)]
    '''
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + language + '/registers=Rare'

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    response_text = json.loads(r.text)

    word_list = []

    for word in response_text["results"]:
        word_list.append((word["id"],word["word"]))

    return word_list

def getWordDescription(word_id):
    '''
    :param word_id:
    :return: word description. It's a string.
    '''

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    response_text = json.loads(r.text)

    word_desc = response_text["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]

    return word_desc

