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
![alt text](https://www.researchgate.net/profile/Roohollah_Amiri/publication/323867253/figure/fig2/AS:606095550738432@1521515848671/Reinforcement-Learning-Agent-and-Environment.png)





