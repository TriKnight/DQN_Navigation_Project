# DQN_Navigation_Project
This is the DQN_Navigation_Project 
## 1. Installation
The Project use the MLAngents version 0.4.0 so we need to do some following steps
### 1.1 Create virtual environment using conda

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

# install the requirements from our package
cd PATH_TO_OUR_PACKAGE
pip install -r requirements.txt

```
### 1.3 Create and Adding Kernel to Jupyter notebook
```
conda install -c anaconda ipykernel
python -m ipykernel install  --user --name=DQN_navigation
```
Open Jupyter notebok. Go to ```Kernel/Change Kernel/DQN_navigation```

## 2. Banana Navigation Environment
2.1 Reinforcement Block diagram
In the reinforcement learning. First step is determine what are the action, state, reward, agent, enviroment?

![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/reinforcement-learning-fig1-700.jpg)

<p align="center">
Fig1. Reinforcement Learning Diagram
</p>

**Number of Agent**: only 1 and moving the planar environment to collect the banana.

**Observation** : A set of 37 measurement ranges and kinds of objects in the environment.

**Action**: 4 discrete action [0, 1, 2, 3] with [Move forward, Move Backward, Turn Left, Turn Right]

**Reward**:  +1 when Agent get Yellow Banana and -1 when get Purple Banana


***Explain Detail Observation:***

7 ray perceptions with each ray include 5 entries (35 values) and 2 Value agent's velocity
![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/banana_env_observations.png)
[Source](https://wpumacay.github.io/research_blog/posts/deeprlnd-project1-navigation/?fbclid=IwAR2oHLD-WwJkBdyis6sHMgSDH7-LkjHxaZGELckBTY_Sy_qfLwaxGX2lp4I)

  *Fig2. Agent ray-perceptions. a) 7 rays reaching at least one object (banana or wall). b) One ray reaching the max. length before reaching any object*


Each ray is represented by a vector with 4th first elements are the indetical ray object detection and the last one is percentage of ray range, if ray range over the limit, it will be 0.0. The example show the ray[0 1 0 0 0.1534]


![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/ray_explain.png)

  *Fig3. Observation ray explain*


***Explain Detail Action***: 
4 Actions in the list bellow: 

*Action 0*: Move forward 
*Action 1*: Move backward
*Action 2*: Turn Left
*Action 3*: Turn Right


![alt text](https://github.com/TriKnight/DQN_Navigation_Project/blob/master/pics/banana_env_actions.png)
[Source](https://wpumacay.github.io/research_blog/posts/deeprlnd-project1-navigation/?fbclid=IwAR2oHLD-WwJkBdyis6sHMgSDH7-LkjHxaZGELckBTY_Sy_qfLwaxGX2lp4I)

   *Fig4. Action of the Agent*


        




