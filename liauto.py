import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os,sys,pyperclip
import pyautogui

login='you lined in username here'
password='your password here'

# opening automated browser window
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'your\path\to\chromedriver.exe')

# opening linkedin in ABW
driver.get("https://www.linkedin.com/")
time.sleep(4)

# logging in
driver.find_element_by_name("session_key").send_keys(str(login))
driver.find_element_by_name("session_password").send_keys(str(password))
time.sleep(2)
pyautogui.click(1586,545)
print("successfully logged in")


filename='1'


def myfun():
    
     # generating copies urls in list
     urls=pyperclip.paste()
     urls=urls.split('\n')

     

     for url in urls:
          driver.get(url)
          time.sleep(20)
          pyautogui.keyDown('ctrlleft');pyautogui.press('p');
          pyautogui.keyUp('ctrlleft');
          time.sleep(4)
          pyautogui.click(1414,869)
          time.sleep(4)
          pyautogui.click(180,572);pyautogui.write(c)
          c=str(int(c)+1)
          time.sleep(3)
          pyautogui.click(740,672)
          time.sleep(3)



x=True
while(x):
    i=int(input("Enter 0 if you have copies new urls"))
    if i==0:
        myfun()
    q=input(r"Do you want to continue(y/n)")
    if q=='y':
        x=True

        
    if q=='n':
        x=False
    

    
