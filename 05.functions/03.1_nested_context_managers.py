import os
import random
from contextlib import contextmanager

# useful utility to change cwd to current directory


@contextmanager
def in_dir(directory):
    """Change current working directory to `directory`, run some code, and then change back."""

    # store the original directory
    original_dir = os.getcwd()
    # change the directory
    os.chdir(directory)

    try:
        yield
    finally:
        os.chdir(original_dir)


@contextmanager
def stock(ticker):
    print(f"Connecting to NASDAQ for {ticker}")

    class Stock:
        def price(self):
            return random.uniform(100.0, 500.0)

    try:
        connection = Stock()
        yield connection

    finally:
        print(f"Disconnecting from NASDAQ for {ticker}...")


####

script_dir = os.path.dirname(__file__)

with in_dir(script_dir):
    with stock("NVDA") as nvda:
        # here we can just feed in the file ame
        with open("NVDA.txt", "w") as f_out:
            for _ in range(10):
                value = nvda.price()

                # .format(value) substitutes the value into the placeholder ${:.2f}
                # (which means floating poin number with 2 decimal points)
                print("Logging ${:.2f} for NVDA".format(value))

                f_out.write("{:.2f}\n".format(value))
