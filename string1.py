def hello_name(name):
    '''
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    '''
    output = 'Hello {}!'.format(name)
    return output

def make_abba(a, b):
    '''
    Given two strings, a and b, return the result of putting them together in the order abba, 
    e.g. "Hi" and "Bye" returns "HiByeByeHi".
    '''
    return a + b + b + a

def make_tags(tag, word):
    '''
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    '''
    return "<{}>{}</{}>".format(tag,word,tag)

def make_out_word(out, word):
    '''
    Given an "out" string length 4, such as "<<>>", and a word, 
    return a new string where the word is in the middle of the out string
    '''
    return out[:2] + word + out[2:]

def extra_end(string):
    '''
    Given a string, 
    return a new string made of 3 copies of the last 2 chars of the original string. 
    '''
    end = string[-2:]
    return end*3

def first_two(string):
    '''
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is
    '''
    if len(string) < 2:
        return string
    else:
        return string[:2]

def first_half(string):
    '''
    Given a string of even length, return the first half.
    So the string "WooHoo" yields "Woo". 
    '''
    half = (len(string)/2)
    return string[:half]
