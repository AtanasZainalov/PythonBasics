 # Dictionary  has a KEY not an index, but it works the same way
customer1 = {
    "CustomerID": "ALFKI",
    "CompanyName": "Alfreds Futterkiste",
    "ContactName": "Maria Anders",
    "ContactTitle": "Sales Representative",
    "Address": "Obere Str. 57",
    "City": "Berlin",
    "Region": None,
    "PostalCode": 12209,
    "Country": "Germany",
    "Phone": "030-0074321",
    "Fax": "030-0076545",
    "isActive": True
}

customer2 = {}
customer3 = dict()
print(customer1)

print('#### 1.Read (ACCESS THE VALUES)E ########################')
print(f"ID of the customer : {    customer1['CustomerID']    }"   )
print(f"Name of the customer : {    customer1['CompanyName']    }"   )
print(f"Country of the customer : {    customer1['Country']    }"   )

print('#### 2.Update ########################')

print(f' Customers city before update  {customer1['City']}')
customer1['City'] = 'Frankfurt'
print(f' Customers city after update  {customer1['City']}')
print(" Adding new info - key-valuer pair .....")
customer1['isActive'] = False
print(f' SetDefault fir is Active {customer1}')
customer1.setdefault("isActive",True)
print(customer1)
print('#### 3.Delete ########################')

del customer1['Fax']
customer1['Fax'] = '9999999'
print(customer1)
print('#### 4.Looping through the dictionary ########################')



#H/W given a phrase, count each how many times easch letter was used
#H/W given a phrase, count each how many times vowels were used
# use dictionary ,for loop , if condition, setdefault()

##