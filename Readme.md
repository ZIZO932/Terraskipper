# Mudskipper-Inspired Soft Robot for Agriculture

## Project Description
i made this robot because i was really interested in how mudskipper fish move around in places where regular animals or even robots would just get stuck in the mud. instead of using wheels which would just spin and sink i designed this to use pectoral fins and a tail to crutch along the ground. it also has these sensors that can check the ph and tds of the soil to see if its actually a good spot to plant anything. if the soil looks okay it has this little seed planting mechanism that drops a seed which makes it a lot more useful than just a robot that walks around for no reason. it was a huge challenge to get the movement right because copying nature is way harder than it looks.

---

## Why I Made This Project
the main reason i started this was to see if i could actually take a weird movement from nature and use it for something practical like farming in muddy or salty areas. i also really wanted to get better at 3d design and electronics because i knew i would make a lot of mistakes and i wanted to see if i could fix them. this project taught me that even a tiny mistake in the 3d model like making a wall too thin can ruin the whole thing later on. it was also a big wake up call when i realized my initial sensors were for water and i had to scramble to find soil probes that wouldn't just break the second they touched the dirt.
---

## 3D Model
the 3d model was a total headache and it took so many versions to get it right. i had to make the main body hollow so it could hold all the messy wires and the pico w but it also had to be strong enough to hold the five servos. the design has these custom holders for the servos that move the fins and the tail and i also had to build a specific vertical slider for the sensors. that slider was tough because it has to push the ph and tds probes into the soil which takes a lot more force than just dipping them in water. i also had to make sure the seed planting part wouldnt jam up every time it tried to drop something.
![Alt text](/Images/1.png) ![Alt text](/Images/2.png) ![Alt text](/Images/3.png)



---

## Wiring Diagram
the wiring diagram was where i had to figure out how to connect everything without blowing up the pico w. it shows how the controller handles all five servos and where the data from the ph and tds sensors goes. i had to be really careful about the power because five servos pulling current at the same time can easily crash the system. i ended up using kicad to make a proper schematic and pcb because a breadboard was just becoming a nightmare of tangled wires. doing this helped me find a bunch of mistakes where i had wires crossing that would have definitely shorted out the whole thing if i hadn't caught them.
![Alt text](/Images/s1.png) ![Alt text](/Images/pp1.png)

---

## Bill of Materials (BOM)

| Item | Description | Qty | Unit Price (EGP) | Unit Price (USD) | Total Price (USD) | URL | Running Total (USD) |
|------|-------------|-----|------------------|------------------|-------------------|-----|---------------------|
| Raspberry Pi Pico W | MCU (Main Controller) | 1 | 650 | 13.85 | 13.85 | https://electra.store/product/raspberry-pi-pico-w/ | 13.85 |
| MG996R Servo | High Torque Servo Motor | 5 | 200 | 4.26 | 21.30 | https://www.ram-e-shop.com/ar/shop/servo-mg996-180-mg996r-servo-motor-180deg-11-kg-cm-metal-gears-7397?srsltid=AfmBOoq1zvLpgjLLOmXDFrNQpmj2SQrDjgcnsE8VNdSKkgjMb-rjCr2f | 35.15 |
| 7 in 1 soil sensor | pH and TDS Measurement Sensor | 1 | 4500 | 95.87 | 95.87 | https://makerselectronics.com/product/industrial-soil-moisture-temperature-sensor-modbus-rtu-rs485/?campaignid=20503411856&adgroid=up&network=x&device=c&campaignname=sales_pmax&gad_source=1&gad_campaignid=20503433012&gbraid=0AAAAApRJSNFn77HI4O79RMkhUNGKsHWNO&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xqx909JpmEgYe0-mFSB0og0OA0A5Ajb2pms3LxBvvR7rJVYkLQwEe4aAsfdEALw_wcB | 131.02 |
| Breadboard & Wires | Prototyping Accessories | 1 | 300 | 6.39 | 6.39 | https://www.ram-e-shop.com/shop/bb2t4d-j140-bb-bb-2t4d-j140-breadboard-1660-tie-point-140-jumper-wire-metal-base-6755 | 137.41 |
| XL4015 Converter | Regulation Module | 1 | 95 | 2.02 | 2.02 | https://www.ram-e-shop.com/shop/dc-dc-101-dc-dc-step-down-voltage-converter-adjustable-5a-xl4015-5v-32vdc-to-0-8v-30vdc-sku-dc101-7258 | 139.43 |
| 18650 Battery | Power Source | 2 | 245 | 5.22 | 10.44 | https://www.ram-e-shop.com/shop/battery-18650-lgcm-battery-lithium-li-ion-inr18650mh1-mh1-3200mah-10a-4-2-3-7-2-5v-rechargeable-9064 | 149.87 |
| MPU-6050 | IMU | 1 | 175 | 3.73 | 3.73 | https://www.ram-e-shop.com/shop/kit-imu-mpu6050-gy521-imu-6-dof-mpu-6050-gyroscope-accelerometer-sensor-module-7076 | 153.60 |
| NEO-6M GPS | GPS Module | 1 | 563 | 12.00 | 12.00 | https://makerselectronics.com/product/ublox-hw-539-neo-6m-gps-module/?srsltid=AfmBOorZ5a90If9bXw3bXueIRVRr6BAAfuh6hryrSHD4mv6YlEpa6hi- | 165.60 |


---

## Final Notes
this project is definitely still something i am working on and it's far from perfect. looking back i can see how much i had to change like the whole sensor mounting system and the way the fins were shaped. the mistakes i made with the 3d prints and the circuit design were actually the most useful parts of the whole experience because they forced me to learn how to troubleshoot. it might not look like a professional robot yet but it represents a lot of hours of me just trying to get a plastic fish to plant seeds in the mud.



