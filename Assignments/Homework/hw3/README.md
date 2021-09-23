## Homework 3 (3% over the final grade) 

### Assigned: September 23, 2021
### Due: September 30, 2021

--------

#### Homework 3 will test your ability to create ROS packages, create ROS nodes, and integrate your code into existing infrastructure.
________

In Homework 2, you sent and received messages to a ROS node manually, using rostopic. In this homework, you will create a new node to send messages to the homework 2 node and a node to receive messages from it.

--------

## Steps

- Create a new ROS package in your repo. Reference [slides](https://cse.sc.edu/~ijsalman/db/content/lectures/lec03.pdf), [Video](https://github.com/18r441m/CSCE274/tree/fall2021/Lecture/ROS), and [ROS wiki](http://wiki.ros.org/ROS/Tutorials/CreatingPackage) for help

    NOTE: you may need to change the permissions of this folder so that it is accessible outside the docker container:
        
        chmod -R a+rw <package_folder>


- Create a new node inside this package that publishes to the input message you discovered in homework 2. You can send whatever numbers you like to the node as long as it is a value message. Test this node using rostopic echo.

    NOTE: If you do this with python, you will need to make your file executable using the command
    
        chmod +x <file_name>

    This will need to be done for each node you create.

- Create a second node that subscribes to the output of homework 2. Have it log each message it receives using the “INFO” warning level. Test this node using rostopic pub. Refer to class slides and video to display the output.

- Now create a launch file that:
    - Includes the launch file from homework 2
    - Starts your two nodes

- Test your package, code, and launch file thoroughly.

- Commit and push your code to your repo along with a tag (“hw3”)
    - Verify that you actually pushed your code AND TAG by checking github


## Dropbox submission

- Sumbit the hw3 tag zip file from the previous step to CSE Dropbox



