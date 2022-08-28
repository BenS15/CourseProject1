
def CalculateTaxandNetpay(TotalHours, HourlyRate, TaxRate):
    tax = float(TotalHours) * float(HourlyRate) * (float(TaxRate) / 100)
    net_pay = float(TotalHours) * float(HourlyRate) - tax
    return tax, net_pay

def GetName():
    name = input("Enter employee name: ")

    return name

def GetTotalHours():
    TotalHours = float(input("Enter total hours: "))
    return TotalHours

def GetHourlyRate():
    HourlyRate = float(input("Enter hourly rate: "))
    return HourlyRate

def GetTaxRate():
    TaxRate = float(input("Enter tax rate (in %): "))
    return TaxRate

def GetGrossPay(TotalHours, HourlyRate):
    gross_pay = float(TotalHours) * float(HourlyRate)
    return gross_pay

def DisplayEmpInfo(name, TotalHours, HourlyRate, TaxRate, tax, gross_pay, net_pay):
    print("====================================================")
    print("Employee name:", name)
    print("Total hours:", TotalHours)
    print("Hourly rate:", HourlyRate)
    print("Tax rate:", TaxRate)
    print("Income tax:", tax)
    print("Gross pay:", gross_pay)
    print("Net pay:", net_pay)
    print("====================================================")

def DisplayTotalInfo(total_employees, TotalHours, total_tax, total_gross_pay, total_net_pay):
    print("====================================================")
    print("Total number of employees:", total_employees)
    print("Total hours:", TotalHours)
    print("Total tax:", total_tax)
    print("Total gross pay:", total_gross_pay)
    print("Total net pay:", total_net_pay)
    print("====================================================")

def main():
    
    total_employees = 0
    TotalHours = 0
    total_tax = 0
    total_gross_pay = 0
    total_net_pay = 0

    while True:
        name = GetName()
        if name.lower() == "End":
            break
        hours = GetTotalHours()
        HourlyRate = GetHourlyRate()
        TaxRate = GetTaxRate()
        gross_pay = GetGrossPay(hours, HourlyRate)
        tax, net_pay = CalculateTaxandNetpay(hours, HourlyRate, TaxRate)
        DisplayEmpInfo(name, hours, HourlyRate, TaxRate, tax, gross_pay, net_pay)

        
        total_employees += 1
        TotalHours += hours
        total_tax += tax
        total_gross_pay += gross_pay
        total_net_pay += net_pay
    
    DisplayTotalInfo(total_employees, TotalHours, total_tax, total_gross_pay, total_net_pay)



if __name__ == "__main__":
    main()
