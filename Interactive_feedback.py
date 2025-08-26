from machine import Pin, PWM
import time
import urandom
from machine import I2C
import lcd1602  # Ensure this is the correct import
import math

# Initialize I2C for LCD
i2c = I2C(1, scl=Pin(7), sda=Pin(6))  # Adjust pins for your setup
lcd = lcd1602.LCD(addr=0x27)  # Create LCD instance using correct class



# Function to display a waveform based on frequency
def display_wave(frequency):
    # Calculate the number of oscillations we want to simulate
    max_wave_width = 16  # Number of characters that can fit on the screen (16 columns)
    wave_period = 10  # Period of the wave (time before repeating)

    # Create the wave pattern
    wave = [' '] * max_wave_width  # Start with empty spaces

    # The position of the '#' character will change based on a sine wave
    for i in range(max_wave_width):
        # Calculate the vertical sine wave position
        sine_value = math.sin((i + (time.ticks_ms() / 1000.0 * frequency)) * 2 * math.pi / wave_period)
        wave_pos = int((sine_value + 1) * 7)  # Map sine wave to positions between 0 and 15
        wave[wave_pos] = '#'

    # Display the frequency and the wave on the LCD
    lcd.clear()
    lcd.write(0, 0, f"Freq: {frequency}Hz")  # Show frequency on line 1
    lcd.write(0, 1, ''.join(wave))  # Show wave pattern on line 2




# Initialize ultrasonic sensor pins
TRIG = Pin(17, Pin.OUT)
ECHO = Pin(16, Pin.IN)

# Initialize PWM for buzzer on pin 15
buzzer = PWM(Pin(15))

# RGB LED initialization using PWM on pins 13, 12, and 11 (for red, green, blue)
red = PWM(Pin(13))
green = PWM(Pin(12))
blue = PWM(Pin(11))

# Set the PWM frequency for each color (1kHz)
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# Function to measure distance using the ultrasonic sensor
def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while not ECHO.value():
        pass
    time1 = time.ticks_us()
    while ECHO.value():
        pass
    time2 = time.ticks_us()
    duration = time.ticks_diff(time2, time1)
    return duration * 340 / 2 / 10000  # Return distance in cm

# Function to play a tone on the buzzer at a specified frequency
def tone(frequency):
    buzzer.freq(frequency)  # Set buzzer frequency
    buzzer.duty_u16(30000)  # Set duty cycle to 50% (approx)

# Function to stop playing the tone (mute the buzzer)
def noTone():
    buzzer.duty_u16(0)  # Set duty cycle to 0% (mute)

# Function to randomly light up the RGB LED with random color values
def lightup():
    red.duty_u16(int(urandom.uniform(0, 65535)))  # Set random intensity for red
    green.duty_u16(int(urandom.uniform(0, 65535)))  # Set random intensity for green
    blue.duty_u16(int(urandom.uniform(0, 65535)))  # Set random intensity for blue

# Function to turn off all RGB LED colors (set all to 0)
def dark():
    red.duty_u16(0)  # Turn off red LED
    green.duty_u16(0)  # Turn off green LED
    blue.duty_u16(0)  # Turn off blue LED

# Main loop to handle distance measurement and tone generation
while True:
    dis = distance()  # Measure distance
    print('Distance: %.2f cm' % dis)
    
    # Play different tones and light up the LED based on distance
    if dis < 10:  # Very close range
        tone(523)  # Play C5
        lightup()  # Light up the RGB LED with random colors
        display_wave(523)
    elif dis < 20:  # Close range
        tone(494)  # Play B4
        lightup()
        display_wave(494)
    elif dis < 30:  # Medium range
        tone(440)  # Play A4
        lightup()
        display_wave(440)
    elif dis < 40:  # Far range
        tone(392)  # Play G4
        lightup()
        display_wave(392)
    elif dis < 50:  # Farther range
        tone(349)  # Play F4
        lightup()
        display_wave(349)
    elif dis < 60:  # Maximum range for this setup
        tone(330)  # Play E4
        lightup()
        display_wave(330)
    else:  # Out of range
        noTone()  # Mute buzzer
        dark()  # Turn off the RGB LED

    time.sleep_ms(300)  # Delay between distance measurements
