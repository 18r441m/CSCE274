FROM ros:noetic

RUN apt update && apt upgrade -y

RUN apt install -y vim tmux

RUN echo 'source /ros_entrypoint.sh' >> ~/.bashrc

RUN mkdir -p /catkin_ws/src

WORKDIR /catkin_ws
