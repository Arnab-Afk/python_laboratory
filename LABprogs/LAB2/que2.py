#input list [can be of any type- string integer etc]
input_list=[1,2,3,3,4,5,5,6,7]

#empty list where the values will be stored
result=[]

for item in input_list:
  if item not in result:
    result.append(item)

#list with no duplicates
print(result)
