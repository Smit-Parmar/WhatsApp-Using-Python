from selenium import webdriver
driver=webdriver.Chrome('D:\Sofware_installation\Python 3.7\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name=input('Enter the name of user :')
msg=input('enter the message :')
input('Enter anything after scanning QR code')

user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
msg_box.send_keys(msg)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()


while True:
    try:

        receivedmsg = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span')
        #newmsg = driver.find_elements_by_class_name("_3zb-j")  
        print(receivedmsg)
    except Exception as e:
        print(e)
        pass










