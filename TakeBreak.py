import time
import webbrowser


break_count = 0
total_count = 5

print ("Cas je "+time.ctime())

while (break_count < total_count):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3O1_3zBUKM8")
    break_count = break_count+1


