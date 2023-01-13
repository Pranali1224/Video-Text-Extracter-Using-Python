from youtube_transcript_api import YouTubeTranscriptApi as yta
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.service import Service
from time import sleep
from tkinter import Tk

vid_id=input("Paste Your Youtube Video Link Here....!!!! : ")
what_to_replace=""
for i in vid_id:

    if i == "=":
        break
    else:
        what_to_replace = what_to_replace + str(i)

vid_id=vid_id.replace(what_to_replace,"")

required_id=vid_id[1:14]

data=yta.get_transcript(required_id)

transcript = ""
for words in data:
    for key,val in words.items():
        if key == "text":
            transcript = transcript +"\n"+val
#print(transcript)
t = transcript.split(" ")
file_name_gen = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
extracted_text = " ".join(t)
print(extracted_text)
ext_len=len(extracted_text)
print(ext_len)
mar_trns=""
if ext_len<=3900:
    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        s = Service("chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=s)
        driver.maximize_window()
        driver.get("https://www.google.com/search?q=google+translate+english+to+marathi&rlz=1C1RXQR_enIN1018IN1018&oq=google+translate+english+to+marathi&aqs=chrome..69i57j69i64l3.7694j0j7&sourceid=chrome&ie=UTF-8")
        sleep(2)
        button = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter text']")
        button.click()
        sleep(1)
        button.send_keys(extracted_text)
        button_0 = driver.find_element(By.XPATH,"//body/div/div[@jsmodel=' ROaKxe']/div/div/div[@role='main']/div/div[@data-hveid='CAYQBA']/div/div/div/div/div[@data-hveid='CAUQAQ']/div/g-expandable-container/div/div[@jscontroller='tZEiM']/div/div/div/div/div/div/span[@title='Copy']/span[1]")
        button_0.click()
        sleep(3)
        driver.close()
        x = Tk().clipboard_get()
        mar_trns = mar_trns + (x)
    except:
        print("sorry encountered an error")
else:
    print("yet to code for it")

print(mar_trns)
with open(f'Extracted_Text_Or_Caption_{file_name_gen}.txt', 'w', encoding='utf-8') as f:
    f.write(mar_trns)
    f.write("\n"+ extracted_text)
    f.close()
