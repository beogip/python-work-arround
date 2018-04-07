import webbrowser
import time

total_breaks = 3
current_breaks = 0
break_time = 10
print("This program started on "+ time.ctime())
while(current_breaks < total_breaks):
  time.sleep(break_time)
  webbrowser.open("https://github.com/")
  current_breaks = current_breaks + 1
