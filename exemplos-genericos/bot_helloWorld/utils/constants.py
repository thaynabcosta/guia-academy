import os

APP_PATH =  r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk'

WAITING_TIME = 2000
INTERVAL_KEYS = 2

TEXT = "Hello World"
FILE_NAME = os.path.join(os.getcwd(), "hello-world.txt")