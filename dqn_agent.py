# Deep Q Network Agent

# Basic imports

import numpy as np
import random
from collections import namedtuple, deque

from model import QNetwork

import torch
import torch.nn.functional as F
import torch.optim as optim

BUFFER_SIZE = int(1e5) # Replay buffer size
BATCH_SIZE = 64 # minibatch size
GAMMA = 0.99 # discount factor
TAU = 1e-3 # for soft update of target parameters
LR = 5e-4 # learning rate
UPDATE_EVERY = 4 # how often to update the network

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu') 

class Agent():
    """ Interacts with and learns from the environment """
    
    def __init__(self, state_size, action_size, seed):
        """ Initialize an Agent object.
        
        Params
        ======
        state_size(int): Dimension of each state
        action_size(int): Dimension of each action
        seed(int): Random seed
        
        """
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(seed)
        
        # Q - Network
        self.qnetwork_local = QNetwork(state_size, action_size, seed).to(device)
        self.qnetwork_target = QNetwork(state_size, action_size, seed).to(device)
        self.optimizer = optim.Adam(self.qnetwork_local.parameters(), lr = LR)
        
        # Replay memory
        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, seed)
        # Initialize time step (for updating every UPDATE_EVERY STEPS)
        self.t_step = 0
        
        
    def step(self, state, action, reward, next_state, done):
        # Save experience in replay memory
        self.memory.add(state, action, reward, next_state, done)
        # Learn every UPDATE_EVERY time steps
        self.t_step = (self.t_step + 1) % UPDATE_EVERY
        if t_step == 0:
            # If enough samples are available in memory, get random subset and learn
            if len(self.memory) > BATCH_SIZE:
                experiences = self.memory.sample()
                self.learn(experiences, GAMMA)
    
    
    def act (self, state, eps = 0.):
        """ Returns actions for given state as per current policy 
        
        Params
        ======
        state(array_like): current state
        eps(float): epsilon, for epsilon-greedy action selection
        
        """
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        self.qnetwork_local.eval() # notify all layers that you are in eval mode
        with torch.no_grad(): # impacts the autograd engine and deactivate it.
            action_values = self.qnetwork_local(state)
        self.qnetwork_local.train() # Train mode
        
        # Epsilon-Greedy action selection
        if random.random() > eps:
            return np.argmax(action_values.cpu.data.numpy())
        else:
            return random.choice(np.arange(self.action_size))
    
            
        
        
        
        
        