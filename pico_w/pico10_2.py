import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('11T','0972830352')

while not wlan.isconnected() and wlan.status() >= 0:
    print("等待連線中....")
    time.sleep(1)
    
    
print(wlan.ifconfig())   