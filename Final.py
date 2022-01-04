import csv
class Display_Details:
    
    
    def __init__(self,lot,parkedLots,Spot,n):
        self.lot = lot
        self.parkedLots = parkedLots
        self.Spot = Spot
        self.n=n
    
    def display(null):
        print("P.Park a Vehicle")
        print("E.Exit a Lot ")
        print("F.Find a Car ")
        print("Q.Quit \n")
    
    def park(self):
        print("\nEnter the Vehicle Type:")
        print("1.Car ")
        print("2.Motor Cycle ")
        print("3.Truck\n ")
        vehType=int(input())
        if vehType==1:
            print("\nEnter Vehicle Plate Number: \n")
            vehPlateNum=(input())
            print("\nAVAILABLE LOTS",lot)
            print("Select a Lot Number: \n")
            vehLotNum=int(input())
            print("\nDo you Proceed to Pay Parking Fee 10$ Per Day? (Yes(or)No)")
            mySelection=input().upper()
            if mySelection=="YES":
                myOrder="\nYour car number {1}  is Parked in the Lot {2}\n"
                print(myOrder.format(vehType,vehPlateNum,vehLotNum))
                self.parkedLots.append(vehLotNum)
                self.lot.remove(vehLotNum)
                print("\nOCCUPIED LOTS",self.parkedLots)
                print("--------------------------------\n")
                with open("csv1.csv","a")as newdet1:
                    det1=csv.writer(newdet1)
                    det1.writerow([vehPlateNum,vehLotNum,"Parked"])
                self.display()
            else:
                print("Parking Reservation Cancelled !")
    def exit(self):
        print("\nEnter the Vehicle Type:")
        print("1.Car ")
        print("2.Motor Cycle ")
        print("3.Truck\n ")
        vehType=int(input())
        if vehType==1:
            if(len(self.parkedLots)==0):
               print("You Have not parked any vehicles")
            else:
                print("\nPARKED LOTS",self.parkedLots)
                print("\nEnter Vehicle Lot Number: \n")
                vehLotNum=int(input())
                self.parkedLots.remove(vehLotNum)
                print("\nYour car is Exited Successfully")
                self.lot.append(vehLotNum)
                self.lot.sort()
                print("--------------------------------")
                print("\nAVAILABLE LOTS",self.lot)
                with open("csv1.csv","a")as newdet:
                    det=csv.writer(newdet)
                    det.writerow([vehLotNum,"Exited"])
                self.display()
    
    def check(self):
        self.n=input().upper()
        if self.n == "P":
            self.park()
            self.check()
        elif self.n=="E":
            self.exit()
            self.check()
            
lot=[1,2,3,4,5,6,7,8,9,10]
parkedLots=[]
Spot=0
n=0
p1 = Display_Details(lot,parkedLots,Spot,n)
p1.display()
p1.check()
