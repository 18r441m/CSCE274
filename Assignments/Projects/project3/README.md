## Project 3

### Assigned: October 28, 2022
### Due: November 14, 2022

--------

### The goal of the project is to program your robot to move. The instruction will take you step by step through the process. You will start by inspecting the Duckiebot to figure out which topics and messages control the wheels. Then, you will create a new package with a few nodes that make your Duckiebot move in different ways.

## Part 1

- Start your robot and start keyboard control on your laptop. Run 

        dts start_gui_tools <duckiebot_name>
    
    and use rqt_graph to inspect the nodes/topics. Use a combination of this graph and rostopic to find the various topics and messages that send commands to the wheels. Record the answers to the following questions:

    - What node converts joystick commands to robot commands?

    - What do you think car_cmd_switch_node does? If you’re not sure, start the lane following demo as see how the graph changes (or refer to Project 2 graphs).

    - What does the output of car_cmd_switch_node look like? Move the robot around and watch it change. Describe the components of the message (data types) and their purpose.

    - At some point, the command is converted from linear/angular velocity to commands for the left and right wheels. Which node does this?

    - During Project 2, you calibrated the wheels. Which node do you think accepts that calibration value and adjusts commands as needed?

- Start your container and create a new package for this project in the “packages” folder of your repo. Note that you will need to add duckietown_msgs as a dependency. This can be added to the end of the catkin_create_pkg command that you used before.

- Create a new node in that package that publishes a command to the output of car_cmd_switch_node. Select values that make your robot drive in a ~1m diameter circle. You will have to guess in this first trial, we will test in the next few steps. Make sure that you make this node executable (chmod +x <node_name>)

- Create a launch file for your node such that it looks something like this:

        <launch> 
            <group ns="duck44"> 
                YOUR NODE GOES HERE
            </group> 
        </launch>

    This will start your node inside the namespace for your robot. Make sure to commit these files.

---------------------
## At this point, you can exit the container. We can do the rest of this project from your Linux system.
---------------------

- We need to build the container with this new package in it, but we want to build it on the robot this time instead of on your laptop. Run:

        dts devel build -H <duckiebot_name>.local

- Now we need to run the code. Start the container on your robot with:

        dts devel run -H <duckiebot_name>.local -s -M --cmd bash
    
    The -s flag copies your repo to the /code folder on the robot so that it can be mounted by the -M flag and you do not need to rebuild for every small change.

- Make sure your robot can move using keyboard control. Note that when your code starts running, the robot will move and may be unpredictable. Be ready to stop your code with ctrl-c and take over with keyboard control. Your robot will continue doing the last command it was told until you stop it with keyboard control, even if you ctrl-c the launch file. Start your launch file on the robot (same terminal as above command) to test your code.

- Revise your code until your robot does exactly one circuit of a 1 meter circle. Have your robot stop at the end. Record your best run. You will be graded on precision at the resolution your instructor can see on the video you turn in. Once you are within a precision you find acceptable you can move on.

There are a few methods to revise your code:

- The easiest way to revise your code is to continue editing on your laptop and sync the files on your robot as needed using the same program as dts uses with the -s flag: rsync. To do this, run this command:

        rsync --archive <path/to/repo> duckie@<duckiebot>.local:/code/

    NOTE: in <path/to/repo> do NOT include the trailing “/”. It should look something like:

        /home/user/my_repo

- To avoid using rsync manually, you can exit your container and rerun the dts devel run command from the step above. This is a little tedious but a good way to test that your code works and will be committed to git properly when you are finished.

- You can also edit the code directly on your robot. Your repo is transferred to the /code folder on the robot. Note that you will have to sync these changes with your computer to turn in on git, so while this can be fast to test you run the risk of forgetting to turn in completed code.

- Finally, you can clone your repo onto your robot and run dts devel build/run through ssh without the -H command, just like you do on your laptop. If you do this and use ssh keys for git, do NOT use the default duckiebot keys because 1) everyone will have complete access to your repo and 2) someone already managed to do that so github will not allow you to upload your public key.

- Create a second node and launch file that makes your robot move in a 1 meter pentagon. Again, tune it to be as precise as possible and have it stop after one circuit.

## Part 2

### Dropbox submission

NOTE: Your submission should consist of one PDF file & (make sure you Tag your latest code you want to use as your submission code on the Github repo).

- Submit a PDF to CSE Dropbox with:

    * A youtube link to the video of:
        - your best attempt at the 1m circle pattern
        - your best attempt at the 1m pentagon pattern

    * Answers to the following questions:
        - What node converts joystick commands to robot commands? (2 points)

        - What do you think car_cmd_switch_node does? (2 points)

        - What does the output of car_cmd_switch_node look like? Move the robot around and watch it change. Describe the components of the message (data types) and their purpose. (2 points)

        - At some point, the command is converted from linear/angular velocity to commands for the left and right wheels. Which node does this? (2 points)

        - During Project 2, you calibrated the wheels. Which node do you think accepts this calibration value and adjusts commands as needed? (2 points)

        - What difficulties did you have in tuning your robot to make a pattern? (5 points)

        - Do you think you could make your robot reliably drive around a circular/oval track like you have at home without any feedback from the camera? Why or why not? (5 points)

    * pdf format instructions
        * Header with the class code, the semester and year, the homework number, and your UofSC username.
          e.g., CSCE 274 Section 1 Fall 2022 – Project 3 – ijsalman
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
            csce274_fall2022_<project#>_<UofSC username>.pdf
            e.g., csce274_fall2022_project3_ijsalman.pdf


- Submit the Github repos link (After making sure you create a tag for the current project to mark the submission)


### Rubric:
- 10 points: Package creation, repo and tag link
- 25 points: Circle node/launch file
- 10 points: Circle precision (mostly graded on uniformity of shape, not scale)
- 25 points: pentagon node/launch file
- 10 points: pentagon precision (mostly graded on uniformity of shape, not scale)
- 20 points: Answers to questions
