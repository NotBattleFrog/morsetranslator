#morse_translator.py
#ref : https://en.wikipedia.org/wiki/Morse_code
import time
import os 
import pyglet # require avbin : https://avbin.github.io/AVbin/Download.html

sound_path = os.getcwd()+r'\sounds'+"\\"
#dot (0.1s) and dash(0.3s) sound -> 600Hz
#gap testing (symbols,letters,words) (0.2,0.4,0.8)
dot = pyglet.media.StaticSource(pyglet.media.load(sound_path+"dot_sound.wav")) 
dash = pyglet.media.StaticSource(pyglet.media.load(sound_path+"dash_sound.wav")) 

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
# ^ -> Unknown
def toCode(word) :
    data = ''
    up_word = word.upper()
    for char in up_word:
        data += morse.get(char,'^') + ' '
    return data
          
def toWord(code) :
    data = ''
    splited = code.split()
    for char in splited :
            data += inverse_morse.get(char,'^')
    return data

def toSound(code):
   for i in code:
        if i == '.':
               dot.play()
               time.sleep(0.2)
        elif i == '-':
              dash.play()
              time.sleep(0.4)
        elif i == '|':
               time.sleep(0.8)
        else:
              time.sleep(0.4)
