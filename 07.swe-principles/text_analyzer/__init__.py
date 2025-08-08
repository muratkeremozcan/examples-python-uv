from .counter_utils import plot_counter, sum_counters
from .document import Document
from .social_media import SocialMedia
from .tweets import Tweets

# with __init__ file you can do these
# # Example 1: Package metadata and version
# __version__ = "1.0.0"
# __author__ = "Murat Ozcan"

# # Example 2: Setting up logging
# import logging
# logging.getLogger(__name__).addHandler(logging.NullHandler())

# # Example 3: Environment setup
# import os
# DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')

# # Example 4: Import and expose select functionality (like you're already doing)
# from .counter_utils import plot_counter, sum_counters

# # Example 5: Run startup configurations
# import matplotlib
# matplotlib.use('Agg')  # Set non-interactive backend

# # Example 6: Define package-level constants
# MAX_ITEMS = 10
# DEFAULT_THEME = 'light'

# # Example 7: Conditional imports based on environment
# try:
#     from .advanced_utils import complex_function
# except ImportError:
#     def complex_function(*args, **kwargs):
#         raise NotImplementedError("Advanced utils not available")
