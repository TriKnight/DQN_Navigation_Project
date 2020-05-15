# DQN_Navigation_Project
This is the DQN_Navigation_Project 
## 1. Setup Environment and Installation Requirements
The Project use the MLAngents version 0.4.0 so we need to do some following steps
### 1.1 Install Anaconda & Create virtual environment using conda
Install Anaconda following link bellow

https://www.anaconda.com/products/individual

Create virtual environment

```
# Create the virtual env DQN
conda create -n DQN_navigation python=3.6
# activate environment
source activate DQN_navigation
```
### 1.2 Install all dependence
```

# clone the udacity repo
git clone https://github.com/udacity/deep-reinforcement-learning.git

# go to the python folder of the repo
cd deep-reinforcement-learning/python

# install the unityagents package from this folder
pip install -e .

# git clone DQN_Navigation_Project
cd ..
git clone https://github.com/TriKnight/DQN_Navigation_Project

# install the requirements from our package
cd DQN_Navigation_Project
pip install -r requirements.txt

```
### 1.3 Create and Adding Kernel to Jupyter notebook
```
conda install -c anaconda ipykernel
python -m ipykernel install  --user --name=DQN_navigation
```
Open Jupyter notebok. 
```
jupyter notebook
```

Go to ```Kernel/Change Kernel/DQN_navigation```

### 1.4 Download Environment
1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.
 
### 1.5 DRLND GitHub repository
2. Place the file in the DRLND GitHub repository, in the `DQN_Navigation_Project/` folder, and unzip (or decompress) the file. 


## 2. Banana Navigation Environment

Reinforcement Block diagram
In the reinforcement learning. First step is determine what are the action, state, reward, agent, enviroment?

[![Watched Trained Agent](http://i3.ytimg.com/vi/OaNuVnunzmA/maxresdefault.jpg)](https://youtu.be/OaNuVnunzmA)


![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/reinforcement-learning-fig1-700.jpg)

<p align="center">
Fig1. Reinforcement Learning Diagram
</p>

**Number of Agent**: only 1 and moving the planar environment to collect the banana.

**Observation** : A set of 37 measurement ranges and kinds of objects in the environment.

**Action**: 4 discrete action [0, 1, 2, 3] with [Move forward, Move Backward, Turn Left, Turn Right]

**Reward**:  +1 when Agent get Yellow Banana and -1 when get Purple Banana


***Explain Detail Observation:*** 7 ray perceptions with each ray include 5 entries (35 values) and 2 Value agent's velocity
![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/banana_env_observations.png)

<p align="center">
  Fig2. Agent ray-perceptions. a) 7 rays reaching at least one object (banana or wall). b) One ray reaching the max. length before reaching any object 
</p>


Each ray is represented by a vector with 4th first elements are the indetical ray object detection and the last one is percentage of ray range, if ray range over the limit, it will be 0.0. The example show the ray[0 1 0 0 0.1534]


![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/ray_explain.png)

<p align="center">
  Fig3. Observation ray explain
</p>

***Explain Detail Action***: 4 Actions in the list bellow: 

*Action 0*: Move forward 
*Action 1*: Move backward
*Action 2*: Turn Left
*Action 3*: Turn Right


![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/banana_env_actions.png)


<p align="center">
   Fig4. Action of the Agent
</p>

### 3. The DQN Algorithms:
Following the papper 
["Human-level control through deep reinforcementlearning"](http://files.davidqiu.com//research/nature14236.pdf)
.We have the DQN Algorithms with experience replay:

![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/DQN_Algorithm.png)

<p align="center">
   Fig5. The DQN Algorithms
</p>



### References:
1. https://wpumacay.github.io/ [link](https://wpumacay.github.io/research_blog/posts/deeprlnd-project1-navigation/?fbclid=IwAR2oHLD-WwJkBdyis6sHMgSDH7-LkjHxaZGELckBTY_Sy_qfLwaxGX2lp4I)

       



