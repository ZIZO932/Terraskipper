# JOURNAL.md  
**Project:** Mudskipper-Inspired Soft Robot for Agriculture  
**Total Time Spent:** ~32 hours  

---

## Day 1 – Project Ideation & Research  
**Date:** Day 1  
**Time Spent:** 3 hours  

i spent about three hours just looking at videos of mudskippers because their movement is honestly kind of weird but also perfect for what i want to do. i spent a lot of time trying to figure out how they use their pectoral fins to crutch along the mud and i was wondering if i could actually replicate that with servos. the biggest struggle was honestly just trying to find actual research papers that werent too scientific but still gave me enough info on their bone structure. i started thinking about how this could actually work in a field with really salty or wet soil where a normal robot with wheels would just get stuck and die immediately. it was a bit overwhelming at first because i kept thinking if i should just make a normal walking robot but i really want to stick to the mudskipper idea.

---

## Day 2 – System Planning & Component Selection  
**Date:** Day 2  
**Time Spent:** 4 hours  

spent four hours today just trying to map out how everything is going to connect to the raspberry pi pico w. i chose that one because it has wifi and is pretty small but i started getting worried about the power draw from five different servos. i have two for the fins one for the tail and then two more just to move the sensors around which is a lot for a small board. the most annoying part was definitely the sensors because i realized that the ph and tds sensors i was looking at were actually meant for water like for a fish tank or something and that just wont work if i want to jab them into the ground. i had to spend some time looking for actual soil probes that can handle the grit and the pressure of being pushed into dirt without breaking the first time i use them.

![Alt text](/Images/sen.png)
---

## Day 3 – 3D Design: Main Body  
**Date:** Day 3  
**Time Spent:** 3 hours  

i started modeling the main body but the first version i made was way too thin and there was no way i was going to fit the pico and all the messy wiring inside of it. i had to go back and make the walls thicker so it wouldnt just snap but then that made the whole thing heavier which is another problem for the servos. i also struggled a lot with the alignment for the pectoral fin servos because if they are even a little bit off the robot is just going to walk in circles or flip over. i had to keep restarting the sketch because the holes for the mounting screws werent lining up with the servo brackets i found online.

![Alt text](/Images/7.png)


---

## Day 4 – Servo Holders & Structural Adjustments  
**Date:** Day 4  
**Time Spent:** 2 hours  

i spent two hours today just working on the holders that actually keep the servos in place inside the body. my first attempt was a total disaster because i didnt leave any room for the wires to come out of the side of the servo so i had to go back and chop out part of the design. it felt like i was finally getting somewhere when i got them to sit flush but then i realized i didnt leave enough clearance for the servo arm to rotate fully. i had to stay at the computer and basically carve out sections of the 3d model so the "arms" wouldnt hit the chassis. it was one of those days where you feel like you did a lot of work but you dont have much to show for it except a slightly different looking box.

![Alt text](/Images/8.png)

---

## Day 5 – Pectoral Fins (Hands of the Robot)  
**Date:** Day 5  
**Time Spent:** 3 hours  

pectoral fins hands of the robot today was all about the fins and it took me three hours to get a shape i actually liked. i wanted them to look like the broad flat fins of a real mudskipper so they have enough surface area to push off the mud. the struggle here was trying to figure out how to attach them to the plastic servo horns because if i just glue them they will definitely fall off after five minutes of walking. i had to design a little socket that the horn fits into tightly and then screw it in. i went through like three different shapes because some were too long and were bending too much and others were too short to actually lift the body up.

![Alt text](/Images/9.png)

---

## Day 6 – Tail Design & Locomotion Concept  
**Date:** Day 6  
**Time Spent:** 3 hours  

i spent three hours on the tail today and i almost made it way too complicated. i was going to make this multi jointed tail that wagged back and forth like a real fish but when i started looking at the code i realized it was going to be a nightmare to program. i decided to simplify it down to one single servo with a flexible piece of plastic at the end. it was kind of a relief to make that decision because it saves me so much time and it also makes the robot lighter. i still struggled with the balance though because the tail is supposed to help it stay steady but if i make it too heavy it just drags behind and slows everything down.

![Alt text](/Images/10.png)

---

## Day 7 – Seed Planting Mechanism  
**Date:** Day 7  
**Time Spent:** 3 hours  

seed planting mechanism this was definitely the trickiest part of the whole week and i spent three hours on it. i need the robot to be able to drop seeds but only when the sensors tell it the soil is good. i made a little hopper and a channel for the seeds to slide down but they kept getting jammed in the opening because they are slightly irregular shapes. i had to rebuild the whole channel to be smoother and i added a little gate that is controlled by another servo. i spent so much time just dropping seeds through a plastic tube to see if they would get stuck. it was really tedious and honestly kind of annoying but i think i got it working now.

![Alt text](/Images/11.png)

---

## Day 8 – Sensor Placement & Vertical Movement  
**Date:** Day 8  
**Time Spent:** 1 hours  

i spent an hour today just hacking apart the main body design again because i forgot to leave a good spot for the soil sensors. i had to make a vertical sliding system so the robot can actually push the probes into the ground to get a reading and then pull them back up so it can move. this was hard because soil is a lot tougher to poke than water so the servo has to be really strong. i had a few designs that just looked too flimsy and i knew they would snap the first time they hit a rock in the dirt. i finally came up with a rack and pinion style setup that feels a bit more solid.


![Alt text](/Images/6.png)

---

## Day 9 – Circuit Design and PCB (Kicad)  
**Date:** Day 9  
**Time Spent:** 5 hours  

today was a massive five hour grind on the electrical side and i switched over to using kicad to get everything done. mapping out the connections for five servos plus the sensors and the pico was a huge headache because the schematic kept getting so messy with lines crossing everywhere and i had to keep deleting things and starting over to make it readable. once i finally got the schematic done i moved on to the pcb layout which was even harder because i had to fit all the traces in a really tight space without causing any short circuits. i spent forever trying to figure out where to put the power traces because i really dont want the servos to pull so much current that they reset the controller or cause a brownout in the middle of a test. i also had to write some basic code just to make sure the logic pins i picked actually made sense for the pcb layout. im still a bit worried about the actual soldering part and how many wires are going to be crammed into that tiny body but at least the board design is finished and the pcb looks solid.

![Alt text](/Images/s1.png)
![Alt text](/Images/pp1.png)
---

## Day 10 – Review, Reflection & Documentation  
**Date:** Day 10  
**Time Spent:** 5 hours  

today was the final stretch and i spent five hours going over everything i did for the last nine days. i looked back at the 3d models and realized just how much they changed from that first skinny version i made on day three. i spent a lot of time thinking about the sensor change too because switching from water sensors to soil probes was a huge pivot that changed the whole mechanical design of the sensor mount. 

![Alt text](/Images/4.png)

---

## Final Reflection  
This project taught me a lot about mechanical design, electronics integration, and iterative problem-solving. Many early ideas didn’t make it into the final design, but they were essential for learning. The journal reflects not just what worked, but also what didn’t—and that’s what made the project meaningful.

**Total Logged Time:** ~32 hours  

