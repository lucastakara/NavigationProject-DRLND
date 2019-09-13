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

The task is episodic, and in order to solve the environment, your agent must get an `average score of +13 over 100 consecutive episodes.``



`


