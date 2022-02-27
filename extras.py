import re

def appendMultipleItems(l = [], *args):
    for arg in args:
        l.append(arg)
    return l

def cleanPriceItem(price):
    return int(''.join(re.findall('[0-9]', price)))

def cleanBedAndBath(s):
    l = list()
    bed, bath = s.split(',')
    bed = bed.split(':')[1]
    bath = bath.split(':')[1]
    bed_and_bath = appendMultipleItems(l, int(bed), int(bath))
    return bed_and_bath
