class Employee:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount


# Polymorphism: Creating a unified interface that morphs child method behavior
# Can even change method signature - keep arg order similar, add new args last
class Manager(Employee):
    def __init__(self, name, salary=Employee.MIN_SALARY, project=None):
        # Employee.__init__(self, name, salary) # using super is much better, saves the self arg
        super().__init__(name, salary)
        self.project = project

    def give_raise(self, amount, bonus=1.05):
        # Employee.give_raise(self, amount * 1.1) # using super is much better, saves the self arg
        super().give_raise(amount * bonus)


mgr = Manager("Alex", 90000, "Engineering")
mgr.give_raise(5000, 1.1)  # Gives 5500 total (5000 + 10% bonus)
print(mgr.salary)


# class Employee {
#     static MIN_SALARY = 30_000;

#     constructor(
#         public name: string,
#         public salary: number = Employee.MIN_SALARY
#     ) {
#         if (salary < Employee.MIN_SALARY) {
#             this.salary = Employee.MIN_SALARY;
#         }
#     }

#     giveRaise(amount: number): void {
#         this.salary += amount;
#     }
# }

# class Manager extends Employee {

#     constructor(
#         name: string,
#         salary: number = Employee.MIN_SALARY
#         public project = '',
#     ) {
#         super(name, salary);
#     }
#
#     giveRaise(amount: number, bonus = 1.05): void {
#         super.giveRaise(amount * bonus);
#     }
# }

# // Example usage:
# const mgr = new Manager("Alex", 90_000, "Engineering");
# mgr.giveRaise(5_000);
# console.log(mgr.salary); // 95500
