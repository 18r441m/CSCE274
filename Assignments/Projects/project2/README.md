## Project 2

### Assigned: September 20, 2022
### Due: October 03, 2022

--------

### The goal of project 2 is to calibrate the camera and wheels of the duckiebot and test the calibration.

## Part 1 
### Let's make the duckiebot move
- Follow the [instructions](https://docs.duckietown.org/daffy/opmanual_duckiebot/out/rc_control.html) to make your robot move.

## Part 2
### Camera Calibration

Calibrate your camera so that your duckiebot can see the world around it. Ensure it is in focus first by twisting the lens while looking at the initial calibration window in the [instructions](https://docs.duckietown.org/daffy/opmanual_duckiebot/out/camera_calib.html) until the image is sharp. 

### [Calibration Pattern](./calibration_pattern.pdf)

## Part 3
### Wheel Calibration

Calibrate your wheels so your duckiebot can drive straight. [Instructions](https://docs.duckietown.org/daffy/opmanual_duckiebot/out/wheel_calibration.html)

## Part 4
### Lane Follow Demo

let’s put it all together and start the lane following demo. We’re going to do this by manually starting a docker container on the robot and running each step by hand. 

- The Lab (1D49) has assembled Duckietowns you can use for the step. If you choose to assemble your own duckietown, follow the [instructions](https://docs.duckietown.org/daffy/opmanual_duckietown/out/dt_ops_appearance_specifications.html).

- To start, place your robot in a lane.
- Let’s see what is running on your robot first. In a terminal, run:

        dts start_gui_tools <duckiebot_name>

    When that starts, you will connect to the ROS instance on the Duckiebot and can use debug tools. Run:
        
        rqt_graph
    And you should see a graph of all nodes and topics. Screenshot the most legible image of this graph as you can to turn it in.

- Start keyboard control as in part 4.

        dts duckiebot keyboard_control <duckiebot_name>

- Open a terminal and start the dt-core docker container on the duckiebot:

        docker -H <duckiebot_name>.local run --rm --name test_lane_follow -v /data:/data --network=host -it duckietown/dt-core:daffy-arm32v7 bash
    NOTE: this command is all one line.

    This should start in the directory 
    
        /code/catkin_ws/src/dt-core

- Change directory:

        cd /code/catkin_ws

- Source your environment
    
        source devel/setup.bash
- Run 
    
        catkin build 

- Source your environment again
        
        source devel/setup.bash

- Run
        
        roslaunch duckietown_demos lane_following.launch 
        
    Wait for the messages to stop (You should see health status change to “STARTED” at the end)

- In a start_gui_tools terminal (from earlier) run “rqt_graph” again. What has changed since the last time you ran it? Turn in a screenshot of this graph as well.

- In keyboard control, while selecting the window, press ‘a’. The robot should now move around the track. Press ‘s’ to stop. 

    Note that the robot does not handle intersections in this mode. Ensure that it follows lanes or recalibrate until it does.

    Note that you can also start the demo through dts tools but you will not receive as much feedback [instruction](https://docs.duckietown.org/daffy/opmanual_duckiebot/out/demos.html).

- Demonstrate lane following to your instructor/TA by taking a video and uploading it to youtube. Make sure to follow the instructions below to include a link to the video in your submission.

## Part 5

### Dropbox submission

NOTE: Your submission should consist of only one pdf file

- Submit a PDF to CSE Dropbox with:

    * The name of your duckiebot
    * A youtube link to the video of your best lane following demo run
    * The screenshots:
        - FROM PART 4 (rqt_graph before)
        - FROM PART 4 (rqt_graph after)

    * Write a few sentences about what happens on the robot when you run lane following. Which nodes start, and how are they connected to what was running on the robot before? What do you think each of these new nodes does?

    * pdf format instructions
        * Header with the class code, the semester and year, the homework number, and your UofSC username.
          e.g., CSCE 274 Section 1 Fall 2022 – Project 2 – ijsalman
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
            csce274_fall2022_<project#>_<UofSC username>.pdf
            e.g., csce274_fall2022_project2_ijsalman.pdf
