import phonenumbers

from num import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
yourloccation = geocoder.description_for_number(pepnumber , "en")
print(yourloccation)