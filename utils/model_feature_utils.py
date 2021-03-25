import re
import string
from nltk.corpus import stopwords

sw = stopwords.words("english")
stop_words = [w.lower() for w in sw]

def word_count(row, stopwords = stop_words):
    '''
    This function will remove stopwords from the review and count the unqie
    remainning words
    '''
    row = str(row).lower().translate(str.maketrans('', '', string.punctuation)) # removes punctuation
    words = row.split(' ')
    word_count = len(set(words) - set(stopwords))
    return word_count

def encode_main_cat(x):
    '''
    This function will encode the category associated to main_cat variable
    '''
    
    encoding_dict = {
        'category_all electronics' : 0, 
        'category_amazon home' : 0,
        'category_arts crafts  sewing' : 0, 
        'category_automotive' : 0,
        'category_camera  photo' : 0, 
        'category_computers' : 0,
        'category_gps  navigation' : 0, 
        'category_home audio  theater' : 0,
        'category_office products' : 0, 
        'category_tools  home improvement' : 0,
        'category_toys  games' : 0, 
        'category_video games' : 0, 
    }
    
    if x in list(encoding_dict.keys()):
        encoding_dict[x] = 1
        b
    return list(encoding_dict.values())