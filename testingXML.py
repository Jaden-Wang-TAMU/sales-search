import xml.etree.ElementTree as ET 
import dateutil.parser

# xml_file=ET.parse('sales-data.xml') # set up
# rt=xml_file.getroot() # getting the root, in this case its people

xml_file=ET.parse('sales-data.xml')
rt=xml_file.getroot()
Dict={}
for person in rt.findall('./person'):
    date = person.find('timestamp').text
    ts = str(dateutil.parser.parse(date))
    print(ts[0:4]+", "+ts[5:7]+", "+ts[8:10])
#     if (cat in Dict.keys()):
#         Dict[cat]=Dict[cat]+float(person.find('amount').text)
#     else:
#         Dict.update({cat:float(person.find('amount').text)})
# sortedDict={}
# for x in Dict.keys():
#     first="ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
#     for key in Dict.keys():
#         if(key<first and key not in sortedDict):
#             first=key
#     sortedDict.update({first:Dict.get(first)})
# print(sortedDict)

# for person in rt.findall('./person'):
#     id = person.find('id')

# val = int('1')
# some_string = str(123)
# flt = float('1.23')

# # ts = dateutil.parser.parse('2021-09-21')
# # print(ts) # ts is a datetime object
# amount=0
# for person in rt.findall('./person'):
#     cat = person.find('category').text
#     if(cat=="Electronics"):
#         amount=amount+float(person.find('amount').text)
# print(amount)
