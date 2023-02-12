import schedule
import time
import datetime


# 스케쥴 모듈이 동작시킬 코드 : 현재 시간 출력
def test_function():
    now = datetime.datetime.now()
    print("test code- 현재 시간 출력하기")
    print(now)

#1시간마다 동작
schedule.every(1).hour.do(test_function)

#하루마다 동작
#schedule.every(1).days.do(test_function)

#매주 월요일에 동작
#schedule.every().monday.do(test_function)

# 무한 루프를 돌면서 스케쥴을 유지한다.
while True:
    schedule.run_pending()
    time.sleep(1)