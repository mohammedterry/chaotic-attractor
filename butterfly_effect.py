import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def chaotic_reorder(xi=random.random() * 10 - 5 ,yi = random.random() * 10 - 5,zi = random.random() * 10 - 5,len_seq = 5000):
    traj_original = {}
    traj_variant = {}
    x1,y1,z1 = [],[],[]
    x2,y2,z2 = [],[],[]
    variant_seq = []
    x1.append(xi)
    y1.append(yi)
    z1.append(zi)
    x2.append(xi + 0.01)
    y2.append(yi)
    z2.append(zi)
    
    for n in range(len_seq):
        xn1,yn1,zn1 = lorenz(x1[n],y1[n],z1[n])
        xn2,yn2,zn2 = lorenz(x2[n],y2[n],z2[n])    
        x1.append(xn1)
        y1.append(yn1)
        z1.append(zn1) 
        x2.append(xn2)
        y2.append(yn2)
        z2.append(zn2)
        traj_original[n] = (round(xn1,1),round(yn1,1),round(zn1,1)) 
        traj_variant[(round(xn2,1),round(yn2,1),round(zn2,1))] = n

    for n in range(len(traj_original)):
        xyz = traj_original[n]
        if xyz in traj_variant:
            variant_seq.append(traj_variant[xyz])
    
    #plot the 2 trajectories created
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.scatter(x1, y1, z1, s=.5)
    ax.scatter(x2, y2, z2, s=.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Lorenz')
    plt.show()

    return variant_seq

def test_with_music():
    import pygame.midi
    import time
    
    pygame.midi.init()
    player = pygame.midi.Output(0)
    player.set_instrument(0)

    song = []
    melody = [60, 64, 67, 72, 76, 67, 72, 76,  #bach prelude
              60, 64, 67, 72, 76, 67, 72, 76,
              60, 62, 69, 74, 77, 69, 74, 77,
              60, 62, 69, 74, 77, 69, 74, 77,              
              59, 62, 67, 74, 77, 67, 74, 77,
              59, 62, 67, 74, 77, 67, 74, 77,
              60, 64, 67, 72, 76, 67, 72, 76,
              60, 64, 67, 72, 76, 67, 72, 76,
              60, 64, 69, 76, 81, 69, 76, 81,
              60, 64, 69, 76, 81, 69, 76, 81,
              60, 62, 66, 69, 74, 66, 69, 74,
              60, 62, 66, 69, 74, 66, 69, 74,
              59, 62, 67, 74, 79, 67, 74, 79,
              59, 62, 67, 74, 79, 67, 74, 79,              
              59, 60, 64, 67, 72, 64, 67, 72,
              59, 60, 64, 67, 72, 64, 67, 72,
              57, 60, 64, 67, 72, 64, 67, 72,
              57, 60, 64, 67, 72, 64, 67, 72,
              50, 57, 62, 66, 72, 62, 66, 72,
              50, 57, 62, 66, 72, 62, 66, 72,
              55, 59, 62, 67, 71, 62, 67, 71,
              55, 59, 62, 67, 71, 62, 67, 71, 
              55, 58, 64, 67, 73, 64, 67, 73,             
              55, 58, 64, 67, 73, 64, 67, 73,
              53, 57, 62, 69, 74, 62, 69, 74,
              53, 57, 62, 69, 74, 62, 69, 74,
              53, 56, 62, 65, 71, 62, 65, 71,
              53, 56, 62, 65, 71, 62, 65, 71,
              52, 55, 60, 67, 72, 60, 67, 72,
              52, 55, 60, 67, 72, 60, 67, 72,
              52, 53, 57, 60, 65, 57, 60, 65,
              52, 53, 57, 60, 65, 57, 60, 65,
              50, 53, 57, 60, 65, 57, 60, 65,
              50, 53, 57, 60, 65, 57, 60, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              48, 52, 55, 60, 64, 55, 60, 64,
              48, 52, 55, 60, 64, 55, 60, 64,
              48, 55, 58, 60, 64, 58, 60, 64,
              48, 55, 58, 60, 64, 58, 60, 64,
              41, 53, 57, 60, 64, 57, 60, 64,
              41, 53, 57, 60, 64, 57, 60, 64,
              42, 48, 57, 60, 63, 57, 60, 63,
              42, 48, 57, 60, 63, 57, 60, 63,
              44, 53, 59, 60, 62, 59, 60, 62,
              44, 53, 59, 60, 62, 59, 60, 62,
              43, 53, 55, 59, 62, 55, 59, 62,
              43, 53, 55, 59, 62, 55, 59, 62,
              43, 52, 55, 60, 64, 55, 60, 64,
              43, 52, 55, 60, 64, 55, 60, 64,
              43, 50, 55, 60, 65, 55, 60, 65,
              43, 50, 55, 60, 65, 55, 60, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              43, 51, 57, 60, 66, 57, 60, 66,
              43, 51, 57, 60, 66, 57, 60, 66,
              43, 52, 55, 60, 67, 55, 60, 67,
              43, 52, 55, 60, 67, 55, 60, 67,
              43, 50, 55, 60, 65, 55, 60, 65,
              43, 50, 55, 60, 65, 55, 60, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              43, 50, 55, 59, 65, 55, 59, 65,
              36, 48, 55, 58, 64, 55, 58, 64,
              36, 48, 55, 58, 64, 55, 58, 64,
              36, 48, 53, 57, 60, 65, 60, 57, 60, 57, 53, 57, 53, 50, 53, 50, 
              57, 67, 71, 74, 77, 74, 71, 74, 71, 67, 71, 62, 65, 64, 62, 60 ]
    for i in range(10):
        song.extend(melody)

    for note in melody:
        player.note_on(note,127)
        time.sleep(0.1)
        player.note_off(note,127)

    new_seq = chaotic_reorder(len_seq = len(song))
    for i in new_seq:
        player.note_on(song[i], 127)
        time.sleep(0.1)
        player.note_off(song[i], 127)

    del player
    pygame.midi.quit()

def test_with_story():
    variant_content = []
    with open('sample_dataset.txt') as f:
        content = f.readlines()
    new_seq = chaotic_reorder(len_seq = len(content))
    for i in new_seq:
        variant_content.append(content[i])
    return variant_content

def test_with_letters():
    variant_content = []
    with open('sample_dataset.txt') as f:
        content = f.read()
    new_seq = chaotic_reorder(len_seq = len(content))
    for i in new_seq:
        variant_content.append(content[i])
    return ''.join(variant_content)

test_with_music()
#print(test_with_letters())
print(test_with_story())