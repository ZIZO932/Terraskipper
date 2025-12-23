# Mudskipper-Inspired Soft Robot for Agriculture

## Project Description
This is a soft robot inspired by the mudskipper, created to operate in muddy and high-salt fields. The system does not employ wheels for propulsion but relies on the pectoral fins and the tail, the same as in the mudskipper.
The robot can also interact with soil using pH and TDS sensors. The sensor helps it determine whether to engage in activities that will make it plant seeds using a small seed-planting mechanism. This makes it possible for the robot to be able to interact with soil.

---

## Why I Made This Project
The reason I was interested in this project was because I was curious whether it was possible to adapt a movement like this by simply copying it and see how it could be used in agriculture, particularly in regions where the ground is muddy or salty. This project was also a way for me to learn more about 3D designing and the electronics, as well as how a small mistake in the design can impact the overall system.
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



