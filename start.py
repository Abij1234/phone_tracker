import os

os.system("""

pack=(figlet)

for i in "${pack[@]}"; do
if ! hash $i; then
printf "\033[1;31mINSTALLING BANNER \033[00m\n"
pkg install $i
else
figlet phone_tracker
fi
done""")


os.system("""

if [[ ! -d $PREFIX/lib/python3.10/site-packages/phonenumbers ]]; then
printf "\033[1;31mBASIC LIBRARY NOT FOUNDED SO INSTALLING \033[00m\n"
pip install phonenumbers
fi""")

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

print("\n")
number = input("\033[1;36mEnter your target phone number with country code==> \033[00m")

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

choice = input("\033[1;31mwould you want to check mobile service[y/n]==> \033[00m")

if choice == 'y':
    service_number = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_number, "en"))

elif choice == 'n':
    print("\033[1;34mOK THANKS FOR USING THE TOOL \033[00m")

else:
    print("\033[1;31mSELECT A VALID OPTION \033[00m")

