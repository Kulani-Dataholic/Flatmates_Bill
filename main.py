class Bill:
    """
    Object that contains data about a bill such as totAal amount and period of the bill
    """

    def __init__(self,amount,period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    create a flatmate person who lives in the flat and pay a share of the bill
    """

    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self,bill,flatmate2):
        weight = self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        topay = bill.amount*weight

        return topay



class PdfReport:

    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pass

the_bill = Bill(amount=120,period="March 2024")
john = Flatmate(name="John",days_in_house=20)
marry = Flatmate(name="Marry",days_in_house=25)

print("John pays: ",john.pays(bill=the_bill,flatmate2=marry))
print("Marry pays: ",marry.pays(bill=the_bill,flatmate2=john))
