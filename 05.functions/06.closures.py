# Key Takeaways:
# - Python functions can capture and "remember" values from their defining scope in a closure (accessible via __closure__).
# - Even if the original function is redefined or deleted, a closure retains its captured values.
# - Inspecting __closure__ helps understand what variables a function has closed over.


def return_a_func(arg1, arg2):
    def new_func():
        print("arg1 was {}".format(arg1))
        print("arg2 was {}".format(arg2))

    return new_func


my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__))

# Get the values of the variables in the closure
closure_values = [my_func.__closure__[i].cell_contents for i in range(2)]
print(closure_values)


#########


def my_special_function():
    print("You are running my_special_function()")


def get_new_func(func):
    def call_func():
        func()

    return call_func


new_func = get_new_func(my_special_function)


# Show that you still get the original message even if you redefine
# my_special_function() to only print "hello".
def my_special_function():
    print("hello")


# Show that even if you delete my_special_function(), you can still call
# new_func() without any problems.
del my_special_function

new_func()
