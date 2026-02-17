from machine import Pin
import time

#first i = [1,0,0,0] , i[0]
in1 = Pin(5,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)


step = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
step2= [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]



while True:
    for k in range(500):
        for i in step:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
            
    for p in range(500):
        for o in step2:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
      
