from machine import Pin, I2C
from i2c_lcd import I2cLcd
from time import sleep
import dht

DEFAULT_I2C_ADDR = 0x27
sensor = dht.DHT11(Pin(2))  # 2번 핀 사용

def setup():
    global lcd
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)  # SDA는 0번핀, SCL은 1번 핀
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

def loop():
    while True:
        sensor.measure()
        temp = sensor.temperature()  # 온도 측정
        hum = sensor.humidity()  # 습도 측정
        print(f"Temperature: {temp}°C  Humidity: {hum}%")

        lcd.move_to(0, 0)
        lcd.putstr(f"Temp: {temp}°C")
        lcd.move_to(0, 1)
        lcd.putstr(f"Humi: {hum}%")
        sleep(1)

setup()
loop()