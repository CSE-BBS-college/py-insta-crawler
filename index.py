import asyncio
import requests 
from pyppeteer import launch
import random
import string
import os.path  

# def download_reel():


def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str
    # print("Random string of length", length, "is:", result_str)

task_input = input("Welcome to Py-instagram-crawler.\n [1]-Download Reels\n")
link = input("Please enter the valid link \n")


async def main(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    page_title = await page.title()
    title = page_title.split('on')[0] 
    name_of_file = f"{title.title().rstrip()}-{get_random_string()}"
    file_name = os.path.join(os.path.expanduser('~'),'Videos', name_of_file+".mp4") 
   
    print(file_name)
    # await page.screenshot({'path': 'example.png'})
    source = await page.querySelector("video.tWeCl")
    video_link = await page.evaluate('(source) => source.src', source)
    
    # print(title)

    print(f"\n ###################################### \n # \n # Downloading file:{file_name} \n # \n #####################################")           
    # create response object 
    r = requests.get(video_link, stream = True) 
          
    # download started 
    with open(file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
          
    print(f"\n Downloaded file:{file_name}")
      
    await browser.close()

asyncio.get_event_loop().run_until_complete(main(link))