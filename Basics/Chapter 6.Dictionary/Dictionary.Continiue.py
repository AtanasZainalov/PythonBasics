#### to make the numbers uniq in the list of numbers we can put them in a dictionary , that will delete the duplicates

n
#loop through each element
#loop through keys only
#loop through values only

customer1 = {
    "CustomerID": "ALFKI",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Anders",
    "ContactTitle": "Sales Representative",
    "Address": "Obere Str. 57",
    "City": ['Berlin','Moscow'],
    "Region": None,
    "PostalCode": 12209,
    "Country": "Germany",
    "Phone": "030-0074321",
    "Fax": "030-0076545",
    "isActive": True
}


# scope of variable, where variable lives
# print(column)

print("--------------------------------------")
print("# 1. Loop through each Element (key, value)")
for column, value in customer1.items():
    print(f"column name: {column}")
    print(f"column value: {value}")
    print(f"INFO: {column.lower()} = {value}")
    # print(f"val3 value: {val3}")
    print("*************************************")

# for key, value in customer1.items():
#     print(f"column name: {key}")
#     print(f"column value: {value}")
#     print("*************************************")

print("# 2. Loop through Keys only")
print("# by Default, for loop in dictionary returns only keys")
for column in customer1:
    print(f"column name: {column}")

print("############################################")
print("# using keys(), for loop in dictionary returns only keys")
for key in customer1.keys():
    print(f"column name: {key}")
    print(f"column value: {customer1[key]}")

print("############################################")
print("# 3. Loop through Values only")
print("# for loop in dictionary returns only values")
for value in customer1.values():
    print(f"column value: {value}")

columns = list(customer1.keys())
print(f"list of columns {columns}")
print(f"first column of columns {columns[0]}")
print(f"first column of columns {list(customer1.keys())[0]}")

c1_info = list(customer1.values())
print(f"Customer details: {c1_info}")


