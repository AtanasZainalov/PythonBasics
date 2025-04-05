import yaml

from utilities import read_yaml_file

customer_path= "data/customers.yml"
with open(customer_path, 'r') as file:
    customers = yaml.safe_load(file)

print(customers)
print(customers['customer1']['CompanyName'])
print(customers['customer1']['Region'])
print(customers['customer1']['PhoneNumbers'])
print(customers['customer1']['PhoneNumbers'][0])
print("__________________________")


config_path = ('./data/config.yml')
data = read_yaml_file(config_path)
print(f'link for dev env: {data['DEV']} ')