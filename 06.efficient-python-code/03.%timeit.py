# %timeit modifiers explained:
# -n <number>    sets the number of loops per run (i.e. how many times the statement is repeated in each run)
# -r <number>    sets the number of runs (i.e. how many separate times to repeat the whole experiment)
# -o             stores the result in a variable (a TimeitResult object) which you can inspect for stats


# [output_if_true | for variable in iterable | if condition]
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

nums_unpack = [*range(51)]
print(nums_unpack)

# IPython feature and isn’t recognized in a plain Python script when run with the standard Python interpreter.
# To use %timeit, you need to run the code in an IPython environment (for example, in a Jupyter Notebook or an IPython shell)
# %timeit [num for num in range(51)]
# %timeit [*range(51)]


# Example 1: Benchmark a list comprehension with 25 loops per run and 5 runs.
# This will execute the comprehension 25 times per run, for a total of 5 runs.
# %timeit -r5 -n25 [num for num in range(51)]

# Example 2: Benchmark the same using unpacking.
# %timeit -r5 -n25 [*range(51)]

# Example 3: Store the result in a variable using the -o modifier.
# In an IPython environment, this returns a TimeitResult object.
# result = %timeit -o -r5 -n25 [*range(51)]
# You can then inspect the result, for example:
# print(result.best)     # Best (minimum) time out of all runs.
# print(result.repeat)   # A list of times for each run.
