# 2. Install an external module and use it to perform an operation of your interest.

# -> installation:- pip install pyjokes

import pyjokes

joke = pyjokes.get_joke()
print(joke)



# -> installation:- pip install pyttsx3
# Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.

import pyttsx3
pyttsx3.speak("I will speak this text")