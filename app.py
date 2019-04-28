# To make HTTP request to the Wikipedia article
import urllib.request
# To beautify the content and extract data from it
from bs4 import BeautifulSoup
# Wrapper around Wikipedia API
import wikipedia

# for word count using PySpark
import re, string
from pyspark import SparkContext


url = 'https://en.wikipedia.org/wiki/Machine_learning'

# Extract HTML content from given url
html = urllib.request.urlopen(url)
# Beautify the HTML content
soup = BeautifulSoup(html)

title = soup.find("h1", {"id": "firstHeading"})

# print(title.text)

# Will take the Machine Learning URL 
p = wikipedia.page(title.text)

# print(p.url)

# Will find the "Theory" subsection from the given Wikipedia article
subsectionContent = p.section("Theory")

print(subsectionContent)


file = open("wipedia-file.txt", "w")
file.write(subsectionContent)
file.close()

sc = SparkContext("local", "First App")

text_file = sc.textFile('wipedia-file.txt')

## Read the wikipedia content file and count words from it below:

# punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

# Contains all the punctuations
punc = string.punctuation
print(punc)

# To convert unicode to clean string and remove punctuations
def uni_to_clean_str(x):
    # To change from unicode to string
    converted = x.encode('utf-8')
    # To lowercase letters
    lowercased_str = x.lower()
    print("Lowercase str ", lowercased_str)
    # Replace '--' with ' ' (space)
    lowercased_str = lowercased_str.replace('--',' ')
    clean_str = lowercased_str.translate(punc) #Change 1
    print("Clean str ", clean_str)
    return clean_str


one_RDD = text_file.flatMap(lambda x: uni_to_clean_str(x).split())
one_RDD = one_RDD.map(lambda x: (x,1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)
# Will print first 55 keys
print(one_RDD.take(55))
print(type(one_RDD.take(55)))



