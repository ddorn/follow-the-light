# Follow the Light

Follow the Light is a game where I test ideas. 
I don't care about coherence and don't expect 
anyone to actually play it.
 
It is my game oriented code sandbox. 

### Experiments that happened here

I may or may not write in more details about my experiments here 
on my [blog](https://ddorn.gitlab.io).

Here is a list of everything I tried here, and how it went (briefly).
It is kind of ordered by *when* those experiments happened.


 - Using Python for game development. Python is a fantastic language to
     work with, but slow, however if found that by using the right
     libraries, the speed of both development and execution is correct,
     even on my old laptop.
 - Using an ECS (Entity-Component-System) allows for things
    to be much more independent which is a must in
    this project and in any game really
 - Using [moderngl](https://github.com/moderngl/moderngl) 
    allowed me to not care about the low level opengl code
    while still having the control I wanted. 
    It made it possible to have great performances 
    and experiment with shaders.
 - Entirely separate game logic and rendering. 
    The logic is 100% agnostic of the rendering engine
    or input system, which I found very nice, even if it is 
    unlikely that one would develop different rendering methods
    for a game, but because it offers a good structure and
    follow the principle of [separation of concerns](https://github.com/moderngl/moderngl).
 - Creating a fog shader, thanks to [The Book of Shaders](https://thebookofshaders.com/)
 - Smooth scaling pixel art to non-integer multiple 
    by using a nearest filter and on the conflicting 1px borders
    a linear filter. 
    Idea from [Cláudio Fernandes](https://csantosbh.wordpress.com/2014/01/25/manual-texture-filtering-for-pixelated-games-in-webgl/).
 - Using a state machine to represent the state (Running/Jumping...) 
    of the player. 

### Experiments that I would like to do
 - separate update and rendering in the game loop, and using 
    prediction to render things at the right position.
    [Koen Witters' article](https://dewitters.com/dewitters-gameloop/)
    about game loops is a must read in this domain.

### Resources

I would recommend to anyone to read every article here
that they are interested in.
 
About ECS:
 - [esper](https://github.com/benmoran56/esper): 
    a python ECS implementation, from which my ECS is base
    
About shaders and generative art:
 - [The Book of Shaders](https://thebookofshaders.com/):
    A great read (the best ?) for anyone who want to discover
    and master generative art with fragment shaders.
    
About state machines:
 - [The State Pattern](http://gameprogrammingpatterns.com/state.html):
    A chapter about state machines from a game design perspective,
    but the whole book is worth reading.
    
 About the game loop:
  - [Koen Witters' article](https://dewitters.com/dewitters-gameloop/)
    is a clear and detailed explanations of the different game loops
    possible in a game and how to make them *better*.
  - [Fix your Timestep!](https://www.gafferongames.com/post/fix_your_timestep/)
    a good article about the same things as the one above but with a focus
    on how to integrate numerically a physics system and what could go wrong.


### Install and run

Can we still play that experimental game if we want to ?
Yes, sure.

You will need python 3.7+ and [Poetry](https://python-poetry.org/) to get the dependencies.

```shell script
git clone git@gitlab.com:ddorn/follow-the-light.git
cd follow-the-light
poetry install
./make.sh run
```
