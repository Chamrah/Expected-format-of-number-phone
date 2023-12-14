import re

def MobilePhone(Num):
    patt = re.compile(r'\d{2}-\d{3}\d{4}')
    if patt.search(Num):
        print("The phone number is in the expected format.")
    else:
        print("The phone number is not in the expected format.")

