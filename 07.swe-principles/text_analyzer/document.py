# _ means private method

import re
from collections import Counter


class Document:
    """A class for text analysis

    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed set by `text` parameter
    """

    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()

    # converts text to lowercase and uses regex to find all alphanumeric "words"
    def _tokenize(self):
        return re.findall(r"\b\w+\b", self.text.lower())

    def _count_words(self):
        return Counter(self.tokens)


# TS version

# type WordCount = Record<string, number>

# class Document {
#   constructor(
#     public text: string,
#     private tokens: string[] = [],
#     private wordCounts: WordCount = {}
#   ) {
#     this.tokens = this._tokenize()
#     this.wordCounts = this._countWords()
#   }

#   // Private method to tokenize text
#   private _tokenize(): string[] {
#     // Find all alphanumeric "words" and convert to lowercase
#     const regex = /\b\w+\b/g
#     return this.text.toLowerCase().match(regex) || []
#   }

#   // Private method to count word frequencies
#   private _countWords(): WordCount {
#     const counts: WordCount = {}

#     for (const token of this.tokens) {
#       counts[token] = (counts[token] || 0) + 1
#     }

#     return counts
#   }

# 	Public getters (in python all class properties are public, but that's not a good TS practice)
#   get tokens(): string[] {
#     return [...this._tokens]; // Return copy to prevent mutation
#   }

#   get wordCounts(): WordCount {
#     return {...this._wordCounts}; // Return copy to prevent mutation
#   }

# }
