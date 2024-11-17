def annual_net_income(gross_salary):
    # complete your function implementation here...
    #return net_salary
    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else:
        tax_rate = 0.15
        
    net_salary = gross_salary * (1 - tax_rate)
    return net_salary

#gross_salary = 40000  
#net_salary = annual_net_income(gross_salary)
#print(f"The net annual income of £{gross_salary} is £{net_salary}.")   
        

#gross_salary = 60000  
#net_salary = annual_net_income(gross_salary)
#print(f"The net annual income of £{gross_salary} is £{net_salary}.")  

#gross_salary = 30000  
#net_salary = annual_net_income(gross_salary)
#print(f"The net annual income of £{gross_salary} is £{net_salary}.") 

#gross_salary = 20000  
#net_salary = annual_net_income(gross_salary)
#print(f"The net annual income of £{gross_salary} is £{net_salary}.") 

