'''
Calculations python module for engineering calculator project

Defines rudimentary calculations used within main.py
'''


# Basic

''' Force definition '''
def force_eqn():
    force = lambda m,a: m * a
    acceleration = lambda f,m: f / m
    mass = lambda f,a: f / a

''' Velocity definition '''
def velocity_eqn():
    velocity = lambda s,t: s / t
    displacement = lambda v,t: v * t
    time = lambda s,v: s * v

''' Momentum definition '''
def momentum_eqn():
    momentum = lambda m,v: m * v
    velocity = lambda p,m: p / m
    mass = lambda p,v: p / v

''' Acceleration definition '''
def acceleration_eqn():
    acceleration = lambda v,t: v / t
    velocity = lambda a,t: a * t
    time = lambda v,a: v * a

''' Density definition '''
def density_eqn():
    density = lambda m,v: m / v
    mass = lambda p,v: p * v
    volume = lambda m,p: m * p

''' Power definition '''
def power_eqn():
    def energy_term():
        power = lambda E,t: E / t
        energy = lambda P,t: P * t
        time = lambda P,E: P * E

    def work_term():
        power = lambda W,t: E / t
        work = lambda P,t: P * t
        time = lambda P,W: P * W

''' Efficiency definition '''
def efficiency():
    efficiency = lambda in,out: ((in - out) / in) * 100


# Mechanics

## TODO: Add equations for stress, strain, pressure, E, torque



# Structural

## TODO: Add equations for beams, bending, shearing, deflection, FoS


