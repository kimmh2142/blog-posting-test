import sys

import schedule
import time
import datetime


# 스케쥴 모듈이 동작시킬 코드 : 현재 시간 출력
def test_function():
    now = datetime.datetime.now()
    print("test code- 현재 시간 출력하기")
    print(now)

#프로그램을 종료시키기 위한 함수
def exit():
    print("function exit")
    sys.exit()

#3초마다 동작
schedule.every(3).seconds.do(test_function)

#1시간마다 동작
#schedule.every(1).hour.do(test_function)

#매일 특정시간에 동작(10:00)
schedule.every().day.at("10:00").do(test_function)

#하루마다 동작
#schedule.every(1).days.do(test_function)

#매주 월요일에 동작
#schedule.every().monday.do(test_function)

# 무한 루프를 돌면서 스케쥴을 유지한다.
while True:
    schedule.run_pending()
    time.sleep(1)