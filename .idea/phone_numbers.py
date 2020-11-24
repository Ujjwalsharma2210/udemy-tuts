import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

phone_number = phonenumbers.parse("Enter phone number with country code: ")

country = geocoder.description_for_number(phone_number, 'en')
carrier_name = carrier.name_for_number(phone_number, 'en')
