# class Employee {
#   constructor(private name: string, private salary: number) {
#     if (salary > 0) {
#       this.salary = salary;
#     } else {
#       this.salary = 0;
#       console.log("Invalid salary!");
#     }
#   }

#   setName(newName: string): void {
#     this.name = newName;
#   }

#   setSalary(newSalary: number): void {
#     this.salary = newSalary;
#   }

#   giveRaise(amount: number): void {
#     this.salary += amount;
#   }
# }

# Core concepts
# Encapsulation: state + behavior bundled together (attributes + methods)
# Inheritance: Extending the functionality of existing code
# Polymorphism: Creating a unified interface that morphs child method behavior
# __init__ (constructor): add data to the object when creating it


class Employee:
    def __init__(self, name, salary):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary += amount


emp = Employee("Korel Rossi", 50000)

print(emp.name)
print(emp.salary)
emp.give_raise(10000)
print(emp.salary)


emp.set_name("Korel Ross")
emp.set_salary(60000)
print(emp.name)
print(emp.salary)


# class Calculator {
#   constructor(private numOne: number, private numTwo: number) {}

#   addition(): number {
#     return this.numOne + this.numTwo;
#   }

#   subtraction(): number {
#     return this.numOne - this.numTwo;
#   }

#   multiplication(): number {
#     return this.numOne * this.numTwo;
#   }

#   division(): number {
#     return this.numOne / this.numTwo;
#   }
# }


class Calculator:
    def __init__(self, num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two

    def addition(self):
        return self.num_one + self.num_two

    def subtraction(self):
        return self.num_one - self.num_two

    def multiplication(self):
        return self.num_one * self.num_two

    def division(self):
        return self.num_one / self.num_two
