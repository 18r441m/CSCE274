## Project 4 (10% over the final grade) 

### Assigned: November 16, 2021
### Due: November 30, 2021

--------

# NOTE: Make sure to read the description carefully

#### The goal of this project is for you to produce a node that keeps your Duckiebot in its lane. Note that you already did this in [Project 3](../project3) and you can use some of the code from project 3. In project 3, you used the linear and angular velocities to guide the duckiebot by publishing to the switch_node topic, for this project, you should publish seperate wheel velocity commands, vel_left and vel_right. Also, one of the significant differences is that you cannot modify this [launch file](./project4.launch) except for the p, i, and d values. As you know, to drive forward, vel_left = vel_right, so, in the case of driving forward, you must use the rosparam "vel_min" and "vel_max" included in the launch file. When turning, you can modify only one wheel's velocity maintaining vel_min and vel_max. Also, note that you must use the PID values from the rosparams only.

--------

## Steps

- Tune your controller(s) until they work well on your Duckietown mats.

- To prove it is your code running, and not the lane following demo, please do the following:
    - Have your code output a unique message to loginfo or similar (logwarn/logerr will show up in amber/red on the screen and may be better for visibility) every time your main callback is run. Your message should be like:
        
            Duck: duck23, vel_min: 0, vel_max: .5, vel_left: .5, vel_right: .35, p: 1, i: 1, d: 1
    - Record the screen on your computer (preferably using a screen capture program) while your code is running with the following programs open:
        - A terminal showing that no lane controller nodes are running at the beginning (run “rosnode list” and show the output) and then showing roslaunch as it starts your controller.
        - rqt_image_view showing the Duckiebot’s camera view
        - rqt_console (if your custom message is not shown in the terminal)
        - NOTE: to run both rqt_console and rqt_image_view at the same time, use & at the end of the command to run in the background, like:

                rqt_image_view &
                rqt_console &
            You may need to press enter again to get back to the command prompt
    - Also record a top-down video of your Duckiebot performing lane following for at least three laps of your mats. Make sure this recording overlaps with the recording from the last step. You do NOT need to sync the videos or any other serious video editing, just make sure it is from the same run.


### Dropbox submission

NOTE: Your submission should consist of one PDF and one ZIP file.

- Submit a PDF to CSE Dropbox with:

    * A youtube link to the video you recorded

    * Answers to the following questions:
        - A description of what you choose to control (input and output signals) and why.
        - What final PID gain values did you use?
        - A description of the difference between this project (4) and the previous project (3)
        - A description of any problems you had completing this project
        - List each Group member's contribution


    * pdf format instructions
        * Header with the class code, the semester and year, the homework number, and your group.
          e.g., CSCE 274 Section 1 Fall 2021 – Project 4 – Group 23
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
            csce274_fall2021_<project#>_<group#>.pdf
            e.g., csce274_fall2021_project4_group23.pdf

- Submit the Tag Zip of the code above to CSE Dropbox with:
