import phonenumbers
from phone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder,geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))


