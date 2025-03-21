from machine import Pin, I2C  
from i2c_lcd import I2cLcd  
from time import sleep 
import dht  


DEFAULT_I2C_ADDR = 0x27  # LCD I2C 주소
sensor = dht.DHT11(Pin(2))  # DHT11 센서 (GPIO 2번 핀 사용)

def setup():
    global lcd
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # I2C 통신 초기화
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)  # 16x2 LCD 설정

# 온습도를 측정하고 LCD에 표시하는 반복 함수
def loop():
    while True:
        sensor.measure()  # 온습도 측정
        temp = sensor.temperature()  # 온도 값 가져오기
        hum = sensor.humidity()  # 습도 값 가져오기
        
        print(f"Temperature: {temp}°C  Humidity: {hum}%")  # 시리얼 모니터 출력

        lcd.move_to(0, 0)  
        lcd.putstr(f"Temp: {temp}°C")  # 온도 표시

        lcd.move_to(0, 1) 
        lcd.putstr(f"Humi: {hum}%")  # 습도 표시

        sleep(1)  

setup()

loop()
