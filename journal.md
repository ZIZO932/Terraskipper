# JOURNAL.md  
**Project:** Mudskipper-Inspired Soft Robot for Agriculture  
**Total Time Spent:** ~32 hours  

---

## Day 1 – Project Ideation & Research  
**Date:** Day 1  
**Time Spent:** 3 hours  

Today I focused on understanding how mudskippers move and why they are suitable as inspiration for an agricultural robot. I watched several videos and read articles about their pectoral fins and tail-based locomotion. I also started thinking about how this motion could help in muddy or high-salinity soil environments.  
I decided early on that the robot should be able to interact with the soil directly, not just move on top of it.

---

## Day 2 – System Planning & Component Selection  
**Date:** Day 2  
**Time Spent:** 4 hours  

I planned the overall system architecture today. I chose the Raspberry Pi Pico W as the main controller because it’s compact, powerful enough, and allows future wireless data transmission. I finalized the use of 5 servos:  
- 2 for pectoral fins  
- 1 for the tail  
- 2 for the sensor placment  

I also confirmed the use of pH and TDS sensors for soil analysis. I sketched how the sensors would need to move up and down to take measurements at different depths.  

---

## Day 3 – 3D Design: Main Body  
**Date:** Day 3  
**Time Spent:** 3 hours  

I started the 3D modeling process today. I began with the main body, focusing on keeping it compact but hollow so it could fit the electronics. The first version was too thin and wouldn’t realistically hold the servos, so I redesigned it with thicker walls.  
Later in the session, I modified the body to allow two servos to be placed on opposite sides for the pectoral fins. This took longer than expected because of alignment issues.  
![Alt text](/Images/7.png)


---

## Day 4 – Servo Holders & Structural Adjustments  
**Date:** Day 4  
**Time Spent:** 2 hours  

I designed custom servo holders that could be integrated directly into the body. My first attempt didn’t give enough clearance for servo movement, so I had to redo it.  
By the end of the day, the servos fit correctly, and the body felt more “robot-like” rather than just a shell. This was a frustrating day, but it helped me understand mechanical constraints better.  
![Alt text](/Images/8.png)

---

## Day 5 – Pectoral Fins (Hands of the Robot)  
**Date:** Day 5  
**Time Spent:** 3 hours  

Today I modeled the pectoral fins, which act like the robot’s hands. I tried to mimic the wide, flat shape of real mudskipper fins.  
I tested multiple shapes before settling on one that looked flexible and stable. I also ensured the fins could attach cleanly to the servo horns.  

![Alt text](/Images/9.png)

---

## Day 6 – Tail Design & Locomotion Concept  
**Date:** Day 6  
**Time Spent:** 3 hours  

I designed the tail, which is responsible for assisting movement and balance. At first, I wanted a complex segmented tail, but that felt unnecessary and hard to control.  
I simplified it to a single flexible structure controlled by one servo. This decision saved time and made the motion easier to program later.  

![Alt text](/Images/10.png)

---

## Day 7 – Seed Planting Mechanism  
**Date:** Day 7  
**Time Spent:** 3 hours  

This was one of the most challenging parts. I designed the seed planting mechanism to release seeds only when soil conditions are suitable.  
The first mechanism jammed in the simulation, so I redesigned it with smoother channels. I also planned for a servo-driven gate system.  
This mechanism is directly linked to the sensor readings, which makes it the “brain-meets-action” part of the robot.  

![Alt text](/Images/11.png)

---

## Day 8 – Sensor Placement & Vertical Movement  
**Date:** Day 8  
**Time Spent:** 1 hours  

I modified the main body again to include a dedicated sensor placement slot. I designed a vertical sliding system so the pH and TDS sensors could move up and down using a servo.  
This part required careful spacing to avoid collisions with other components. After a few failed designs, I finally got a version that worked smoothly.  

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
