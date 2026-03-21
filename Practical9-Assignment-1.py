class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


class Manager(Employee):
    def get_manager_data(self):
        self.department = input("Enter department: ")

    def display_manager(self):
        self.display()
        print("Department:", self.department)


# Processing 10 managers
managers = []

for i in range(10):
    print("\nEnter details for Manager", i+1)
    m = Manager()
    m.get_data()
    m.get_manager_data()
    managers.append(m)

print("\nManager Details:")
for m in managers:
    print("-----")
    m.display_manager()
