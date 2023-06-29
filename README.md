# IoTSecurity
This is the project I am currently working on (2023). It is about building an indoor security system using ESP32 and a few programming languages. 

# Goals
This system aims to identify intruders within restricted hours and take picutres automatically. I use infrared sensor to see if anyone enters the  
restriced area, and use suzuki contour algorithm to see if there is any moving object.

# Tools
The list below shows all the tools I have used.
+ C++ (for the code on ESP32)
+ JavaScript (for sending request to the server by ajax and for display the result on my webpage)
+ Python (for using background subtraction to capture images and store on store)
+ HTML
+ CSS

# Demo


This video shows the real-time motion detection. The frame with red rectangle is captured and stored into the database 
for future investigation.


https://github.com/Rob12312368/IoTSecurity/assets/56261402/d6589ec6-6cef-4e54-8c0b-bd57a36c9ad2



The second video contains all the other function of this program, including setting the restricted time for detection, searching
and deleting pictures within specific time range, and showing different messages when detection is triggered within or not within restricted hours.




https://github.com/Rob12312368/IoTSecurity/assets/56261402/a90e2c72-1a9a-4544-b380-e57505ef1c9e



