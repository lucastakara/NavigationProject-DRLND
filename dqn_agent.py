# Deep Q Network Agent

# Basic imports

import numpy as np
import random
from collections import namedtuple, deque

from model import Dueling_QNetwork

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
        self.qnetwork_local = Dueling_QNetwork(state_size, action_size, seed).to(device)
        self.qnetwork_target = Dueling_QNetwork(state_size, action_size, seed).to(device)
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
        if self.t_step == 0:
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
            action_values = self.qnetwork_target(state) # DDQN - Target estimate the action_values, local evaluate 
        self.qnetwork_local.train() # Train mode
        
        # Epsilon-Greedy action selection
        if random.random() > eps:
            return np.argmax(action_values.cpu().data.numpy())
        else:
            return random.choice(np.arange(self.action_size))
    
    def learn(self, experiences, gamma):
        """ Update value parameters using given batch of experience tuples.
        
        Params
        ======
        experiences(Tuple[torch.Variable]): tuple of (s,a,r,s',done) tuples
        gamma(float): discount factor
        
        """
        states, actions, rewards, next_states, dones = experiences
        
        # Get max predicted Q values (for next states) from target model
        Q_targets_next = self.qnetwork_target(next_states).detach().max(1)[0].unsqueeze(1)
        # Compute Q targets for current states
        Q_targets = rewards + (gamma *Q_targets_next*(1 - dones))
        # Get expected Q values from local model
        Q_expected = self.qnetwork_local(states).gather(1,actions)
        # Compute loss
        loss = F.mse_loss(Q_expected,Q_targets)
        # Minimize the loss
        self.optimizer.zero_grad() # set gradients to zero before starting to do backpropragation 
        loss.backward()
        self.optimizer.step() # performs a parameter update based on the current gradient 
        
        # -------- Update target Network --------- #
        self.soft_update(self.qnetwork_local, self.qnetwork_target, TAU)
        
        
    def soft_update(self, local_model, target_model, TAU):
        """ Soft update model parameters.
        ϴ_target = 𝜏 * ϴ_local + (1 - 𝛕) * ϴ_target
        
        Params
        ======
        local_model(Pytorch model): weights will be copied from
        target_model(Pytorch model): weights will be copied to
        TAU(float): interpolation parameter
        
        """
        for target_param, local_param in zip (target_model.parameters(), local_model.parameters()):
            target_param.data.copy_(TAU*local_param.data + (1.0 - TAU)*target_param.data)
            
    

class ReplayBuffer:
    """ Fixed-size buffer to store experience tuples. """
    
    def __init__(self, action_size, BUFFER_SIZE, BATCH_SIZE, seed):
        """ Initialize a ReplayBuffer object.
        
        Params
        ======
        action_size(int): Dimension of each action
        BUFFER_SIZE(int): Maximum size of buffer
        BATCH_SIZE(int): size of each training batch
        seed(int): Random seed
        
        """
        self.action_size = action_size
        self.memory = deque(maxlen = BUFFER_SIZE)
        self.BATCH_SIZE = BATCH_SIZE
        self.experience = namedtuple("Experience",field_names = ['state','action','reward','next_state','done'])
        self.seed = random.seed(seed)
        
    
    def add(self, state, action, reward, next_state, done):
        """ Add a new experience to memory. """
        e = self.experience(state, action, reward, next_state, done)
        self.memory.append(e)
    
    
    def sample(self):
        """ Randomly sample a batch of experiences from memory. """
        experiences = random.sample(self.memory, k = self.BATCH_SIZE)
        
        states = torch.from_numpy(np.vstack([e.state for e in experiences if e is not None])).float().to(device)
        actions = torch.from_numpy(np.vstack([e.action for e in experiences if e is not None])).long().to(device)
        rewards = torch.from_numpy(np.vstack([e.reward for e in experiences if e is not None])).float().to(device)
        next_states = torch.from_numpy(np.vstack([e.next_state for e in experiences if e is not None])).float().to(device)
        dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float().to(device)
        return (states, actions, rewards, next_states, dones)
    
    
    def __len__(self):
        """ Return the current size of internal memory. """
        return len(self.memory)
        
        
        
            
        
        
        
        
        