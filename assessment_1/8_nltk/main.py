"""
A script to work on the NLTK practical.
@author: ksuchak1999
data_created: 19/03/14
last_modified: 19/03/14
"""
# Imports
from time import sleep
import nltk
import requests

# Constants
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
with open('../../../GEOCODING_KEY') as f:
    API_KEY = f.readline().strip()

# Functions
def restrict(input_string, start_str=None, end_str=None):
    """
    Text parsing function to get substrings,
    based on substrings before an after.
    :param intput_string: string to be stripped down
    :param start_str:
    :param end_str:
    :returns: string that has been stripped down
    """
    # Type-checking
    if not isinstance(input_string, str):
        raise TypeError('inputString must be a string.')
    start_index = input_string.index(start_str) + len(start_str) if start_str else 0
    reduced_str = input_string[start_index:]
    end_index = reduced_str.index(end_str) if end_str else len(reduced_str)
    return reduced_str[:end_index]

def request_url(url):
    """
    A wrapper function for requesting a url.

    :param url: url of webpage to be requested.
    :returns: text of the requested url.
    """
    # Type-checking
    if not isinstance(url, str):
        raise TypeError('url must be a string.')

    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('Page request unsuccessful: status code {0}'.format(
            r.status_code))
    return r.text

def is_nnp(tagged_word):
    """
    A function to check if a tagged word really is a proper noun.
    :param tagged_word: A tagged word, (word, tag)
    :returns: boolean, true if npp else false
    """
    return tagged_word[0].isalpha() and not tagged_word[0].isupper()

def geocode_google(noun):
    """
    A function to geocode a noun using Google Maps Geocoding API.
    :param noun: The noun that we think might be a place.
    :returns: a dictionary of the geocoding information.
    """
    params = {'address': noun, 'key': API_KEY}
    r = requests.get(GOOGLE_MAPS_API_URL, params)
    res = r.json()
    if res['results']:
        return res

def geocode(noun):
    """
    A wrapper function to geocode a noun.
    :param noun: The noun that we think might be a place.
    :returns: A geodata dictionary.
    """
    geo = geocode_google(noun)
    if geo:
        result = geo['results'][0]
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        return geodata

# URLs
data_url = 'http://www.gutenberg.org/files/1321/1321-0.txt'

# Main
# Get poem by requesting full text and reducing to poem
full_text = request_url(data_url)
start_string = 'CONTENTS'
end_string = 'Line 415'
poem = restrict(full_text, start_string, end_string)
print(poem)

# Tokenise poem
tokens = nltk.word_tokenize(poem)
text = nltk.Text(tokens)

# Find 20 most common words
word_frequency = nltk.FreqDist(text)
print(word_frequency.most_common(20))

# Find 20 most common word lengths
word_length = nltk.FreqDist(len(w) for w in text)
print(word_length.most_common(20))

# Find all words over 10 letters long
long_words = [w for w in text if len(w) > 10]
print(long_words)

# POS tagging
tagged = nltk.pos_tag(text)
print(tagged)

# Get proper nouns
proper_nouns = [x for x in tagged if x[1] == 'NNP']
print(proper_nouns)

# Clean list
cleaned_nnp = [x[0] for x in proper_nouns if is_nnp(x)]
print('cleaned', list(set(cleaned_nnp)))

def geocode_all(nnp_list):
    for i, noun in enumerate(cleaned_nnp):
        if i % 25 == 0:
            print('Searched for {0} nouns, taking a quick break'.format(i))
            sleep(0.5)
        print(noun)
        x = geocode(noun)
        print(x)
