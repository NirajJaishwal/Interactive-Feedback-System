# Interactive Feedback System  
### Sensory Feedback System with Raspberry Pi Pico W  

**Course Name:** Human Computer Interaction  
**Professor:** Dr. Yingcai Xiao  
**Project Type:** Final Project  

---

## Introduction  

Human-Computer Interaction (HCI) focuses on designing systems that create intuitive and effective interactions between users and technology. Sensory feedback—such as audio, visual, or touch responses—plays a vital role in enhancing user experience, providing immediate, context-specific information, and making technology more accessible.  

This project demonstrates an **Interactive Sensory Feedback System** built with a **Raspberry Pi Pico W**, combining an **ultrasonic sensor**, **passive buzzer**, **RGB LED**, and **MPR121 touch sensor module**.  

- The **ultrasonic sensor** detects hand distance.  
- A **buzzer** produces variable frequencies to indicate distance.  
- An **RGB LED** lights up in random colors, providing visual cues.  
- The **MPR121 touch sensor** adds an additional **touch-based sensory feedback** mechanism.  

This multisensory system offers **auditory, visual, and tactile feedback**, creating an engaging and interactive HCI experience.  

---

## Components  

- **Raspberry Pi Pico W** – Microcontroller for processing inputs and controlling outputs  
- **Ultrasonic Sensor (HC-SR04)** – Measures distance between the sensor and objects  
- **Passive Buzzer** – Provides auditory feedback with frequency variations  
- **RGB LED** – Provides visual feedback with dynamic color changes  
- **MPR121 Touch Sensor Module** – Adds touch-based sensory feedback  
- **Transistor & Resistors** – Regulate and control electrical flow  

---

## System Design  

1. **Ultrasonic Sensor (HC-SR04)**  
   - Trigger Pin: GPIO 17  
   - Echo Pin: GPIO 16  
   - Power: 3.3V + GND  

2. **Passive Buzzer**  
   - PWM Pin: GPIO 15  
   - Power: GPIO 15 + GND  

3. **RGB LED**  
   - Red: GPIO 13  
   - Green: GPIO 12  
   - Blue: GPIO 11  
   - Powered via resistors to ground  

4. **MPR121 Touch Sensor Module**  
   - Communication: I2C (SDA, SCL)  
   - Power: 3.3V + GND  

---

## Implementation  

- **Distance Measurement:**  
  Uses ultrasonic sensor to calculate object distance (cm) by measuring time of sound reflection.  

- **Buzzer Feedback:**  
  Maps measured distances to different frequency tones. Closer objects = higher frequency.  

- **LED Feedback:**  
  Random color generation on the RGB LED when a hand is detected in range.  

- **Touch Feedback:**  
  MPR121 module detects touch inputs to provide additional interactivity.  

---

## Lessons Learned  

- Improved understanding of **programming microcontrollers** and **sensor integration**.  
- Learned to generate specific tones and map sensor readings into real-time feedback.  
- Faced challenges with **RGB LED resistor calibration** and **combining multiple modules** in code.  
- Developed skills in debugging and system integration.  

---

## Future Work  

- Add a **small display** for real-time distance readouts.  
- Implement **more refined tone and color mappings** for better proximity interpretation.  
- Utilize **Wi-Fi features of Pico W** for remote monitoring and IoT applications.  
- Extend into real-world use cases like **interactive installations** or **assistive technologies**.  

---

## Getting Started  

### Prerequisites  
- [Raspberry Pi Pico SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html) or [MicroPython](https://micropython.org/download/rp2-pico-w/) firmware  
- Thonny IDE or any MicroPython IDE  
- Circuit connections as listed above  

### Running the Project  
1. Flash MicroPython to Pico W  
2. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/interactive-feedback-system.git
