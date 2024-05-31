import bpy
import math

uuid_store = {}


def easeInOutSine(t, start = 0, end = 1):
    """
    Easing equation function for a sinusoidal (sin(t)) ease-in-out, accelerating until halfway, then decelerating.
    """
    t = (t - start) / (end - start)  # normalize t to the range [0, 1]
    
    eased = -0.5 * (math.cos(math.pi * t) - 1)

    return eased * (end - start) + start

def easeInOutQuad(t, start = 0, end = 1):
    """
    Easing equation function for a quadratic (t^2) ease-in-out, accelerating until halfway, then decelerating.
    """
    t = (t - start) / (end - start)  # normalize t to the range [0, 1]
    
    eased = t < 0.5 and 2 * t * t or -1 + (4 - 2 * t) * t

    return eased * (end - start) + start

def easeInOutCubic(t, start = 0, end = 1):
    """
    Easing equation function for a cubic (t^3) ease-in-out, accelerating until halfway, then decelerating.
    """
    t = (t - start) / (end - start)  # normalize t to the range [0, 1]
    
    eased = t < 0.5 and 4 * t * t * t or (t - 1) * (2 * t - 2) * (2 * t - 2) + 1

    return eased * (end - start) + start

def easeInOutQuart(t, start = 0, end = 1):
    """
    Easing equation function for a quartic (t^4) ease-in-out, accelerating until halfway, then decelerating.
    """
    t = (t - start) / (end - start)  # normalize t to the range [0, 1]
    
    eased = t < 0.5 and 8 * t * t * t * t or 1 - 8 * (t - 1) * t * t * t

    return eased * (end - start) + start

def easeInOutQuint(t, start = 0, end = 1):
    """
    Easing equation function for a quintic (t^5) ease-in-out, accelerating until halfway, then decelerating.
    """
    t = (t - start) / (end - start)  # normalize t to the range [0, 1]
    
    eased = t < 0.5 and 16 * t * t * t * t * t or 1 + 16 * (t - 1) * t * t * t * t

    return eased * (end - start) + start


def bounce(current, speed = .1, max = 1, min = 0, uuid = 'bounce'):
    """ Oscillate between max and min values at speed,
        with some smoothing

        bounce(current, speed, max, min, "my_bounce")
    """

    if speed <= 0:
        return current

    #get values
    direction = uuid_store.get(uuid + "_dir", True) # True = min -> max, False = max -> min
    prev = uuid_store.get(uuid, current)

    #calculate the distance to cover in this iteration
    distance = (max - min) * speed
    if not direction:
        distance = -distance

    #calculate the new value with smoothing
    #new_value = easeInOutSine(prev + distance, prev, prev + distance)
    #new_value = easeInOutQuad(prev + distance, prev, prev + distance)
    #new_value = easeInOutCubic(prev + distance, prev, prev + distance)
    #new_value = easeInOutQuart(prev + distance, prev, prev + distance)
    new_value = easeInOutQuint(prev + distance, prev, prev + distance)
        
    #check if we need to change direction
    fudge_factor = 0.001
    if new_value > max or abs(new_value - max) < fudge_factor:
        new_value = max
        direction = False
    elif new_value < min or abs(new_value - min) < fudge_factor:
        new_value = min
        direction = True

    #store the new values
    uuid_store[uuid] = new_value
    uuid_store[uuid + "_dir"] = direction

    return new_value

bpy.app.driver_namespace["bounce"] = bounce