
from datetime import datetime
import time
import schedule


def everymin():
    day = datetime.today().strftime("%A")
    time = datetime.now().strftime("%H:%M")
    print(time)

schedule.every().minute.do(everymin)


while True:

    schedule.run_pending()
    time.sleep(1)
