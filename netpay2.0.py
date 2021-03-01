class PayRoll():
  
    def __init__(self, name, department, basic_pay, benefits):
        self.name = input(name)
        self.department = input(department)
        self.basic_pay = int(input(basic_pay))
        self.benefits = int(input(benefits))
        self.total_pay = 0
        self.nssf = 0
        self.taxable_pay = 0
        self.tax_payable = 0
        self.personal_relief = 0
        self.paye = 0
        self.nhif = 0
        self.net_pay = 0

    def personal_details(self):
        return f'{self.name} is in the {self.department} department and earns a basic pay of KES{self.basic_pay} and KES{self.benefits} in benefits.'

    def calculate_total_pay(self):
        self.total_pay = self.basic_pay + self.benefits
        return self.total_pay

    def calculate_nssf(self):
        nssf_rate = input("Do you want to use old or new NSSF rates?(New or Old):\n")

        if nssf_rate == "New" or nssf_rate == "new" or nssf_rate == "new rates" or nssf_rate == "New rates" or nssf_rate == "New Rates" or nssf_rate == "New Rate" or nssf_rate == "new Rate" or nssf_rate == "new rate":
            if self.total_pay<=18000: 
                self.nssf = self.total_pay*0.06
                return self.nssf

            elif self.total_pay > 18000:
                self.nssf = 1080
                return self.nssf

        elif nssf_rate == "Old" or nssf_rate == "old" or nssf_rate == "old rates" or nssf_rate == "Old rates" or nssf_rate == "Old Rates" or nssf_rate == "Old Rate" or nssf_rate == "old Rate" or nssf_rate == "old rate":
            self.nssf = 200
            return self.nssf

    def calculate_taxable_pay(self):
        self.taxable_pay = self.total_pay - self.nssf
        return self.taxable_pay
    
    def calculate_tax_payable(self):
        if self.taxable_pay <= 24000:
            self.tax_payable = self.taxable_pay * 0.1
            return self.tax_payable

        elif self.taxable_pay >= 24001 and self.taxable_pay<= 40667:
            self.tax_payable = (24000*0.1) + (0.15*(self.taxable_pay-24000))
            return self.tax_payable

        elif self.taxable_pay >= 40668 and self.taxable_pay<= 57333:
            self.tax_payable = (24000*0.1) + (0.15*(40667-24000))+(0.20*(self.taxable_pay-40668))
            return self.tax_payable

        elif self.taxable_pay > 57334:
            self.tax_payable = (24000*0.1) + (0.15*(40667-24000))+(0.20*(57333-40668))+(0.25*(self.taxable_pay-57333))
            return self.tax_payable

        else:
            self.taxable_payable = (f'Please enter a positive number.')
            return self.tax_payable

    def set_personal_relief(self):
        if self.tax_payable <= 2400:
            self.personal_relief = self.tax_payable
            return self.personal_relief

        elif self.tax_payable >=2401:
            self.personal_relief = 2400
            return self.personal_relief

    def calculate_paye(self):
        self.paye = self.tax_payable - self.personal_relief
        return self.paye

    def calculate_nhif(self):
        if self.basic_pay <= 5999:
            self.nhif = 150
            return self.nhif

        elif self.basic_pay >=6000 and self.basic_pay <=7999:
            self.nhif = 300
            return self.nhif

        elif self.basic_pay >=8000 and self.basic_pay <=11999:
            self.nhif = 400
            return self.nhif

        elif self.basic_pay >=12000 and self.basic_pay <=14999:
            self.nhif = 500
            return self.nhif

        elif self.basic_pay >=15000 and self.basic_pay <=19999:
            self.nhif = 600
            return self.nhif

        elif self.basic_pay >=20000 and self.basic_pay <=24999:
            self.nhif = 750
            return self.nhif

        elif self.basic_pay >=25000 and self.basic_pay <=29999:
            self.nhif = 850
            return self.nhif

        elif self.basic_pay >=30000 and self.basic_pay <=34999:
            self.nhif = 900
            return self.nhif

        elif self.basic_pay >=35000 and self.basic_pay <=39999:
            self.nhif = 950
            return self.nhif

        elif self.basic_pay >=40000 and self.basic_pay <=44999:
            self.nhif = 1000
            return self.nhif

        elif self.basic_pay >=45000 and self.basic_pay <=49999:
            self.nhif = 1100
            return self.nhif

        elif self.basic_pay >=50000 and self.basic_pay <=59999:
            self.nhif = 1200
            return self.nhif

        elif self.basic_pay >=60000 and self.basic_pay <=69999:
            self.nhif = 1300
            return self.nhif

        elif self.basic_pay >=70000 and self.basic_pay <=79999:
            self.nhif = 1400
            return self.nhif

        elif self.basic_pay >=80000 and self.basic_pay <=89999:
            self.nhif = 1500
            return self.nhif

        elif self.basic_pay >=9000 and self.basic_pay <=99999:
            self.nhif = 1600
            return self.nhif

        elif self.basic_pay >= 100000:
            self.nhif = 1700
            return self.nhif


    def calculate_net_pay(self):
        self.net_pay = float(self.total_pay) - float(self.nssf) - float(self.paye) - float(self.nhif)
        return self.net_pay

# Person 1
personal_info1 = PayRoll(name="What is your name:\n", department="What is your department:\n", 
basic_pay="What is your month basic salary?\n", benefits="What are your benefits(in cash)?\n")
result1 = personal_info1.personal_details()
total_pay1 = personal_info1.calculate_total_pay()
nssf1 = personal_info1.calculate_nssf()
taxable_pay1 = personal_info1.calculate_taxable_pay()
tax_payable1 = personal_info1.calculate_tax_payable()
personal_relief1 = personal_info1.set_personal_relief()
paye1 = personal_info1.calculate_paye()
nhif1 = personal_info1.calculate_nhif()
net_pay1 = personal_info1.calculate_net_pay()

print(result1)
print(f'Your Total Pay is',total_pay1)
print(f'Your NSSF is',nssf1)
print(f'NB: NSSF is calculated on the Total Pay and not the Basic Salary.')
print(f'Your Taxable pay is',taxable_pay1)
print(f'Your Tax Payable is',tax_payable1)
print(f'Your Personal Relief is',personal_relief1)
print(f'Your PAYE is',paye1)
print(f'Your NHIF is',nhif1)
print(f'NB: NHIF is calculated on the Basic Salary and not Total Pay.')
print(f'Your Net Pay is',net_pay1)

# Person 2
"""
personal_info2 = PayRoll(name="What is your name:\n", department="What is your department:\n", 
basic_pay="What is your month basic salary?\n", benefits="What are your benefits(in cash)?\n")
result2 = personal_info2.personal_details()
total_pay2 = personal_info2.calculate_total_pay()
nssf2 = personal_info2.calculate_nssf()
taxable_pay2 = personal_info2.calculate_taxable_pay()
tax_payable2 = personal_info2.calculate_tax_payable()
personal_relief2 = personal_info2.set_personal_relief()
paye2 = personal_info2.calculate_paye()
nhif2 = personal_info2.calculate_nhif()
net_pay2 = personal_info2.calculate_net_pay()

print(result2)
print(f'Your Total Pay is',total_pay2)
print(f'Your NSSF is',nssf2)
print(f'Your Taxable pay is',taxable_pay2)
print(f'Your Tax Payable is',tax_payable2)
print(f'Your Personal Relief is',personal_relief2)
print(f'Your PAYE is',paye2)
print(f'Your NHIF is',nhif2)
print(f'NB: NHIF is calculated on the basic salary and not total pay.')
print(f'Your Net Pay is',net_pay2)"""
