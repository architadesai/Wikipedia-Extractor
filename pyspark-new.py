import re, string
from pyspark import SparkContext

sc = SparkContext("local", "First App")

text_file = sc.textFile('text.txt')

print(text_file)

# first 5 elements of the RDD
print(text_file.take(5))


# punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

# Contains all the punctuations
punc = string.punctuation
print(punc)

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

print(uni_to_clean_str("ac def. gh"))

one_RDD = text_file.flatMap(lambda x: uni_to_clean_str(x).split())
one_RDD = one_RDD.map(lambda x: (x,1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)
print(one_RDD.take(55))
