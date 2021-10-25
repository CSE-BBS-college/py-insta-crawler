from requests_html import HTMLSession
import random
import requests
import string
import os.path  

def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str
    # print("Random string of length", length, "is:", result_str)

# Initial input function
def get_opration_from_user():
    a = int(input(" [1]-Download Reels\n [0]-To exit\n "))
    return a

###########
# Main program starts
###########
got_op_code =  False
print("Welcome to Py-instagram-crawler")
while got_op_code == False :
    task_input = get_opration_from_user()
    #print(task_input)
    if task_input == 1:
        got_op_code = True
        link = input("Please enter the valid link \n ")
        if link == '':
            print("Invalid link")
    elif task_input == 0:
        exit()
    else:print("\n**************************************\n#\n# Invalid value entered. Try again!\n#\n**************************************\n")
        # task_input=get_opration_from_user()

###########
# Getting video link from the screped page
###########

# test_URL = "https://www.instagram.com/reel/CU46BpAIAw0/?utm_source=ig_web_copy_link"
session = HTMLSession()
r = session.get(link)
r.html.render()

page_title=r.html.find('title',first=True).text
link_obj=r.html.find('video.tWeCl',first=True).attrs
video_link = link_obj["src"]

###########
#  Genrating a random filename for the file
###########

title = page_title.split('posted')[0] 
name_of_file = f"{title.title().rstrip()}-{get_random_string()}"
file_name = os.path.join(os.path.expanduser('~'), 'Videos', name_of_file+".mp4")


# print(file_name)

###########
# Getting video link from the screped page
###########


print(f"\n ###################################### \n # \n # Downloading file:{file_name} \n # \n #####################################")           
# create response object 
r = requests.get(video_link, stream = True) 
          
# download started 
with open(file_name, 'wb') as f: 
    timer_amount=1
    for chunk in r.iter_content(chunk_size = 1024*1024): 
        if chunk: 
            f.write(chunk)
            print(" *"*timer_amount)
            timer_amount+=1
             
          
print(f"\n Downloaded file at :{file_name} ")
