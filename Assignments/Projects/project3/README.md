## Project 3 (10% over the final grade) 

### Assigned: October 23, 2021
### Due: November 07, 2021

--------

#### The goal of this project is for you to produce a node that keeps your Duckiebot in its lane. Note that this node already exists in the Duckietown code repo. Feel free to look at it for inspiration but make sure that the actual node you turn in is your own. You do NOT need to perform any of the state checking done in the actual node, you only need to accept the lane position message and publish the command message as described below.

--------

## Part 1

- Run the lane controller demo on your Duckiebot. Look at the inputs and outputs of the lane_controller_node. 
    - You should be somewhat familiar with the output but may not be familiar with the exact topic. Note that this time, it goes to the switch node, not straight to kinematics. This is because lane following waits for a signal from keyboard control before it starts. You will want to do the same.
    - Pay attention to the input topic lane_pose. This contains the output from the sensing pipeline and tells you where you are in the lane. Pay special attention to the d and phi parameters in that message. Experiment a bit with your robot on a lane. The d parameter tells you where you are in the lane and the phi parameter tells you your orientation. Ideally, they should both be 0.

- Think about what variables you need to control here. Does the speed affect the robot’s position in the lane? How about the angular velocity?

- Create a lane controller that uses a PID controller (not all terms are necessarily needed) to keep your robot in the lane. Note that two PID controllers (one for each parameter described in 1b) added together tends to work best.

- Tune your controller(s) until they work well on your Duckietown mats.

- Some notes on writing your code:
    - Use whichever method of syncing and revising code worked for you in Project 2
    - Do NOT include your Duckiebot’s name in the topics (or anywhere else) in your code. Instead, use a namespace in the launch file as required in Project2. This allows your code to be run on any Duckiebot.
    - You will need to include several other Duckietown nodes in your launch file. Take a look at how the Duckietown lane following demo launch file works or look at the example launch file at the end of these instructions.
    - This is a real robot with real hardware, so there will be errors in sensing. You may want to threshold (limit) the maximum/minimum errors given to your controller and/or the maximum control signal you will send. Be patient and work out what your robot is telling you versus what it should be doing.

- To prove it is your code running, and not the lane following demo, please do the following:
    - Have your code output a unique message to loginfo or similar (logwarn/logerr will show up in amber/red on the screen and may be better for visibility) every time your main callback is run. Something like “your name LANE FOLLOWING CODE” is preferred to show that it is your code.
    - Record the screen on your computer (preferably using a screen capture program) while your code is running with the following programs open:
        - A terminal showing that no lane controller nodes are running at the beginning (run “rosnode list” and show the output) and then showing roslaunch as it starts your controller.
        - rqt_image_view showing the Duckiebot’s camera view
        - rqt_console (if your custom message is not shown in the terminal)
        - NOTE: to run both rqt_console and rqt_image_view at the same time, use & at the end of the command to run in the background, like:

                rqt_image_view &
                rqt_console &
            You may need to press enter again to get back to the command prompt
    - Also record a top-down video of your Duckiebot performing lane following for at least three laps of your mats. Make sure this recording overlaps with the recording from the last step. You do NOT need to sync the videos or any other serious video editing, just make sure it is from the same run.


## Part 2

### Dropbox submission

NOTE: Your submission should consist of one PDF and one ZIP file.

- Submit a PDF to CSE Dropbox with:

    * A youtube link to the video you recorded

    * Answers to the following questions:
        - A short description of what you choose to control (input and output signals) and why. 
        - What final PID gain values did you use?
        - A description of any problems you had completing this project


    * pdf format instructions
        * Header with the class code, the semester and year, the homework number, and your group.
          e.g., CSCE 274 Section 1 Fall 2021 – Project 3 – Group 23
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
            csce274_fall2021_<project#>_<group#>.pdf
            e.g., csce274_fall2021_project3_group23.pdf

- Submit the Tag Zip of the code above to CSE Dropbox with:


### Rubric:
- Algorithm: 30 points
- Implementation: 40 points
- Reasonable tuning parameters: 10 points
- ROS package setup: 5 points
- ROS node implementation: 15 points
- PID class integration: 10 points
- Accuracy (scaled to your peers): 10 points
- Demo video: 15 points (Youtube link included in the pdf above)
- Answers to submission questions: 5 points
