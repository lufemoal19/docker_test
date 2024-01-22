import pyautogui as pg
import pyperclip as pyc
import pandas as pd
import webbrowser as web
import time
import subprocess

emojis = '🌸💖🌺😻🌹😍🌻🥰🌷'
white_square = '▫️'
data = pd.read_csv('number_list.csv')
print(data)

def draw_heart(emoji) -> str:
    draw = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    heart = ''

    for row in draw:
        for col in row:
            if col == 1:
                heart += emoji
            else:
                heart += white_square
        heart += '\n'
    # print(heart)
    # copy_to_clipboard(heart)
    return heart

def send_message(messages):
    cellphone = data.loc[0, 'cellphone'].astype(str) # cast to string
    whatsapp_path = f'https://web.whatsapp.com/send?phone={cellphone}'
    for i in range(messages):
        time.sleep(5)
        draw = draw_heart(emojis[i % 10])
        print(draw)
        pg.click(329, 22)
        web.open(whatsapp_path+f'&text={draw}')
        pg.press('enter')

    time.sleep(1.5)
    pg.hotkey('ctrl', 'w') # close window
    time.sleep(1)

def main():
    messages = int(input('Message number: '))
    send_message(messages)
    

if __name__ == '__main__':
    main()
