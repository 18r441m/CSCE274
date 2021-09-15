# ROS Lecture : Rock Paper Scissors

### To build the images:
	
		cd CSCE274/Lectures/ROS/

		docker build . -t lecture:ros

### To start a container 

		docker run -itd -v $(pwd)/packages:/catkin_ws/src --name rps lecture:ros

### To access in terminal

		docker exec -it rps bash

