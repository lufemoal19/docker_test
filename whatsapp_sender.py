import pandas as pd
import pyautogui as pg
import webbrowser as web
import time

data = pd.read_csv("client_list.csv")
print(data)

for i in range(len(data)):

    # Step 0: get data from csv! 

    cellphone = data.loc[i, 'cellphone'].astype(str) # cast to string
    name = data.loc[i, 'name']
    product = data.loc[i, 'product']
    price = data.loc[i, 'price']

    # Step 0.1: build message! 

    message = f'Hello, {name}!\nThanks for buying {product}.\nPrice: ${price}\n'

    # Step 1: Open new window to access WhatsApp Web! 

    whatsapp_path = f'https://web.whatsapp.com/send?phone={cellphone}&text={message}'

    web.open(whatsapp_path) # if open on Mozilla
    
    mozilla_path = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe %s'
    web.get(mozilla_path).open(whatsapp_path) # else open Mozilla

    # Step 2: send message!

    time.sleep(8)
    pg.click(329, 22)
    time.sleep(2)
    pg.press('enter')

    # Step 3: close window!

    time.sleep(1.5)
    pg.hotkey('ctrl', 'w') # close window
    time.sleep(1)