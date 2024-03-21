from opencage.geocoder import OpenCageGeocode

key = '2157c7fc42d549eb819c657bc18d6552'
geocoder = OpenCageGeocode(key)
query = "ABD road, India"
result = geocoder.geocode('london', no_annotations=1 , language ='en')
print(result)