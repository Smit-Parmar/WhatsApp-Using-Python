from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from tkinter import messagebox as mb
import time
import keyboard
from datetime import datetime
import wikipedia as wk
from bs4 import BeautifulSoup
import requests
import re

oldmessage=''
name=input('Enter the name of user :')
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=./User_Data')
driver=webdriver.Chrome('D:\Sofware_installation\Python 3.7\chromedriver.exe',options=option)
driver.get('https://web.whatsapp.com/')
input('Press Enter after scanning QR code/Loading page')
user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
print("Enter your choice")
print("1:Message")
print("2:Send attachment")
print("3:Bot action")
argument=int(input())

def messagesend():
    oldmsg=""
    msg=input('enter the message :')
    print("press space for send another message")
    send(msg)
    while True:
        try:     
            #receivedmsg = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span')
            newmsg = driver.find_elements_by_class_name("_3zb-j")
            length=len(newmsg)
            msg=((newmsg[length-1].text).lower())
            if keyboard.is_pressed("space"):
                usermsg = input("Enter message to be sent: ")
                send(usermsg)
            if msg!=oldmsg :
                print(msg)
            #newmessage=input()
            #send(newmessage)
            #oldmessage=newmessage
                oldmsg=msg
        except Exception as e:
            print(e)
            pass

    
def send(message):
    msg=message
    msg_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)#for sending message in message box

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
   
def bsend(message): #message send by bot Bot 
    msg="Cyborg: %s"%message
    msg_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)#for sending message in message box

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
   
def attachimage():
    print("Send Image or video")
    sourcepath=input("Enter a path for yourfile :")
    attachment_box=driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
    attachment_box.click()
    image_box=driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(sourcepath)
    print("reached here")
    sleep(3)
    #send_attach_button=driver.find_element_by_class_name('_3hV1n yavlE')
    send_attach_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_attach_button.click()

def attachdocument():
    print("Send Document")
    sourcepath=input("Enter a path for yourfile :")
    attachment_box=driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
    
    attachment_box.click()
    Document_box=driver.find_element_by_xpath('//input[@accept="*"]')
    Document_box.send_keys(sourcepath)
    print("reached here")
    sleep(3)
    #send_attach_button=driver.find_element_by_class_name('_3hV1n yavlE')
    send_attach_button=driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_attach_button.click()
def bot():
    oldmsg=""
    while True:
        try:     
            #receivedmsg = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span')
            newmsg = driver.find_elements_by_class_name("_3zb-j")
            length=len(newmsg)
            msg=((newmsg[length-1].text).lower())
            if keyboard.is_pressed("space"):
                usermsg = input("Enter message to be sent: ")
                send(usermsg)
            if msg!=oldmsg :
                print(msg)
            #newmessage=input()
            #send(newmessage)
            #oldmessage=newmessage
                if 'cyborg' in msg:
                    pass
                else:
                    
                    if "hii" in msg or "hi" in msg  or "hyy" in msg or "hello" in msg:
                        bsend("Hii ")
                        
                    if 'lol' in msg:
                        bsend(":-)")
                        
                    if "how are you" in msg or "h r u" in msg or "how are u" in msg:
                        bsend("I am always fine")
                        
                    if "what are you doing" in msg :
                        bsend("just replying you as fast as i can")
                        
                    if "about me" in msg:
                        bsend("Your phone does not have enough memory to hold my words which i will say about you. You are such a skillful person ")

                    if "who are you" in msg:
                        bsend("Lets be honest..I am whats app bot of smit")
                        
                    if "time" in msg:
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        bsend(str(current_time))
                    
                    if "bye" in msg:
                        bsend("bye")
                        exit()

                    if "news" in msg:
                        bsend("Just hold on i am gathering right information...")
                        url="https://timesofindia.indiatimes.com/home/headlines"
                        page=requests.get(url)
                        soup=BeautifulSoup(page.text,'html.parser')
                        headline=soup.findAll(class_='w_tle')
                        bsend("here are your news")
                        count=0
                        for n in headline[:3]:
                            count+=1
                            send(n.text)

                    if "tell me about" in msg:
                        msg=msg.replace("tell me about","")
                        bsend("your information about %s is on the way"%msg)
                        summary =wk.summary(msg,sentences=2)
                        bsend(summary)

                    if "where is smit" in msg:
                        bsend("smit is not available right now till i can help you by serving news,facts,wikipedia you just have to give me command")
                        bsend("news")
                        bsend("facts")
                        bsend("tell me about (topic) you want to know")

                    if "fact" in msg:
                        bsend("getting interesting fact for interesting person")
                        url="https://bestlifeonline.com/world-facts/"
                        page=requests.get(url)
                        soup=BeautifulSoup(page.text,'html.parser')
                        facts=soup.findAll(class_='title')
                        for f in facts[:10]:
                            bsend(f.text)
                    if "Thank you" in msg:
                        bsend("Happy to help")
            oldmsg=msg
            sleep(3)
        except Exception as e:
            print(e)
            pass
    
if argument==1:
    messagesend()
if argument==2:
    print("A.Image/Video")
    print("B.Document")
    take=input()
    if take=='A' or take=='a':
        attachimage()
    if take=='B' or take=='b':
        attachdocument()
    
if argument==3:
    bot()
    










