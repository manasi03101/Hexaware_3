class Clerk:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter name:");
        self.age=int(input("enter the age:"));
        self.salary=25000;
        self.desig="Clerk";
    def display(self):
        print("....................................")
        print("Id:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*5/100);
        print("Raised Salary:",new);
    def options(self):
        print("Choose below option to perform the certain task");
        print("1.Create")
        print("2.Display")
        print("3.Raise Salary")
        print("4.exit")
   

class Manager:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter name:");
        self.age=int(input("enter the age:"));
        self.salary=80000;
        self.desig="Manager";
    def display(self):
        print("......................................")
        print("Id:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*20/100);
        print("Raised Salary:",new);

class Tester:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter name:");
        self.age=int(input("enter the age:"));
        self.salary=40000;
        self.desig="Tester";
    def display(self):
        print("................................")
        print("Id:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*10/100);
        print("Raised Salary:",new);

class Developer:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter name:");
        self.age=int(input("enter the age:"));
        self.salary=60000;
        self.desig="Developer";
    def display(self):
        print(".................................")
        print("Id:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        old=self.salary;
        new=old+(old*15/100);
        print("Raised Salary:",new);


C=Clerk();
M=Manager();
T=Tester();
D=Developer();
counter=0;
print("choose the below option num to perfom the certain task");
print("1.Create");
print("2.Display");
print("3.Raise Salary");
print("4.exit");
while True:
    counter+=1;
    n=int(input("enter your choice number:"));
    if(n==1):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.Developer");
        n1=int(input("choose the option number to create:"));
        if(n1==1):
            print("enter the clerk deails");
            C.create();
            C.options()

        elif(n1==2):
            print("enter the manager Details");
            M.create();
            C.options()

        elif(n1==3):
            print("enter the tester Details");
            T.create();
            C.options()

        elif(n1==4):
            print("enter the developer Details");
            D.create();
            C.options()

        else:
            print("wrong selection:");
            
    if(n==2):
        C.display()
        M.display()
        T.display()
        D.display()
        C.options()

    if(n==3):
        C.raisesalary();
        M.raisesalary();
        T.raisesalary();
        D.raisesalary();
        C.options()

    if(n==4):
        print("Exit:");
        break


