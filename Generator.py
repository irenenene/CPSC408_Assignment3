import csv
import random
import string
import sys
import datetime
from datetime import timedelta
from faker import Faker
fake = Faker()


# https://stackoverflow.com/a/11749761
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for z in range(y))


def gen_employees():
    # Create 5 to 20 random employees
    numEmployees = random.randint(5, 20)
    Employees = []
    for x in range(numEmployees):
        Employee = {
            "id": x,
            "fName": fake.first_name(),
            "lName": fake.last_name()
        }
        Employees.append(Employee)

    return Employees


def gen_suppliers():
    # create 20-100 random Suppliers
    numSuppliers = random.randint(20, 100)
    Suppliers = []
    for x in range(numSuppliers):
        addIt = True
        sid = "SUP-" + str(random.randrange(0, 10000)).zfill(4)
        Supplier = {
            "sid": sid,
            "sName": fake.company(),
            "sAddress": fake.address()
        }
        for s in Suppliers:
            if s["sid"] == sid:
                addIt = False

        if addIt:
            Suppliers.append(Supplier)

    return Suppliers


def gen_customers():
    # create 10-30 random Customers
    numCustomers = random.randint(10, 30)
    Customers = []
    for x in range(numCustomers):
        Customer = {
            "cid": x,
            "cName": fake.company(),
            "cAddress": fake.address()
        }
        Customers.append(Customer)

    return Customers


def gen_companies(cust):
    # create 5-100 random Companies with an associated Customer
    numCompanies = random.randint(5, 100)
    Companies = []
    for x in range(numCompanies):
        addIt = True
        compID = random_char(4)+"-"+str(random.randint(100, 99999)).zfill(5)
        Company = {
            "compId": compID,
            "compName": fake.company(),
            "compAddress": fake.address(),
            "customer": random.randint(0, len(cust)-1)  # the Customer this Company is associated with
        }
        for c in Companies:
            if c["compId"] == compID:
                addIt = False

        if addIt:
            Companies.append(Company)

    return Companies


def gen_records(num_records):
    operators = gen_employees()
    suppliers = gen_suppliers()
    customers = gen_customers()
    companies = gen_companies(customers)

    Records = []
    records_left = num_records
    batch_num = 0
    # create a record
    while records_left > 0:
        batch_num += 1
        batch_size = random.randrange(0, 10)
        batch_create = fake.date_time_this_decade()
        batch_release = batch_create + fake.time_delta(end_datetime=timedelta(days=4))
        ws = fake.local_latlng(country_code='US')[2][:20]  # PC Workstation names
        boolpaper = random.getrandbits(1)
        batchtype = random.choice(['Paper', 'Email'])
        for x in range(batch_size):

            record = {
                "batchid": batch_num,
                "documentid": x,
                "workstation": ws,
                "createTime": batch_create.strftime('%Y-%m-%d %H:%M:%S'),
                "releaseTime": batch_release.strftime('%Y-%m-%d %H:%M:%S'),
                "isPaper": boolpaper,
                "batchType": batchtype,

            }

            if records_left > 0:
                Records.append(record)
                records_left -= 1
            else:
                break

    print(Records)

    return Records


def write_records(rec, file_name):
    fieldnames = rec[0].keys()
    with open(file_name, 'w') as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(rec)


num = int(sys.argv[1])
fName = sys.argv[2]
record_list = gen_records(num)
write_records(record_list, fName)