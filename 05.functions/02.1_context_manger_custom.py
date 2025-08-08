# We can create our own context managers using @contextlib.contextmanager.

# The 'timer()' context manager measures the execution time of the code within its block.
# The 'open_read_only()' context manager opens a file for reading only and ensures it closes automatically.
# Using os.path.dirname(__file__) helps us construct an absolute path to
# avoid file path issues.

import contextlib
import os
import time


# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block
    yield
    end = time.time()
    print("Elapsed: {:.2f}s".format(end - start))


with timer():
    time.sleep(0.25)


############


@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

    Args:
      filename (str): The location of the file to read

    Yields:
      file object
    """

    # Construct an absolute path based on this script's directory
    script_dir = os.path.dirname(__file__)  # Directory containing this script
    file_path = os.path.join(script_dir, filename)

    read_only_file = open(file_path, mode="r")

    # Yield read_only_file so it can be assigned to alice
    yield read_only_file

    # Close read_only_file
    read_only_file.close()


with open_read_only("alice.txt") as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ["cat", "cats"]:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))
