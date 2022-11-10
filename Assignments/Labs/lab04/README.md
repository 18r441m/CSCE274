## Lab 4 (3% over the final grade) 

### Assigned: Nov 10, 2022
### Due: Nov 17, 2022

--------

#### Lab 05 will ask you to:
- Create a new ROS package
- Create a single ROS node that contains one subscriber and one publisher
- Remap a topic used in lab 2
- Take in a ROS parameter that selects which units to output:
- Meters
- Feet (no conversion)
- Smoots (1.7018 meters or 5.5833 feet, ref: https://www.larsondesigngroup.com/understanding-smoot/ )

The below steps will walk you through this process. 

NOTE: Do NOT modify lab 1 or lab 2 packages for this assignment.

________

lab 1 provided a node that sums the input it receives and posts it to the total topic. Let’s pretend this is part of a bigger project. Someone is using this to measure how far a wheel has gone (like an odometer) but realized that they were measuring in feet, but actually need the result in meters. We could rewrite some code to make these changes, but other people already like the code as is. Instead, let’s make a new package with a new node that subscribes to /lab1/total and publishes a new topic (call it what you like) with the same data, but in meters. We will also need to remap this topic to the subscriber node you created in lab 2.


--------

## Steps

- We will be using lab 2 Classroom [Assignment Repo](https://classroom.github.com/a/MDqz5gsY).

- Create your new package in the “packages” directory.

- Create a node in this package. It should:
    - Subscribe to /lab1/total
    - Contain a function to convert the input from feet to each of the above measurements (meters, feet, and smoots)
    - Publish a new topic (you can decide what to call it). Start by publishing any of the above conversions.


- Test this node with the code from lab 1 and 2 without making any changes to them. Make sure all units work.

- Now, we need to make the lab 2 subscriber listen to this new topic. Write a launch file that:
    - Starts each of the nodes from lab 1, 2, and 4. You can choose if you would like to import their launch file(s) or not. Regardless, make sure you start the lab 1 node in the lab 1 namespace.
    - Remaps the /lab1/total topic to whatever topic you created in step above. Note that this can be done in a few ways. Refer to class slides and videos.

- Once you verify the above works, we need to add one more thing: a parameter to control the units we output. Add logic to your callback function such that it checks the parameter’s state each time new data is received (so each time the callback runs) and outputs in whatever units are required. Also, log the units, inputs, and outputs to the INFO level. If no parameter is found, output to meters.

- Initialize this parameter in your launch file to convert to smoots.

- Use the command line tool rosparam to change the units as your code runs. Make sure it works by watching the log output. You may find the tool rqt_console a convenient way to watch this.

- Commit and push your code to your repo along with a tag (“lab4”)
    - Verify that you pushed your code AND TAG by checking Github


## Dropbox submission

- Submit a PDF to CSE Dropbox with:

    * The name of the node created

    * The name of the topic that node publishes on

    * The name of the parameter (in the launch file) and its accepted values

    * pdf format instructions
        * Header with the code of the class, the semester and year, the lab number, and your name.
          e.g., CSCE 274 Fall 2022 – Lab 4 – Ibrahim Salman
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
                csce274_fall2022_<lab#>_<last_name>.pdf
                e.g., csce274_fall2022_lab4_salman.pdf

- Sumbit the lab4 Github TAG link from the previos step to CSE Dropbox



