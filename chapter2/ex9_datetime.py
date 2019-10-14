import sys
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt

now = QDate.currentDate()  # currentDate() 현재 날짜를 반환
print(now.toString())  # toString() 메소드를 통해 문자열로 출력

print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))


time = QTime.currentTime()  # currentTime() 현재 시간 반환
print(time.toString())

print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))


datetime = QDateTime.currentDateTime()  # currentDateTIme() 메소드는 현재 날짜와 시간 반환
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))
