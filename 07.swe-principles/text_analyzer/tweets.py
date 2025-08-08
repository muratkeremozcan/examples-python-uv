from .social_media import SocialMedia

# Document (defines text property)
#    ↓
# SocialMedia (inherits text from Document)
#    ↓
# Tweets (inherits text from SocialMedia which got it from Document)


# Note I would not use multi-level inheritance in the real world
# Most modern programming emphasizes:
# Composition over inheritance
# Shallow inheritance hierarchies (one level is often enough)
# Interface-based design
# Functional approaches that avoid class hierarchies altogether


class Tweets(SocialMedia):
    """A class for Twitter-specific text analysis that extends SocialMedia

    Tweets is a specialized SocialMedia class that adds retweet functionality
    """

    def __init__(self, text):
        # Call parent's constructor to initialize text, tokens, word_counts, hashtag_counts, and mention_counts
        super().__init__(text)
        # Add specialized functionality for tweets
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        """Extract retweets and return them as a SocialMedia object

        Leverages parent's text property and returns a SocialMedia object
        """
        # Extract retweets using regex pattern matching - directly using grandparent's text property
        # This leverages the existing text property from the Document class
        lines = self.text.split("\n")
        retweet_lines = "\n".join(
            [line for line in lines if line.strip().startswith("RT")]
        )

        # Return the retweets as a SocialMedia object that has its own hashtags and mentions
        # This leverages the existing SocialMedia class functionality
        return SocialMedia(retweet_lines) if retweet_lines else SocialMedia("")
