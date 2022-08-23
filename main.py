# QUESTION 1
import time 
class  Time(object):

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        t3 = Time(0, 0) # creating new object
        t3.hours = t1.hours + t2.hours # sum of hours
        t3.minutes = t1.minutes + t2.minutes # sum of minutes
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3

    def displayTime(self):
        print("Time is %d hours and %d minutes" %(self.hours, self.minutes))

    def displayMinutes(self):
        print((self.hours * 60) + self.minutes, "minutes")

a = Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinutes()

print (" \n\nThe next answer will begin now")

# QUESTION 2
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)