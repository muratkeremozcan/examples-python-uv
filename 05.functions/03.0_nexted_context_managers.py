# Key Takeaways:
# Context managers automatically manage resource setup and cleanup.
# Nested context managers are fine in Python
# Using _ as a dummy variable is a common idiom when the loop index isn't needed.
# .format(value) substitutes the value into the placeholder ${...}

import contextlib
import os
import random


@contextlib.contextmanager
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


with stock("NVDA") as nvda:
    script_dir = os.path.dirname(__file__)
    # here we have to come up with a file path (a bit contrived, better version next file)
    file_path = os.path.join(script_dir, "NVDA.txt")

    with open(file_path, "w") as f_out:
        for _ in range(10):
            value = nvda.price()

            # .format(value) substitutes the value into the placeholder ${:.2f}
            # (which means floating poin number with 2 decimal points)
            print("Logging ${:.2f} for NVDA".format(value))

            f_out.write("{:.2f}\n".format(value))
