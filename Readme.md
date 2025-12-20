# Mudskipper-Inspired Soft Robot for Agriculture

## Project Description
This project is a mudskipper-inspired soft robot designed to work in muddy and high-salinity agricultural environments. Instead of using wheels, the robot moves using pectoral fins and a tail, similar to a real mudskipper.  
The robot is also able to interact directly with the soil using pH and TDS sensors. Based on the sensor readings, it can decide when to activate a small seed-planting mechanism, making the system responsive rather than purely mechanical.

---

## Why I Made This Project
I made this project because I was interested in how nature solves problems that engineering struggles with. Mudskippers can move and survive in wet, unstable soil where normal robots would get stuck.  
I wanted to explore whether copying this kind of movement could be useful in agriculture, especially in areas with muddy or salty soil. This project also helped me learn more about 3D design, electronics, and how small design mistakes can affect the whole system.

---

## 3D Model
The 3D model went through several iterations before reaching its current form. It includes:
- A hollow main body to hold electronics  
- Built-in servo holders  
- Two pectoral fins used as the robot’s “hands”  
- A tail for balance and movement  
- A seed planting mechanism  
- A vertical system that moves the pH and TDS sensors up and down  

Below are multiple views of the full 3D model from different angles to show how the parts fit together.
![Alt text](/Images/1.png) ![Alt text](/Images/2.png) ![Alt text](/Images/3.png) ![Alt text](/Images/4.png)



---

## Wiring Diagram
The wiring diagram shows how all components are connected:
- The Pico W controls the five servos  
- The pH and TDS sensors send data to the controller  
- Power is shared safely between logic and motors  

This step helped me catch several connection mistakes before moving to physical assembly.
![Alt text](/Images/13.png)

---

## Bill of Materials (BOM)

| Component | Quantity | Notes |
|-----------|----------|-------|
| Raspberry Pi Pico W | 1 | Main controller (WiFi capable) |
| MG996R Servo Motors | 5 | Fins, tail, sensor movement (High Torque) |
| pH Sensor | 1 | Soil/Water acidity measurement |
| TDS Sensor | 1 | Soil salinity measurement |
| XL4015 Converter | 1 | 5A Step-down regulator (Essential for Servos) |
| 18650 Li-Ion Battery | 2 | Main power source (7.4V Series) |
| MPU-6050 | 1 | IMU (Gyroscope & Accelerometer) |
| NEO-6M GPS | 1 | Location and navigation module |
| Breadboard & Wires | 1 | Prototyping connections |

---

## Final Notes
This project is still a work in progress, but it represents a full design cycle from idea to system-level integration. Many designs failed or were changed along the way, and those mistakes were just as important as the final result.  


