# JOURNAL.md  
**Project:** Mudskipper-Inspired Soft Robot for Agriculture  
**Total Time Spent:** ~32 hours  

---

## Day 1 – Project Ideation & Research  
**Date:** Day 1  
**Time Spent:** 3 hours  

Today, I concentrated on finding out more information on how mudskipper fish move and how they can be used as models for an agricultural robot. I looked at some videos and articles that highlighted how they use their pectoral fins and tails. 
At this point, I began considering how this technique can be used in aiding soil that is either muddy and wet or full of salinity.
I knew early on that the robot would have the ability to interface directly with the soil, as opposed to just walking on top of it.

---

## Day 2 – System Planning & Component Selection  
**Date:** Day 2  
**Time Spent:** 4 hours  

The system architecture was also planned for today. I settled for the Raspberry Pi Pico W for my primary controller, considering that I can connect it wirelessly in the future for data transmission. The final servos to be used are 5:
- 2 for pectoral fins
- 1 for the tail
- 2 for sensor placement
I also confirmed that pH and TDS sensors are used in analyzing soils. Iuating how these sensors will be required to move from top to bottom in order to measure at different intervals.

---

## Day 3 – 3D Design: Main Body  
**Date:** Day 3  
**Time Spent:** 3 hours  

I began the process of my 3D modeling today. I started off with the body, trying to make sure that it was compact and hollow enough to accommodate the electronics. The first design was a bit too slim and wouldn't really hold the servos, so I added thicker walls to the design.
Later in the session, the body was changed to accommodate two servos placed on either side of the pectoral fins. This took longer than anticipated due to alignment constraints.
![Alt text](/Images/7.png)


---

## Day 4 – Servo Holders & Structural Adjustments  
**Date:** Day 4  
**Time Spent:** 2 hours  

I created customized holders for servos that could be incorporated right into the body. In my first attempt, I did not provide enough room for the servos to move, and I had to remake it.
At the end of the day, the servos were in their proper positions, and it felt like having a “robot” as opposed to just having a “shell.” This has been a frustrating day, but it has helped me in understanding the limitations of mechanisms.
![Alt text](/Images/8.png)

---

## Day 5 – Pectoral Fins (Hands of the Robot)  
**Date:** Day 5  
**Time Spent:** 3 hours  

Today, I modeled the pectoral fins, which serve as "hands" for the robot. I attempted to replicate the broad, flat nature of a mudskipper's fins.
I had to try different shapes to be satisfied with the final choice, which had to be flexible and stable. I had to make sure that it would be possible to easily connect the fins to the servo horns.

![Alt text](/Images/9.png)

---

## Day 6 – Tail Design & Locomotion Concept  
**Date:** Day 6  
**Time Spent:** 3 hours  

Tail design, which helps with movement and balance, was my design. Initially, I wanted to create a complex tail, but this seems rather unnecessary and difficult to manage.
I was able to simplify this to a single flexible system that is controlled by a single servo motor. This move saves time when programming this function later on.

![Alt text](/Images/10.png)

---

## Day 7 – Seed Planting Mechanism  
**Date:** Day 7  
**Time Spent:** 3 hours  

This was one of the most tricky parts. I knew that I had to design the seed planting system to deliver seeds only when the soil is appropriate.
The first one jammed in the simulation, so I rebuilt it with smoother channels. I am also designing a gate system driven by a servo motor.
This is directly related to the readings from the sensors, which makes it the “brain-meets-action” component of a robot.

![Alt text](/Images/11.png)

---

## Day 8 – Sensor Placement & Vertical Movement  
**Date:** Day 8  
**Time Spent:** 1 hours  

The main body is altered again to consider the slot for sensor placement. A vertical sliding system is created to enable the pH and TDS sensors to move up and down via the use of a servo.
This component took a lot of attention so as not to crash other elements. After a few unsuccessful designs, I was able to create a functional one.


![Alt text](/Images/6.png)

---

## Day 9 – Circuit Design (EasyEDA)  
**Date:** Day 9  
**Time Spent:** 5 hours  

Today I designed the full circuit using EasyEDA. The circuit includes:  
- Raspberry Pi Pico W  
- Connections for 5 servos  
- pH sensor interface  
- TDS sensor interface  
- Power distribution  

I had to the inital code prepered.

![Alt text](/Images/14.png)

---

## Day 10 – Review, Reflection & Documentation  
**Date:** Day 10  
**Time Spent:** 5 hours  

I reviewed the entire project today, checking the 3D design, circuit, and system logic. 

![Alt text](/Images/4.png)

---

## Final Reflection  
This project taught me a lot about mechanical design, electronics integration, and iterative problem-solving. Many early ideas didn’t make it into the final design, but they were essential for learning. The journal reflects not just what worked, but also what didn’t—and that’s what made the project meaningful.

**Total Logged Time:** ~32 hours  

