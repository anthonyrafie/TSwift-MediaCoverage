import json
import string
import requests
import collections 

#Function to download and return stop words
def get_stop_words(url):
    response = requests.get(url)
    return set(response.text.split())

#Stop words URL
stop_words_url = "https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt"
stop_words = get_stop_words(stop_words_url)

#Load the JSON file
file_path = 'final_data/category_coded_500.json'
with open(file_path, 'r', encoding='utf-8') as file:
    articles = json.load(file)

#Initialize word counts
word_counts = collections.defaultdict(lambda: collections.defaultdict(int))

#Function to process text
def process_text(category, text):
    # Replace punctuation with spaces and split into words
    text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    words = text.lower().split()

    # Count words
    for word in words:
        if word.isalpha() and word not in stop_words:
            word_counts[category][word] += 1

#Process each article
for article in articles:
    category = article['category']
    process_text(category, article['title'])
    process_text(category, article['description'])

#Filter words with frequency less than 5
#for category in word_counts:
#    word_counts[category] = {word: count for word, count in word_counts[category].items() if count >= 5}

#Write to JSON file
output_file = 'category_counts.json'
with open(output_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(word_counts, jsonfile)

print(f"Word counts written to {output_file}")