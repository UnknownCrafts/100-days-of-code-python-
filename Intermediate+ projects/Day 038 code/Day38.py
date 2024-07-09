# Attempt at making a local natural langauge powered workout tracker
# Both versions require the internet for uploading to google sheets its just this version has the NLP occur on device via regex and tokenization

import datetime
import gspread
import re
import nltk
from nltk.tokenize import word_tokenize

#Google Sheets OAuth using google cloud
gc = gspread.oauth(
    credentials_filename='credentials.json',
)

sh = gc.open("My Workouts (Python Controlled)")

print(sh.sheet1.get('A1'))



# Download NLTK resources if not already available
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = input("what did you do today? ")

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform Part-of-Speech tagging
tagged_tokens = nltk.pos_tag(tokens)

# Define regular expressions for matching patterns
exercise_verbs = [
    'run', 'ran', 'cycle', 'cycled', 'swim', 'swam', 'walk', 'walked', 'jog', 'jogged', 'lift', 'lifted',
    'yoga', 'stretch', 'stretched', 'hike', 'hiked', 'climb', 'climbed', 'dance', 'danced', 'row', 'rowed', 'biked'
]
exercise_pattern = re.compile(r'\b(?:' + '|'.join(exercise_verbs) + r')\b', re.IGNORECASE)
distance_pattern = re.compile(r'\b\d+k\b', re.IGNORECASE)
duration_pattern = re.compile(r'\bfor\s\d+\s(minutes?|hours?|mins?|hrs?)\b', re.IGNORECASE)

# Initialize variables for storing extracted information
exercises = []
durations = []

# Temporary storage for current exercise
current_exercise = ""

# Iterate over tokens to extract information
for i, (token, tag) in enumerate(tagged_tokens):
    if exercise_pattern.match(token):
        if current_exercise:
            exercises.append(current_exercise)
        current_exercise = token
    elif distance_pattern.match(token):
        current_exercise += ' ' + token
    elif duration_pattern.match(' '.join(tokens[i:i+3])):
        duration_match = duration_pattern.match(' '.join(tokens[i:i+3]))
        if duration_match:
            durations.append(duration_match.group())
            i += 2  # Skip the next two tokens as they are part of the duration

if current_exercise:
    exercises.append(current_exercise)

# Clean up the duration strings
durations = [re.sub(r'for\s', '', duration) for duration in durations]

# Example output
print("Exercises:", exercises)
print("Durations:", durations)
