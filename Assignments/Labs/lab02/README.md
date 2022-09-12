## Lab 2 (3% of final grade) 

### Assigned: Sep 12, 2022
### Due: Sep 22, 2022

--------

#### Lab 2 will test your ability to create ROS packages, create ROS nodes, and integrate your code into existing infrastructure.
________

In Lab 1, you sent and received messages to a ROS node manually, using rostopic. In this lab, you will create a new node to send messages to the lab 1 node and a node to receive messages from it.

--------

## Steps

- Accept the Github Classroom [Assignment Repo](https://classroom.github.com/a/MDqz5gsY).

- Create a new ROS package in your repo. Reference [Video1](https://youtu.be/Y45ZWp26lHs), [video2](https://www.youtube.com/watch?v=txadk4vU5LE), and [ROS wiki](http://wiki.ros.org/ROS/Tutorials/CreatingPackage) for help

    NOTE: you may need to change the permissions of this folder so that it is accessible outside the docker container:
        
        chmod -R a+rw <package_folder>


- Create a new node inside this package that publishes to the input message you discovered in lab 1. You can send whatever numbers you like to the node as long as it is a value message. Test this node using rostopic echo.

    NOTE: If you do this with python, you will need to make your file executable using the command
    
        chmod +x <file_name>

    This will need to be done for each node you create.

- Create a second node that subscribes to the output of lab 1. Have it log each message it receives using the “INFO” warning level. Test this node using rostopic pub. Refer to class slides and video to display the output.

- Now create a launch file that:
    - Includes the launch file from lab 1
    - Starts your two nodes

- Test your package, code, and launch file thoroughly.

- Commit and push your code to your repo along with a tag (“lab2”)
    - Verify that you actually pushed your code AND TAG by checking github

