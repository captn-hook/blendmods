import bpy
import math

store = {}


def ease(t, max_val, min_val, pow=2):
    t = (t - min_val) / (max_val - min_val)  # Normalize t to the range [0, 1]
    t = max(0, min(1, t))  # Clamp t to the range [0, 1]
    return min_val + (max_val - min_val) * ((t ** pow) / (t ** pow + (1 - t) ** pow))


def bounce(current=0.0, speed=1.0, max=1.0, min=0.0, easeMax=3, easeMin=1.5, name='bounce'):
    """
    current: the current value of the driven property
    speed: how fast the value should change
    max: the maximum value the property should reach, then switch direction
    min: the minimum value the property should reach, then switch
    easeOut: the ease out function to use, sin or a power of t
    easeIn: the ease in function to use
    name: the name of the property to store the value in, if you want to use multiple

    returns: the next value of the property
 
    bounce(self.location[0], speed, max, min, '5', '3', 'bounce_x')
    bounce(self.location[1], speed, max, min, '5', '3', 'bounce_y')
    bounce(self.location[2], speed, max, min, '5', '3', 'bounce_z')

    bounce(self.rotation_quaternion[0], speed, max, min, '5', '3', 'bounce_x')
    bounce(self.rotation_quaternion[1], speed, max, min, '5', '3', 'bounce_y')
    bounce(self.rotation_quaternion[2], speed, max, min, '5', '3', 'bounce_z')
    bounce(self.rotation_quaternion[3], speed, max, min, '5', '3', 'bounce_w')
    """

    if bpy.context.scene.frame_current <= 1 or name not in store:
        store[name + '_dir'] = 1
        store[name] = max
        return max
    
    if speed <= 0 or max <= min:
        return current
    
    current = store.get(name, current)
    
    # speed, max, and min are input math functions
    # current is the driven value on last frame
    # we want to oscillate between max and min at speed (with an optional ease)

    ndir = 0 # 1 is min to max, -1 is max to min
    # do we need to switch direction?
    if current >= max:
        ndir = -1
        store[name + '_dir'] = ndir
        store[name] = max
    elif current <= min:
        ndir = 1
        store[name + '_dir'] = ndir
        store[name] = min
        
    next = current + speed * store.get(name + '_dir', ndir)
    store[name] = next

    #if we are closer to max, use easeMax, else use easeMin
    if abs(max - next) < abs(min - next):
        return ease(next, max, min, easeMax)
    else:
        return ease(next, max, min, easeMin)

bpy.app.driver_namespace['bounce'] = bounce 
