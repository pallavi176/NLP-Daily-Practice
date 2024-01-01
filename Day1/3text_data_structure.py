# Q3: Explore text data structures in Python

# Explore Text Data Structures in Python:
# In Python, text is primarily handled with the str (string) data type, which is immutable and can store sequences of Unicode characters.

#1. String Operations: Basic operations include concatenation, slicing, and transformation:
greeting = "Hello"
audience = "World"
full_greeting = greeting + ", " + audience + "!"  # Concatenation: "Hello, World!"
print(greeting)
print(audience)
print(full_greeting)

#2. String Methods: Strings come with a variety of methods for searching, splitting, and modifying text:
text = "natural language processing"
words = text.split()  # ['natural', 'language', 'processing']
capitalized = text.title()  # 'Natural Language Processing'
print(text)
print(words)
print(capitalized)

#3. String Formatting: Python provides several ways to format strings, such as f-strings for easy interpolation:
name = "GPT-4"
formatted_string = f"The latest model is {name}."  # "The latest model is GPT-4."
print(formatted_string)

#4. Regular Expressions: For more complex patterns and text manipulations, the re module allows for sophisticated searching and replacing:
import re
text = "The price is 100 dollars."
numbers = re.findall(r'\d+', text)  # ['100']
print(text)
print(numbers)

#5. Text Encoding: Text in Python is handled as Unicode, but it can be encoded to bytes for storage or transfer:
text = "Hello, World!"
encoded_text = text.encode('utf-8')  # b'Hello, World!'
print(text)
print(encoded_text)

#6. Data Structures for Text: Larger structures such as lists, dictionaries, and DataFrames from the pandas library are often used to store and manipulate text data in structured forms.
# Examples of how larger data structures such as lists, dictionaries, and pandas DataFrames can be used to store and manipulate text data in Python:
#6.1. Lists: Lists in Python can store a collection of strings. This is useful for keeping track of words, sentences, or any collection of text elements.
# A list of strings representing different types of NLP tasks
nlp_tasks = ['tokenization', 'lemmatization', 'named entity recognition', 'sentiment analysis']

# Adding an item to the list
nlp_tasks.append('machine translation')

# Accessing an element
print(nlp_tasks[0])  # Output: 'tokenization'

# Iterating through the list
for task in nlp_tasks:
    print(task)

#6.2. Dictionaries: Dictionaries allow us to store data in key-value pairs. This is extremely useful for working with text data that has some form of natural association, 
# like word counts or mapping words to their meanings.
# A dictionary to count the occurrence of words in a sentence
sentence = "the cat sat on the mat the cat has a hat"
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(sentence)
print(word_count)

#6.3. Pandas DataFrames: Pandas DataFrames are great for tabular data. They are particularly well-suited for handling large datasets, such as a corpus of documents, 
# where each row can represent a document and columns can represent different features of the text, such as the raw text, the author, the date published, etc.
import pandas as pd

# A DataFrame to store information about various books
data = {
    'Title': ['To Kill a Mockingbird', '1984', 'The Great Gatsby'],
    'Author': ['Harper Lee', 'George Orwell', 'F. Scott Fitzgerald'],
    'Year': [1960, 1949, 1925]
}

books_df = pd.DataFrame(data)

# Accessing data
print(books_df['Title'])  # Output: Series with the titles of the books

# Adding a new column
books_df['Word Count'] = [100, 200, 300]  # Pretend word counts

print(books_df)

#7. Let's delve into more specific examples of handling and analyzing text data with lists, dictionaries, and pandas DataFrames.
#7.1.Using Lists for Text Data: Lists can be particularly useful for storing sequences of text data such as lines in a file or tokens (words) from a sentence.
# Imagine we have a list of sentences from a paragraph
sentences = [
    "Natural language processing enables computers to understand human language.",
    "Machine learning models can be trained to perform tasks like translation.",
    "The field of NLP is evolving rapidly with advances in AI research."
]

# We can tokenize each sentence into words
tokenized_sentences = [sentence.split() for sentence in sentences]

# Printing out the tokenized sentences
for token_list in tokenized_sentences:
    print(token_list)

#7.2. Using Dictionaries for Text Data: Dictionaries are useful for mapping keys to values, which is a common task in text processing. 
# They're often used for tasks like creating a word-to-index mapping which is essential for many machine learning models.
# A dictionary mapping words to their index (useful for text analysis)
word_to_index = {word: idx for idx, word in enumerate(set(" ".join(sentences).split()))}
# Accessing the index of a particular word
print(word_to_index["NLP"])  # Output: the index of "NLP" in the dictionary
print(word_to_index)

#7.3. Using Pandas DataFrames for Text Data: DataFrames are powerful for handling tabular data. They can hold various types of data, including text, 
# and support a wide range of operations on the data.

import pandas as pd

# Creating a DataFrame from a list of dictionaries (often how data is ingested from databases or APIs)
tweet_data = [
    {"user": "user1", "tweet": "Love learning about AI!", "timestamp": "2024-01-01"},
    {"user": "user2", "tweet": "Natural language processing is fascinating.", "timestamp": "2024-01-02"},
    {"user": "user3", "tweet": "How do machines understand language?", "timestamp": "2024-01-03"}
]

tweets_df = pd.DataFrame(tweet_data)

# Adding a column for word count in each tweet
tweets_df['word_count'] = tweets_df['tweet'].apply(lambda x: len(x.split()))

# Aggregating data - for example, count tweets by user
tweet_counts = tweets_df['user'].value_counts()

# Accessing the DataFrame
print(tweets_df)
print("\nTweet counts by user:")
print(tweet_counts)

