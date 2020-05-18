from selenium import webdriver
from selenium.webdriver.chrome.options import Options
oldmsg=""
name=input('Enter the name of user :')
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=./User_Data')
driver=webdriver.Chrome('D:\Sofware_installation\Python 3.7\chromedriver.exe',options=option)
driver.get('https://web.whatsapp.com/')
input('Press Enter after scanning QR code/Loading page')
user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
def send(message):
    msg=message
    msg_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)

    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()
    
msg=input('enter the message :')
send(msg)



while True:
    try:

        #receivedmsg = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span')
        newmsg = driver.find_elements_by_xpath("_3zb-j")
        length=len(newmsg)
        msg=((newmsg[length-1].text).lower())
        if msg!=oldmsg:
            print(msg)
        newmessage=input()
        send(newmessage)
        oldmsg=msg
        '''
            m=input()
            if m:
                msg_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
                msg_box.send_keys(m)
            '''
                
        
            
            
    except Exception as e:
        print(e)
        pass










