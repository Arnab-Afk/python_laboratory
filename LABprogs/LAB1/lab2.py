var="Python Programming"
ith=int(input("Enter the index to access: "))
print(ith,"th character is: ",var[ith])
var_length=len(var)
print("Length of var is: ",var_length)
print("Print the slice \"Python\" from the variable: ",var[:6])
print("Print the slice \"program\" from the variable: ",var[7:])
print("Get the string \"thing\" from the variable: ",var[2:4]+var[15:])
print("Convert string into uppercase: ",var.upper())
new_var=" is interesting"
print("Concatenate both the strings: ",var+new_var)
