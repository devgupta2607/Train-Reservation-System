""" This is Project on Train Reservation """
import pickle
import random
import os
print('                 ()()()()()()()()()()()()()()()()()()()()')
print('                 ()     DEV TRAVEL SERVICES      ','()')
print('                 ()  Your train journey begins here   ',  '()')
print('                 ()()()()()()()()()()()()()()()()()()()()')

class ticket():
    def __init__(self):          #Initisiling all data members
        
        self.name=""
        self.age=0
        self.date=""
        self.startpoint=""
        self.destpoint=""
        self.resno=0
        self.status=""
        self.trainno=0
        self.trainname=""
        self.ac1seats=0
        self.ac2seats=0
        self.ac3seats=0
        self.sleeperseats=0
        self.tottick=0
        self.totalprice=0
        
    def ret(self):
        return self.resno
    def retname(self):
        return self.name
    
    def display(self):          #Displaying Details
        print()
        print("Name: ",self.name)
        print("Age: ",self.age)
        
        print("Journey Date: ",self.date)
        print("Starting Point of your journey: ",self.startpoint)
        print("Destination Point of your journey: ",self.destpoint)
        print("Reservation Number: ",self.resno)
        
        print("Status: ",self.status)
    
    def reservation(self):      #For Accepting Details 
        print() 
        self.name=input("Enter your name: ")
        self.age=eval(input("Enter age: "))
        self.date= input("Enter the journey date: ")
        self.startpoint=input("Enter the starting point: ")
        self.destpoint=input("Enter the destination point: ")
        
        self.resno=random.randint(1000,1200)
        print("Your Reservation Number is: ",self.resno)
    
    def traindetails(self):    #Ticket booking details
  
        self.totalprice= 0
        self.tottick=0
        ch="Y"
        while ch=="Y":
            print()
            print("Seats categories")
            print("1. AC1 seats")
            print("2. AC2 seats")
            print("3. AC3 seats")
            print("4. Sleeper seats")
            choice=eval(input("Enter your choice for seat: "))
            f=0
            if choice==1:
                self.ac1seats=eval(input("Enter Number of AC1 seats you want: "))
                if self.age<60:
                    self.totalprice= self.totalprice+800*self.ac1seats
                else:
                    self.totalprice= self.totalprice+700*self.ac1seats
                self.tottick=self.tottick+self.ac1seats

                f=1
                
                ch=input("Want to book more seats Y/N: ")
                if ch=="N":
                    break
            if choice==2:
                self.ac2seats=eval(input("Enter Number of AC2 seats you want: "))
                if self.age<60:
                    self.totalprice= self.totalprice+700*self.ac2seats
                else:
                    self.totalprice= self.totalprice+600*self.ac2seats
                self.tottick=self.tottick+self.ac2seats
                
                f=1
                ch=input("Want to book more seats Y/N: ")
                if ch=="N":
                    break
            if choice==3:
                self.ac3seats=eval(input("Enter Number of AC3 seats you want: "))
                if self.age<60:
                    self.totalprice= self.totalprice+600*self.ac3seats
                else:
                    self.totalprice= self.totalprice+500*self.ac3seats
                self.tottick=self.tottick+self.ac3seats

                f=1
                
                ch=input("Want to book more seats Y/N: ")
                if ch=="N":
                    break
            if choice==4:
                self.sleeperseats=eval(input("Enter Number of Sleeper seats you want: "))
                if self.age<60:
                    self.totalprice= self.totalprice+650*self.sleeperseats
                else:
                    self.totalprice= self.totalprice+550*self.sleeperseats
                self.tottick=self.tottick+self.sleeperseats
                f=1
                ch=input("Want to book more seats Y/N: ")
                if ch=="N":
                    break
                            
                        
            else:
                print("Wrong Reservation Number Try again")
                ch = "Y"
                    
        if f==1:
            self.status="CONFIRMED"  
        z=["Rajdhani","Superfast Express","Sampark Kranti","DJ Expess","DM Express","DI Express"]
        self.trainno=random.randint(1100,1110)
        p=random.randint(0,5)
        self.trainname=z[p]
                
        
    def cancellation(self):         #Cancelling ticket
        f=0
        file1=open("ticket.dat","rb")
        file2=open("main.dat","ab")
        print()
        print("*** Ticket Cancellation ***")
        print()
        r=eval(input("Enter Your Reservation number: "))
        try:
            while True:
                self=pickle.load(file1)
                z=self.ret()
                if z!=r:
                    pickle.dump(self,file2)
                if z==r:
                    f=1
        except EOFError:
            pass
        file1.close()
        file2.close()
        os.remove("ticket.dat")
        os.rename("main.dat","ticket.dat")
        if f==0:
            print("No such Reservation Number exist")
        else:
            print("Your ticket has been CANCELLED")
            print("Money Refunded")
            
    def outputdetail(self):          #Printing ticket details
        print()
        print("Your train number is : ",self.trainno)
        print("Train name : ",self.trainname)
        print("Number of AC1 seats booked: ",self.ac1seats)
        print("Number of AC2 seats booked: ",self.ac2seats)
        print("Number of AC3 seats booked: ",self.ac3seats)
        print("Number of Sleeper seats booked: ",self.sleeperseats)
        print("Total number of Seats booked: ",self.tottick)
        print("Total Amount to be Paid: ",self.totalprice)
        
    def writefile(self):            # Writing details in file
        file3=open("ticket.dat","wb")
        print("*** Train Reservation ***")
        self.reservation()
        pickle.dump(self,file3)
        file3.close()
        
    def writefile2(self):           # Writing ticket detailsin file
        file4=open("ticket.dat","rb")
        file5=open("ticket1.dat","wb")
        print("*** Train Details ***")
        print()
        x=eval(input("Enter the reservation number"))
        try:
            while 1:
                self=pickle.load(file4)
                if x==self.resno:
                    self.traindetails()
                pickle.dump(self,file5)
            
        except EOFError:
            pass
        
        file4.close()
        file5.close()
        os.remove("ticket.dat")
        os.rename("ticket1.dat","ticket.dat")
        
    def readfile(self):          # Readinng details from file
        file6=open("ticket.dat","rb")
        
        try:
            while True:
                self=pickle.load(file6)
                
                self.display()
                
        except EOFError:
            pass
        file6.close()
        
    def readfile1(self):       # Reading ticket details from file
        file7=open("ticket.dat","rb")
        t=eval(input("Enter your reservation number: "))
        try:
            while True:
                self=pickle.load(file7)
                if t==self.resno:
                    self.outputdetail()
                else:
                    print("There is no such Reservation Number")
                    print("Try Again")
                
        except EOFError:
            pass
        file7.close()
        
    def newpro(self):        # Creating a new profile
        file8=open("ticket.dat","ab")
        print("*** Train Details ***")
        self.reservation()
        pickle.dump(self,file8)
        file8.close()
        
    def payment(self):      # Paying for tickets
        
        file9=open("ticket.dat","rb")
        print("*** Payment ***")
        print() 
        i=eval(input("Enter your reservation number: "))
        try:
            while True:
                self=pickle.load(file9)
                if i==self.resno:
                    print("             PAYMENT             ")
                    print(" 1.Debit card")
                    print(" 2.Paytm Wallet")
                    x=eval(input("Enter your choice"))
                    if x==1:
                        y=eval(input("Enter your Debit Card Number"))
                        z=eval(input("Enter your 3-digit CVV Code"))
                        print("Processing...")
                        print("Payment of Rs.",self.totalprice,"is done")
                        break
                    if x==2:
                        a=input("Enter your paytm username or mobile number")
                        pw=input("Enter Password")
                        print("Processing...")
                        print("Payment of Rs.",self.totalprice,"is deducted from your paytm wallet")
                        break
                    else:
                        print("Wrong choice Try again")
                else:
                    print("There is no such Reservation Number")
                    print("Try Again")
        except EOFError:
            pass
        file9.close()
        
    def receipt(self):        # Printing receipt
        file10=open("ticket.dat","rb")
        y=eval(input("Enter your Reservation Number: "))
        try:
            while 1:
                self=pickle.load(file10)
                if y==self.resno:
                    print()
                    print("=========== RECEIPT ============")
                    print(" Name                              : ",self.name)
                    print(" Age                               : ",self.age)
                    print(" Journey Date                      : ",self.date)
                    print(" Starting Point of your journey    : ",self.startpoint)
                    print(" Destination Point of your journey : ",self.destpoint)
                    print(" Reservation Number                : ",self.resno)
                    print(" Your train number is              : ",self.trainno)
                    print(" Train name                        : ",self.trainname)
                    print(" Number of AC1 seats booked        : ",self.ac1seats)
                    print(" Number of AC2 seats booked        : ",self.ac2seats)
                    print(" Number of AC3 seats booked        : ",self.ac3seats)
                    print(" Number of Sleeper seats booked    : ",self.sleeperseats)
                    print(" Total number of Seats booked      : ",self.tottick)
                    print(" Total Amount Paid                 : ",self.totalprice)
                else:
                    print("There is no such Reservation Number")
                    print("Try Again")
        except EOFError:
            pass
        file10.close()
        
