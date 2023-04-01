# IoTProject
This is the project I am currently working on (2023). It is about building an indoor security system using ESP32 and a few programming languages. 

# Goals
This system aims to identify intruders within restricted hours and take picutres automatically. I use infrared sensor to see if anyone enters the  
restriced area, and use background subtraction to see if there is any moving object.

# Tools
The list below shows all the tools I have used.
+ C++ (for the code on ESP32)
+ JavaScript (for sending request to the server by ajax and for display the result on my webpage)
+ Python (for using background subtraction to capture images and store on store)

# Demo
This image shows the webpage for setting restricted hours. 
![The page for setting restricted time span](/images/settime.PNG)

This image shows the real time monitor process. The down left live stream under "SAFE" is me sitting in front of the ESP32 camera. At first, it shows "SAFE" because nobody passes by (I was not moving).
![nobody passes by](result_safe/images/.PNG)

Then, the word transformed from "SAFE" to "Someone has ...", as someone passes by during restricted hours (I started to move).
![somebody passes by](result_warn/images/.PNG)

