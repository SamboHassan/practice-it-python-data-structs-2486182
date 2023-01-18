"""
Reading CSV files

* data/Customer.csv
* Use a csv reader
* Use first row as field names for named turple
* Create named turple for remainig rows

"""

from collections import namedtuple
from csv import reader


def main():
    with open("data/Customer.csv", "r") as open_csv:
        read = reader(open_csv)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)
            print(person.CustomerID, person.FirstName, person.LastName)
    return


if __name__ == "__main__":
    main()
