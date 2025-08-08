import re
from collections import Counter

from .document import Document


# Define a SocialMedia class that is a child of the `Document` class
class SocialMedia(Document):
    def __init__(self, text):
        # Call the parent class's constructor
        # Document.__init__(self, text) # the old way
        super().__init__(text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        # Extract hashtags directly from the original text
        hashtags = re.findall(r"#(\w+)", self.text)
        return Counter(hashtags)

    def _count_mentions(self):
        # Extract mentions directly from the original text
        mentions = re.findall(r"@(\w+)", self.text)
        return Counter(mentions)


# TS Version

# type WordCount = Record<string, number>;

# class SocialMedia extends Document {
#   constructor(
#     public text: string,
#     private _hashtagCounts: WordCount = this._countHashtags(),
#     private _mentionCounts: WordCount = this._countMentions()
#   ) {
#     super(text);
#     this._hashtagCounts = this._countHashtags();
#     this._mentionCounts = this._countMentions();
#   }

#   // Private methods for counting hashtags and mentions
#   private _countHashtags(): WordCount {
#     .....
#   }

#   private _countMentions(): WordCount {
#     ....
#   }

#   // Public getters to expose the counts
#   get hashtagCounts(): WordCount {
#     return {...this._hashtagCounts}; // Return copy to prevent mutation
#   }

#   get mentionCounts(): WordCount {
#     return {...this._mentionCounts}; // Return copy to prevent mutation
#   }
# }
