from botcity.core import DesktopBot, Backend
from botcity.maestro import *

from utils.remove_files import remove_txt
from utils.constants import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    remove_txt()

    bot = DesktopBot()

    bot.execute(APP_PATH)
    bot.wait(WAITING_TIME) 

    bot.kb_type(TEXT, INTERVAL_KEYS) 
    bot.control_s()
    bot.paste(FILE_NAME)
    bot.enter()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()