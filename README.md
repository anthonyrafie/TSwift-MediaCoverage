## TSwift-MediaCoverage

# Project Overview
This project conducts a comprehensive analysis of the media coverage surrounding Taylor Swift, focusing on 500 North American news articles. The objective is to categorize the coverage into seven distinct topics, highlighting the media's focus on Swift's relationships, personal life, and public appearances.

# Methodology
The analysis involved categorizing each article into one of seven predefined topics, assessing the tone of the coverage, and identifying prevalent themes across the dataset.

1. Data Collection: The first step involved gathering 500 news articles from North American media outlets using newsapi.py. These articles were specifically selected to cover a broad period and include a variety of sources to ensure a comprehensive analysis.

2. Preprocessing: Each article underwent preprocessing to clean the text for analysis. This included removing any non-textual elements, standardizing formatting, and ensuring consistency across the dataset.

3. Topic Categorization: The core of the project was categorizing each article into one of seven topics related to Taylor Swift. A typology was first built to define these topics, which were:
  - Music Career and Achievements
  - Public Appearances and Celebrity Interactions
  - Media and Entertainment Industry Influence
  - Relationships and Personal Life
  - Cultural Impact and Fan Dynamics
  - Business Ventures and Endorsements
  - Fashion, Style, and Lifestyle
Once the typology was built, an open-coding was conducted, manually assigning a category to each article, as can be seen in category_coded_500.json.

4. Thematic Analysis: The next step involved identifying prevalent themes within each topic category. This was done by computing the word counts for each word present in a category using category_counts.py. Then, once the counts were available, a TF-IDF was used to extract the 10 most prevalent themes for each category using tf_idf.py, which can be seen in top_words.json.

5. Tone Analysis: After categorization and thematic analysis, the tone of each article was assessed with another open-coding, identifying whether the coverage was positive, negative, or neutral.


# Findings
The topics with the most articles by far were first 'Relationships and Personal Life', comprised of 232 out of 500 articles, and second the 'Public Appearances and Celebrity Interactions', with 161 articles. Both of these formed over 78% of the dataset, around 48% and 32% respectively. In terms of overall tone, the articles came out to be overall positive, with 314 Positive articles (over 62%), 29 Negative articles (5.8%), and 157 Neutral articles (over 34%). These proportions were then evaluated for each topic, the topic with the most proportionately positive articles being 'Business Ventures and Endorsements', having 100% of its articles being positive. The topic with the most proportionately negative articles was 'Cultural Impact and Fan Dynamics', these sentiments forming almost 14% of the topic’s articles. Lastly, the most relatively neutral topic was 'Media and Entertainment Industry Influence', with over 46% of its articles being neutral.

# Conclusion
The media's portrayal of Taylor Swift in North America is largely favorable, with a focus on her success, personal growth, and positive contributions to the entertainment industry.
