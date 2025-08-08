# __str__ for user-friendly output, __repr__ for debugging/REPL


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __str__(self):
        emp_str = f"""Employee name: {self.name} Employee salary: {self.salary}"""
        return emp_str

    def __repr__(self):
        emp_str = f"Employee('{self.name}', {self.salary})"
        return emp_str


emp = Employee("John", 50000)
print(str(emp))
print(repr(emp))


# class Employee {
#     constructor(public name: string, public salary: number = 30000) {}

#     // Similar to __str__ in Python
#     toString(): string {
#         return `Employee name: ${this.name} Employee salary: ${this.salary}`;
#     }
# }

# const emp = new Employee("John", 50000);

# // Automatically calls toString() when used in a string context
# console.log(emp.toString());  // "Employee name: John Employee salary: 50000"
# console.log(`Employee: ${emp}`);  // "Employee: Employee name: John Employee salary: 50000"

# Why have 2 things in Python?
# Historical Reasons: Python's dual approach gives more control over different string representations.
# Explicit vs Implicit:
# In Python, print(obj) uses __str__, while obj in REPL uses __repr__
# In TypeScript/JavaScript, console.log(obj) shows the object's structure,
# while obj.toString() or string interpolation uses toString()

# Default behavior works fine - Python provides a default string representation that's usually good enough.
# When you actually need it (which is rare):
# Implement str if you want pretty output when using print(your_object)
# Implement repr if you're debugging and want to see object details in the REPL
