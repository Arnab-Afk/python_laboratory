emp_id=input("Enter employee ID: ")
emp_name=input("Enter Employee Name: ")
basic_salary=float(input("Enter Employee Salary: "))

da=basic_salary*0.03
hra=basic_salary*0.1
net_Sal=basic_salary+da+hra

print("Employee Id: ",emp_id)
print("Employee Name: ",emp_name)
print("Net Salary of Employee: ",net_Sal)
