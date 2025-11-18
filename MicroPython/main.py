from machine import Pin, ADC
import time

#PIN SETUP
ldr = ADC(0)    #LDR PIN
led1 = Pin(15, Pin.OUT) #HIJAU
led2 = Pin(13, Pin.OUT) #HIJAU
led3 = Pin(12, Pin.OUT) #HIJAU
led4 = Pin(14, Pin.OUT) #KUNING
led5 = Pin(16, Pin.OUT) #MERAH
# 15 = GPIO15 --> D8
# 13 = GPIO13 --> D7
# 12 = GPIO12 --> D6
# 14 = GPIO14 --> D5
# 16 = GPIO16 --> D0

#THRESHOLDS SETUP
#LDR Value 0 -----------------------------------------> 1024 (5V)
T1 = 1024
T2 = 819
T3 = 614
T4 = 409
T5 = 204

#ALERT FUNCTION KALAU VALUE NYENTUH DI <= T5
def alert():
    for _ in range(1):
        led5.on()
        time.sleep_ms(100)
        led5.off()
        time.sleep_ms(200)

#MAIN LOOP
while True:
    #VARIABEL UNTUK MEMBACA NILAI LDR
    value = ldr.read()
    
    # MATIKAN SEMUA LED TERLEBIH DAHULU
    led1.off(); led2.off(); led3.off(); led4.off(); led5.off()
    
    #BARU NYALAKAN LED BERDASARKAN NILAI LDR
    if value == T1: #<= 1024
        led1.on()
    if value <= T2: #<= 819
        led2.on()
    if value <= T3: #<= 614
        led3.on()
    if value <= T4: #<= 409
        led4.on()
    if value <= T5: #<= 204
        alert()

    time.sleep_ms(5)

# DOCUMENTATION
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