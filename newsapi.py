import requests
import json

# NewsAPI key
api_key = '84c5cd369a764b259e290bc71e3c6d68'

# Specify the base URL for the NewsAPI
base_url = 'https://newsapi.org/v2/everything'

# Specify the parameters for the API request
params = {
    'q': 'Taylor Swift',
    'searchIn': "title,description",
    'language': 'en',
    'apiKey': api_key,
    "domains": "cosmopolitan.com"      # INSERT DOMAINS HERE   WATCH OUT, MAKE SURE OUTPUT FILE IS NAMED TEST.JSON WHEN TESTING FOR DOMAINS
}


# Make the API request
response = requests.get(base_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON
    data = json.loads(response.text)

    # Check if articles are available in the response
    if 'articles' in data:
        articles = data['articles']

        # List to store article data
        article_data = []

        # Process the articles
        for article in articles:
            # Extract relevant information from each article
            title = article['title']
            description = article['description']
            url = article['url']
            published_at = article['publishedAt']
            source_name = article.get('source', {}).get('name', '')

            # Store the information in a dictionary
            article_info = {
                'title': title,
                'description': description,
                'url': url,
                'published_at': published_at,
                'source_name': source_name,
            }

            # Add the dictionary to the list
            article_data.append(article_info)

        # Print the number of entries
        num_entries = len(article_data)
        print(f"Number of entries: {num_entries}")

        # Save the data to a JSON file
        with open('test.json', 'w') as json_file:
            json.dump(article_data, json_file, indent=2)

else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
