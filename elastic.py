import bpy

uuid_store = {}

def elastic(current, target, bounce, decay, uuid):
    """ Elastic effect, with a bounce and decay factor

        elastic(current, target, bounce, decay, "my_elastic")
    """

    # get values
    prev = uuid_store.get(uuid, current)
    vel = uuid_store.get(uuid + "_vel", 0.0)

    # determine velocity
    vel += (target - current) * bounce
    vel *= decay

    # store values
    uuid_store[uuid] = current + vel
    uuid_store[uuid + "_vel"] = vel

    return current + vel

bpy.app.driver_namespace["elastic"] = elastic