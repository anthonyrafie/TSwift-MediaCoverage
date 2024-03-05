import json
import math
from collections import defaultdict

# Read the JSON file
with open('final_data/category_counts.json', 'r', encoding='utf-8') as file:
    category_counts = json.load(file)

# Specify the number of top words for each category
num_words = 10  # Change this number as needed

# Calculate total number of categories
total_categories = len(category_counts)

# Function to calculate IDF
def calculate_idf(word):
    category_count = sum(1 for category in category_counts if word in category_counts[category])
    return math.log(total_categories / category_count)

# Compute TF-IDF scores
tf_idf_scores = defaultdict(dict)
for category, words in category_counts.items():
    for word, count in words.items():
        tf = count
        idf = calculate_idf(word)
        tf_idf_scores[category][word] = tf * idf

# Select top N words for each category
top_words = {category: sorted(words.keys(), key=lambda w: words[w], reverse=True)[:num_words]
             for category, words in tf_idf_scores.items()}

# Print the results
print(json.dumps(top_words, indent=4))