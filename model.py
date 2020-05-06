import torch
import torch.nn as nn
import torch.nn.functional as F 

class QNetwork(nn.Module):
    "Actor (Policy) Model"
    def __init__(self, state_size, action_size,seed, fc1_units=64, fc2_units=64, fc3_units=64):
        """ Initialize parameters and build model.
        Params
        ==========
            state_size(init): Dimension of each state
            action_size(init): Dimension of each action
            seed(int): randm seed
            fc1_units(int): Number of node in the first hidden layer
            fc2_units(int): Number nodes in the second hidden layer
            fc3_units(int): Number nodes in the third hidden layer
        """
        super(QNetwork,self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units,fc3_units)
        self.fc4 = nn.Linear(fc3_units,action_size)
    def forward(self, state):
        """Build a network the maps state --> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return self.fc3(x)



