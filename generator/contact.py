from model.contact import Contact
from model.contact import Monate
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    symbolList = [random.choice(symbols) for i in range(random.randrange(maxlen))]
    return prefix + "".join(symbolList)

testdata= [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                                                   company="", address="", home="", mobile="", work="", fax="",
                                                   email="", email2="", email3="", homepage="", bday="", bmonth="-",
                                                   byear="", aday="",
                                                   amonth="-", ayear="", address2="", phone2="", notes="")] + [
           Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                   lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                   title=random_string("title", 10), company=random_string("company", 10),
                   address=random_string("address", 10), home=random_string("home", 10),
                   mobile=random_string("mobile", 10), work=random_string("work", 10), fax=random_string("fax", 10),
                   email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
                   homepage=random_string("homepage", 10), bday=str(random.randint(1,27)), bmonth=Monate[random.randint(0,11)],
                   byear=random.randint(1600,2027), aday=str(random.randint(1,27)), amonth=Monate[random.randint(0,11)],
                   ayear=random.randint(1600,2027), address2=random_string("address2", 10), phone2=random_string("phone2", 10),
                   notes=random_string("notes", 10))
    for i in range(n)
]

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
file = os.path.join(dirname, "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))