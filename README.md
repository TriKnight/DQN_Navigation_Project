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

![alt text](https://www.researchgate.net/profile/Roohollah_Amiri/publication/323867253/figure/fig2/AS:606095550738432@1521515848671/Reinforcement-Learning-Agent-and-Environment.png)

In this project:

**Number of Agent**: only 1 and moving the planar environment to collect the banana.

**Observation** : A set of 37 measurement ranges and kinds of objects in the environment.

**Action**: 4 discrete action [0, 1, 2, 3] with [Move forward, Move Backward, Turn Left, Turn Right]

**Reward**:  +1 when Agent get Yellow Banana and -1 when get Purple Banana




