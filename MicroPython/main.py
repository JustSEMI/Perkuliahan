from machine import Pin, ADC
import time

ldr = ADC(0)
led1 = Pin(15, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(12, Pin.OUT)
led4 = Pin(14, Pin.OUT)
led5 = Pin(16, Pin.OUT)

T1 = 1024
T2 = 819
T3 = 614
T4 = 409
T5 = 204

def alert():
    for _ in range(1):
        led5.on()
        time.sleep_ms(100)
        led5.off()
        time.sleep_ms(200)

while True:
    value = ldr.read()
    
    led1.off(); led2.off(); led3.off(); led4.off(); led5.off()
    
    if value == T1:
        led1.on()
    if value <= T2:
        led2.on()
    if value <= T3:
        led3.on()
    if value <= T4:
        led4.on()
    if value <= T5:
        alert()

    time.sleep_ms(5)

'''
LDR Value 0 ----------------------------------------- 1024
|-------|-------|-------|-------|--------|
 H1       H2      H3      K4       M5

H1 : [■____] LED1  
H2 : [■■___] LED1-LED2  
H3 : [■■■__] LED1-LED3  
K4 : [■■■■_] LED1-LED4  
M5 : [■■■■■] LED1-LED5
'''

'''
+------------------+------------------------------+
|  Rentang LDR     | LED yang Menyala             |
+------------------+------------------------------+
| 0   - 204        | LED1                         |
| 205 - 409        | LED1, LED2                   |
| 410 - 614        | LED1, LED2, LED3             |
| 615 - 819        | LED1, LED2, LED3, LED4       |
| 820 - 1024       | LED1, LED2, LED3, LED4, LED5 |
+------------------+------------------------------+
'''