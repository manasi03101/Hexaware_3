import os


while True:
    print("-------------------------")
    print("Enter the Choie of Operation")
    print("1.Create")
    print("2.Display")
    print("3.Delete Record")
    print("4.Exit")
    print("-------------------------");

    ch1 = int(input("Enter choice:"))

    while True:
        if(ch1==1):
            print("-------------------------")
            print("1.Clerk")
            print("2.Developer")
            print("3.Manager")
            print("4.Tester")
            print("5.Exit")
            print("-------------------------")
            ch2 = int(input("Enter choice:"))
             #while True:
            if(ch2==1):
                #f=open("Clerk.txt", "x");
                a=open("Clerk.txt", "a");
                id =input("Enter Id : ")
                name =input("Enter Name : ")
                age =input("\nEnter age : ")
                salary ="20000";
                Designation ="Clerk";

                a.write(name);
                a.write(age);
                a.write(salary);
                a.write(Designation);

                a.close();

                break
            elif(ch2==2):
                #f=open("Developer.txt", "x");
                a=open("Developer.txt", "a");
                id =input("Enter Id : ")
                name =input("Enter Name : ")
                age =input("\nEnter age : ")
                devsalary ="25000";
                devDesignation ="Developer";

                a.write(name);
                a.write(age);
                a.write(devsalary);
                a.write(devDesignation);

                a.close();
                
                break
            elif(ch2==3):
                #f=open("Manager.txt", "x");
                a=open("Manager.txt", "a");
                id =input("Enter Id : ")
                name =input("Enter Name : ")
                age =input("\nEnter age : ")
                magsalary ="30000";
                magDesignation ="Manager";

                a.write(name);
                a.write(age);
                a.write(magsalary);
                a.write(magDesignation);

                a.close();
               
                break

            elif(ch2==4):
                #f=open("Tester.txt", "x");
                a=open("Tester.txt", "a");
                id =input("Enter Id : ")
                name =input("Enter Name : ")
                age =input("\nEnter age : ")
                tessalary ="39000";
                tesDesignation ="Tester";

                a.write(name);
                a.write(age);
                a.write(tessalary);
                a.write(tesDesignation);

                a.close();
                break
            else:
                print("Exiting")
                break
                
                
        elif(ch1==2):
            print("-------------------------")
            print("1.Clerk")
            print("2.Developer")
            print("3.Manager")
            print("4.Tester")
            print("5.Exit")
            print("-------------------------")
            ch2 = int(input("Enter choice:"))
            if(ch2==1):
                readdate=open("Clerk.txt","r");
                print(readdate.read());
                
                break
            elif(ch2==2):
                readdate=open("Developer.txt","r");
                print(readdate.read());
                
                break
            elif(ch2==3):
                readdate=open("Manager.txt","r");
                print(readdate.read());
               
                break
            elif(ch2==4):
                readdate=open("Tester.txt","r");
                print(readdate.read());
               
                break
            elif(ch2>=5):
               
                break
                
            else:
                print("Exit")
                break
           
        elif(ch1==3):
            print("-------------------------")
            print("1.Clerk")
            print("2.Developer")
            print("3.Manager")
            print("4.Tester")
            print("5.Exit")
            print("-------------------------")
            ch3 = int(input("Enter choice:"))
            if(ch3==1):
                myfile=input("Enter the file to Delete  ");

                if os.path.exists(myfile):
                    os.remove(myfile);
                    print("File Deleted Successfully");
                else:
                    print("File Does't Exists");
                
                break
            elif(ch3==2):
                myfile=input("Enter the file to Delete  ");

                if os.path.exists(myfile):
                    os.remove(myfile);
                    print("File Deleted Successfully");
                else:
                    print("File Does't Exists");
                
                break
            elif(ch3==3):
                myfile=input("Enter the file to Delete  ");

                if os.path.exists(myfile):
                    os.remove(myfile);
                    print("File Deleted Successfully");
                else:
                    print("File Does't Exists");
               
                break
            elif(ch3==4):
                myfile=input("Enter the file to Delete  ");

                if os.path.exists(myfile):
                    os.remove(myfile);
                    print("File Deleted Successfully");
                else:
                    print("File Does't Exists");
               
                break
            elif(ch3>=5):
               
                break
                
            else:
                print("Exit")
                break
            
        elif(ch2==4):
            pass;
            
        else:
            if(ch1==5):
                pass;