## Homework 5 (3% over the final grade) 

### Assigned: october 21, 2021
### Due: october 28, 2021

--------

#### Homework 5 will ask you to:
- Create a new ROS package
- Create a single ROS node that contains one subscriber and one publisher
- Remap a topic used in homework 3
- Take in a ROS parameter that selects which units to output:
- Meters
- Feet (no conversion)
- Smoots (1.7018 meters or 5.5833 feet, ref: https://www.larsondesigngroup.com/understanding-smoot/ )

The below steps will walk you through this process. 

NOTE: Do NOT modify homework 2 or homework 3 packages for this assignment.

________

Homework 2 provided a node that sums the input it receives and posts it to the total topic. Let’s pretend this is part of a bigger project. Someone is using this to measure how far a wheel has gone (like an odometer) but realized that they were measuring in feet, but actually need the result in meters. We could rewrite some code to make these changes, but other people already like the code as is. Instead, let’s make a new package with a new node that subscribes to /homework1/total and publishes a new topic (call it what you like) with the same data, but in meters. We will also need to remap this topic to the subscriber node you created in homework 3.


--------

## Steps

- Create your new package in the “packages” directory of your repo as in Homework 3.


- Create a node in this package. It should:
    - Subscribe to /homework2/total
    - Contain a function to convert the input from feet to each of the above measurements (meters, feet, and smoots)
    - Publish a new topic (you can decide what to call it). Start by publishing any of the above conversions.


- Test this node with the code from homework 2 and homework 3. Make sure all units work.

- Now, we need to make the homework 3 subscriber listen to this new topic. Write a launch file that:
    - Starts each of the nodes from homework 2, 3, and 5. You can choose if you would like to import their launch file(s) or not. Regardless, make sure you start the homework2 node in the homework2 namespace.
    - Remaps the /homework2/total topic to whatever topic you created in step above. Note that this can be done in a few ways. Refer to class slides and videos.

- Once you verify the above works, we need to add one more thing: a parameter to control the units we output. Add logic to your callback function such that it checks the parameter’s state each time new data is received (so each time the callback runs) and outputs in whatever units are required. Also, log the units, inputs, and outputs to the INFO level. If no parameter is found, output to meters.

- Initialize this parameter in your launch file to convert to smoots.

- Use the command line tool rosparam to change the units as your code runs. Make sure it works by watching the log output. You may find the tool rqt_console a convenient way to watch this.

- Commit and push your code to your repo along with a tag (“hw5”)
    - Verify that you pushed your code AND TAG by checking Github


## Dropbox submission

- Submit a PDF to CSE Dropbox with:

    * The name of the node created

    * The name of the topic that node publishes on

    * The name of the parameter (in the launch file) and its accepted values

    * pdf format instructions
        * Header with the code of the class, the semester and year, the homework number, and your name.
          e.g., CSCE 274 Section 1 Fall 2021 – Homework 5 – Ibrahim Salman
          
        * Your answers, clearly identifying the answered assignments.

        * The name of the file should be in the following format:
        
                csce274_fall2021_<hw#>_<last_name>.pdf
                e.g., csce274_fall2021_hw5_salman.pdf

- Sumbit the HW5 Github TAG zip file from the previos step to CSE Dropbox



