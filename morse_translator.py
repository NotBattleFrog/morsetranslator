#morse_translator.py
#ref : https://en.wikipedia.org/wiki/Morse_code
import time
import os 
import pyglet # require avbin : https://avbin.github.io/AVbin/Download.html

sound_path = os.getcwd()+r'\sounds'+"\\"
dot = pyglet.media.StaticSource(pyglet.media.load(sound_path+"dot_sound.ogg")) # 0.1s
dash = pyglet.media.StaticSource(pyglet.media.load(sound_path+"dash_sound.ogg")) # 0.3s
#time.sleep(0.1,0.3,0.7) # gap between (symbols,letters,words)
#dot = 0.1s , dash = 0.3s

def t(code):
    for char in code:
        if char == '.':
            dot.play()
            time.sleep(0.1)
        elif char == '-':
            dash.play()
            time.sleep(0.1)
        else:
            time.sleep(0.1)
                       
morse = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.' ,
    'S' : '...',
    'T' : '-', 
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-', 
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '!' : '-.-.--',
    ';' : '-.-.-',
    ':' : '---...',
    '/' : '-..-.',
    '-' : '-....-',
    "'" : '.----.',
    '(' : '-.--.',
    ')' : '-.--.-',
    '_' : '..--.-',
    '@' : '.--.-.',
    '&' : '.-...',
    '=' : '-...-',
    '+' : '.-.-.',
    '"' : '.-..-.',
    '$' : '...-..-',
    ' ' : '|'
    }

inverse_morse = {v:k for k,v in morse.items()}

def encode(word) :
    data = ''
    up_word = word.upper()
    for char in up_word:
        data += morse.get(char,'Unknown')+" "
    return data
          
def decode(code) :
    data = ''
    splited = code.split()
    for char in splited :
            data += inverse_morse.get(char,'Unknown')
    return data




