# Context Managers in Python:
# - They automatically manage resource setup and cleanup (e.g., opening/closing files).
# - The 'with' statement ensures cleanup happens even if errors occur, reducing resource leaks.
# - While JavaScript typically uses try/finally for such tasks, Python's context managers offer a concise, explicit syntax.

# with context-manager(args) as variable-name
# with context-manager()
with open("alice.txt") as file:
    text = file.read()
# we have some file directory issues here, better version next file
n = 0
for word in text.split():
    if word.lower() in ["cat", "cats"]:
        n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))


# Context manager examples

# •	Temporary Files:
# import tempfile

# with tempfile.TemporaryFile() as temp_file:
#     temp_file.write(b"Some temporary data")
#     temp_file.seek(0)
#     data = temp_file.read()


# •	DB connections
# import sqlite3

# with sqlite3.connect('my_database.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM my_table")
#     results = cursor.fetchall()


# •	Suppressing Exceptions:
# from contextlib import suppress

# with suppress(FileNotFoundError):
#     open('nonexistent_file.txt')


# Custom context managers
# from contextlib import contextmanager

# @contextmanager
# def my_context_manager():
#     print("Entering the context")
#     yield
#     print("Exiting the context")

# with my_context_manager():
#     print("Inside the context")
