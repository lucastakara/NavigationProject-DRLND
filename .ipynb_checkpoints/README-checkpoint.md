# DRLND - Navigation Project

Author: Lucas Takara  Date: 09/13/2019


### Project Details
___________

### Environment

![Banana](https://raw.githubusercontent.com/RMiftakhov/NavigationProject-drlnd/master/banana-gif.gif )



The goal of this project is to train an agent to navigate and collect bananas in a squared world! It has to collect as many yellow bananas as possible while avoiding purple bananas.


### Details 

This environment was developed on Unity Real-Time Development Platform and it has some peculiarities:

- A reward of +1 is provided for collecting a yellow banana 
- A reward of -1 is provided for collecting a purple banana


The state space has **37** dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- **`W`** - move forward (Note: when playing the game, the agent will move forward, if you don't select a different action in time)
- **`S`** - move backward
- **`A`** - move left
- **`D`** - move right

The task is episodic and in order to solve the environment, your agent **must** get an `average score of +13 over 100 consecutive episodes.`


### Installation

Follow the instructions bellow to install the environment on your own machine:

### Step 1: Clone the DRLND Repository
___

If you haven't already, please follow the instructions in Udacity's [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment. By following these instructions, you will install `PyTorch`, `ML-Agents toolkit` and a few more Python packages required to install the project.


### Step 2: Download the Unity Environment
____

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows 32 bits: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows 64 bits: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)


Once you've downloaded it, place the file in the **`p1_navigation/`** folder in the DRLND GitHub repository, and unzip (or decompress) the file.

(For Windows users) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

### Step 3: Download Anaconda Distribution (Optional)
----

For this project, we'll be using the `Jupyter Notebook` software which comes along with the Anaconda Distribution. 

- Linux: [click here](https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh)
- Mac OSX: [click here](https://repo.anaconda.com/archive/Anaconda3-2019.07-MacOSX-x86_64.pkg)
- Windows 32: [click here](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86.exe)
- Windows 64: [click here](https://repo.anaconda.com/archive/Anaconda3-2019.07-Windows-x86_64.exe)


### Step 4: Connecting Python with the Environment
----

In order to connect python with the environment, which is already saved in the Workspace, please import a few libraries and instantiate an object providing the location of the environment (see example below):

- `import numpy as np`
- `from unityagents import UnityEnvironment`
 
` env = UnityEnvironment(file_name="/Users/Desktop/Banana.app)`

