import math
import sys
class Bank:
    def __init__(self):
        self.__Bank_Name=""
        self.__Borrower_Name=""
        self.__Principal=0
        self.__No_of_Years=0
        self.__Rate_of_Interest=0.0
        self.__pay_per_emi=0.0
        self.__Amount=0
        self.__Balance=[0]
    def LOAN (self,B_name,name,principal,NOI,ROI):
        self.__Bank_Name=B_name
        self.__Principal=principal
        self.__Borrower_Name=name
        self.__No_of_Years=NOI
        self.__Rate_of_Interest=ROI/100
        self.__Amount=(self.__Principal+(self.__Principal*self.__No_of_Years*self.__Rate_of_Interest))
        self.__pay_per_emi=math.ceil(self.__Amount/(self.__No_of_Years*12))
        iterator=1
        while(self.__Balance[-1]<self.__Amount):
            if self.__Amount-self.__Balance[-1]<self.__pay_per_emi:
                self.__Balance.append(self.__Amount-self.__Balance[-1])
                break
            self.__Balance.append(self.__Balance[iterator-1]+self.__pay_per_emi)
            iterator+=1
    def PAYMENT(self,lum_sum,emi):
        self.__Balance.clear()
        self.__Balance.append(0)
        iterator=1
        while(self.__Balance[-1]<self.__Amount):
            if self.__Amount-self.__Balance[-1]<self.__pay_per_emi:
                self.__Balance.append(self.__Amount-self.__Balance[-1])
                break
            self.__Balance.append(self.__Balance[iterator-1]+self.__pay_per_emi)
            if iterator==emi:
                self.__Balance[iterator]+=lum_sum
            iterator+=1
    def BALANCE(self,emi):
        print(self.__Bank_Name," ",self.__Borrower_Name," ",self.__Balance[emi]," ",math.ceil((self.__Amount-self.__Balance[emi])/self.__pay_per_emi))
d={}
with open(sys.argv[1]) as fl:
    while True:
        line=fl.readline()
        if not line:
            break
        line=line.strip()
        line=list(map(str,line.split()))
        c=line[1]+"_"+line[2]
        if c not in d:
            d[c]=Bank()           #creating dictionary with username_bankname as key so that every user will have its seperate objects 
# Now a user having different loans in different banks is also accounted for as the key uses bank name also for identification and not just users name.
# optimised solution as all the transaction and its detailes is stored ina single object of class only 
# Balance of the user is stored in a list but as it is constantly cleaned and reused after every payment it is memory efficient
# As dictionary is being uesd for accessing user data it is very fast as it only takes O(1) time complexity to search. 
        if line[0]=="LOAN":
            d[c].LOAN(line[1],line[2],int(line[3]),int(line[4]),int(line[5]))
        elif line[0]=="PAYMENT":
            d[c].PAYMENT(int(line[3]),int(line[4]))
        elif line[0]=="BALANCE":
            d[c].BALANCE(int(line[3]))