import time
import webbrowser

counter = 0

print("This program started at"+time.ctime())
url = "https://www.youtube.com/watch?v=_Yhyp-_hX2s"

#The program will run every 30 minutes for 12 occurences
while(counter < 4):
    time.sleep(1*1800)
    webbrowser.open(url, new=1)
counter = counter + 1
