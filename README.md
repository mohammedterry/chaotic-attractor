# Chaotic Attractor
This code uses a chaotic attractor (the Lorenz equations) to create variations of any given input sequence (e.g. music, natural language, etc).  The variant has the general theme of the original data, however it remixes it slightly to add a funky new twist.  

# Lorenz Equations
Therefore the heart of this project is in computing the (chaotic) trajectory of the Lorenz Equations:

```
def lorenz(x,y,z, sigma=10.0, rho=28.0, beta=8.0/3, dt = 1e-2):
    # the lorenz system exhibits chaotic behaviour     
    # if sigma,rho,beta are set at these values
    xd = sigma * (y - x)
    yd = (rho-z)*x - y
    zd = x*y - beta*z
    # x,y,z derivatives calculated 
    # according to the lorenz equations
    x += xd * dt
    y += yd * dt
    z += zd * dt 
    return x,y,z
```

# Butterfly Effect
This isnt the only chaotic attractor out there, but it is one of the more famous ones. 
A 3D trajectory of the attractor looks like this:
[]!()
If you restart from the same initial conditions (x,y,z) BUT change one value ever so slightly (by a value of, say, +/- 0.001),
then the resulting trajectory will gradually diverge until it is wildly different from the original!!!
[]!()
This is called sensitive dependence on initial conditions (or more termed "the butterfly effect")

# Tests

There are tests provided in the code which demo the applications of this on various types of input data. 
A midi file (Bach's prelude in C) is hard coded into the file
is chaotically remixed by the program to create a musical variant:
[]!()

and a sample text is provided to show this chaotic reordering on natural language
(compare the story to the original)
[]!()

# How?
The original input data is stored along the x,y,z coordinates of the orinal trajectory.  
The second trajectory will pass by some of the first's trajectorie's coordinates, 
however, not in the exact same order (since its a chaotic variant).
The order it passes them is the order of the data sequence for the chaotic variant
Inspired by the online courses in Complexity Science at Santa Fe Institute
[]!()
