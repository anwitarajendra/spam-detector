import nltk
from nltk.tokenize import word_tokenize

# Re-download in a fresh session
nltk.download('punkt')

# Test
print(word_tokenize("This is a test sentence."))