def menu():
    
    tick=ticket()
    
    while True:
        print()
        print("********** MENU ************")
        print(" 1. RESERVATION OF TICKETS")
        print(" 2. UPDATE TRAIN DETAILS")
        print(" 3. PRINT TRAIN DETAILS")
        print(" 4. CANCELLATION OF TICKETS")
        print(" 5. PAYMENT")
        print(" 6. PRINT THE RECEIPT")
        print(" 7. CREATE A NEW PROFILE")
        print(" 8. ABOUT US")
        print(" 9. QUIT")
        mchoice= eval(input("Enter the code from menu: "))
        print()
        if mchoice==1 :
            tick.writefile()
        elif mchoice==2:
            tick.writefile2()
        elif mchoice == 3:
            tick.readfile1()
        elif mchoice==4:
            tick.cancellation()
        elif mchoice==5:
            tick.payment()
        elif mchoice==6:
            tick.receipt()
        elif mchoice==7:
            tick.newpro()
        elif mchoice==8:
            print("**************** ABOUT US ********************")
            print("Owner: Dev Gupta")
            print("Contact Number: 9476476262")
            print("Office Address: D-5 Bandra Street Near Filmcity Mumbai-400013")
        elif mchoice==9:
            print("THANK YOU FOR USING OUR SERVICE")
            break
        print()
        q=input("Press Enter to Go back to the menu")
menu()
    
    
        
        
        
    
            
                  
        
        
            
            
        
        
        
