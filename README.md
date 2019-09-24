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


### Step 2: Dependencies

___

To set up your Python environment, follow these instructions:

#### 1. Open your Terminal/Command Prompt.

#### 2. Create (and activate) a new environment with **`Python 3.6`**
- For **Linux** or **Mac** users:
>conda create --name drlnd python=3.6
>source activate drlnd
- For **Windows** users:
>conda create --name drlnd python=3.6 
>activate drlnd

####  3. Install Gym environment

OpenAI Gym is a toolkit for developing and comparing reinforcement learning algorithms. This is the `gym` open-source library, which gives you access to standardized set of environments.

- Installation

You can perform a minimal install of the packaged version directly from PyPI:

>**pip install gym**

#### 4. Clone the repository (if you haven't already) and navigate to the `python/` folder. then, install the dependencies.

>`git clone https://github.com/udacity/deep-reinforcement-learning.git`

>`cd deep-reinforcement-learning/python`

>`pip install .`

#### 5. Create an [IPython kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment
>`python -m ipykernel install --user --name drlnd --display-name "drlnd"`

#### 6. Install [Numpy](https://numpy.org/) Library 

NumPy is the fundamental package for array computing with Python.
We will be using the 1.12.1 version on this project. 

- Installation:

>`pip install numpy==1.12.1`

#### 7. Install [Matplotlib](https://matplotlib.org/2.1.0/index.html) Library

Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.

On your Command line, type:

>`conda install matplotlib=2.1.1`

#### 8. Install [Unity Machine Learning Agents Package](https://pypi.org/project/unityagents/):

Unity Machine Learning Agents allows researchers and developers to transform games and simulations created using the Unity Editor into environments where intelligent agents can be trained using reinforcement learning, evolutionary strategies, or other machine learning methods through a simple to use Python API.

- Installation via pip: 

>`pip install unityagents`


#### 8. Install [Pytorch](https://pytorch.org/) Library

Pytorch is an open source machine learning framework that accelerates the path from research prototyping to production deployment. It will be used for creating and training our artificial neural networks.

- For **Mac** users: 

via conda:

`conda install pytorch=0.4.1 cuda80 -c pytorch`

- For **Windows** users:

Download the `whl` file with the version 0.4.1 from the following html page:

`https://download.pytorch.org/whl/cu80/torch_stable.html`

Then, install the file with `pip install [downloaded file]`

- For **Linux** users:

Acess [Pytorch](https://pytorch.org/get-started/previous-versions/)
and download the `whl` file and install it with

`pip install [downloaded file]`

Other packages that may be installed are listed on the `requirements.txt` file.


##### 10. Before running code in a notebook, change the kernel to match the `drlnd` environment that we created by using the drop-down `Kernel`menu.

![Image provided by Udacity](https://user-images.githubusercontent.com/10624937/42386929-76f671f0-8106-11e8-9376-f17da2ae852e.png)




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

### Training the Network

---

Once you're done with setting up your environment, it's time to train our network! In the `model.py`file, there are two options of network:
1. QNetwork 
2. Dueling_QNetwork

To train the weight of the first network, you must make some changes in the `navigation.py` file:

