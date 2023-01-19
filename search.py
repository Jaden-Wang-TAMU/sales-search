import xml.etree.ElementTree as ET 
import dateutil.parser

class Search:
    
    def round_dictionary(self, dict, decimals=2):
        """
        Rounds all values to no more than 2 decimal places. You'll
        need to call this on your dictionaries before returning to
        take care of any floating point weirdness.

        Note: You'll only need this in the methods that return
        dictionaries with a floating point value. 
        """
        for key in dict:
            dict[key] = round(dict[key], 2)
        return dict 

    def amount_spent(self, category):
        """
        Returns the amount spent in category
        """
        xml_file=ET.parse('sales-data.xml')
        rt=xml_file.getroot()
        amount=0
        for person in rt.findall('./person'):
            cat = person.find('category').text
            if(cat==category):
                amount=amount+float(person.find('amount').text)
        return amount
            
    def spent_by_gender(self):
        xml_file=ET.parse('sales-data.xml')
        rt=xml_file.getroot()
        mAmount=0
        fAmount=0
        for person in rt.findall('./person'):
            gen = person.find('gender').text
            if(gen=="M"):
                mAmount=mAmount+float(person.find('amount').text)
            if(gen=="F"):
                fAmount=fAmount+float(person.find('amount').text)
        Dict={"M": mAmount, "F": fAmount}
        return self.round_dictionary(Dict)
        
    def all_categories(self):
        xml_file=ET.parse('sales-data.xml')
        rt=xml_file.getroot()
        Dict={}
        for person in rt.findall('./person'):
            cat = person.find('category').text
            if (cat in Dict.keys()):
                Dict[cat]=Dict[cat]+float(person.find('amount').text)
            else:
                Dict.update({cat:float(person.find('amount').text)})
        sortedDict={}
        for x in Dict.keys():
            first="ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
            for key in Dict.keys():
                if(key<first and key not in sortedDict):
                    first=key
            sortedDict.update({first:Dict.get(first)})
        return self.round_dictionary(sortedDict)

    def spent_between(self, start_date, end_date):
        """
        Returns the sum of all sales between start_date
        and end_date, inclusive
        """
        xml_file=ET.parse('sales-data.xml')
        rt=xml_file.getroot()
        amount=0
        for person in rt.findall('./person'):
            date = person.find('timestamp').text
            ts = dateutil.parser.parse(date)
            if(ts>=start_date and ts<=end_date):
                amount=amount+float(person.find('amount').text)
        return amount

    