# Linux Setup

### Note: This is a basic setup for the host machine that will be used during the course both to program assignments and connect to the duckiebots. For more in-depth steps, use the [DT Manual](https://docs.duckietown.org/DT19/opmanual_duckiebot/out.pdf).

### Summary
* The official Linux distro supported by the course is: [Ubuntu 20.04 LTS (Focal Fossa)](https://releases.ubuntu.com/20.04/)

* I recommend that you nativly run Linux on your host machine (either signle or dual boot)

* The following are the packages needed:
    * pip3
    * git 
    * git-lfs 
    * curl 
    * wget
    * docker
    * docker-compose
    * duckietown-shell

### Step by Step

#### Prerequisites
        sudo apt update && sudo apt upgrade

#### Dependancies
        sudo apt install -y python3-pip git git-lfs curl wget

#### Docker
* Set up the repository
        
        sudo apt-get install apt-transport-https ca-certificates gnupg lsb-release

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

        echo \
        "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

* Install Docker Engine 

        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io

* Add docker to sudo group

        sudo groupadd docker
        sudo usermod -aG docker $USER

* Reboot

#### Docker-compose

        sudo apt-get install docker-compose

#### Duckietown-shell
* Install duckietown-shell (dts)
        
        pip3 install --no-cache-dir --user --upgrade duckietown-shell

* Reboot

* set dts version

        dts --set-version daffy