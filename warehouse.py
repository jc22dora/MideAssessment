#!/usr/bin/python3
"""
Python Coding Exercise: Warehouse
=================================

You should implement your code in this file. See `README.txt` for full
instructions and more information.
"""

__author__ = "** John Doran **"
__email__  = "** Jc22dora@siena.edu **"
__date__   = "** 2/21/2022 **"

#==============================================================================
#
#==============================================================================

from cmath import inf


class Item:
    """ Example class for an item in the warehouse management system. You may
        modify or extend this in any way you need.
    """
    def __init__(self, size):
        self.size = size
        self.length = 1
        self.count = 1
        self.packed = None
        self.freevolume = 0
        self.capacity = size
#==============================================================================
#--- YOUR CODE GOES HERE.
#    At a minimum, you must define classes for Warehouse, Shelf, Bin, Box, and
#    Bag. You may define whatever else you may need as well.
#==============================================================================

class Container:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.size = 0
        self.freevolume = self.capacity
        self.packed = []
    # Returns the total number of objects (Items and/or Containers)
    # within the Container. Objects within Containers inside the Container are
    # not counted; a Bin containing a Box containing a Bag containing an Item
    # will have a length of 1.
    def __len__(self):
        return len(self.packed)

    # Return the total number of objects within the Container,
    # including other Containers and their contents. A Bin containing a
    # Box containing a Bag containing an Item will have a count() of 3.
    def count(self):
        count = 0
        for item in self.packed:
            item.packed.__len__ += count
        return count

    # Attempt to put a given object ('thing') in the
    # Container. If there is not enough room, the add fails and the method
    # returns False. If successful, the method returns True.
    def add(self, thing): 
        if thing != None and thing.size != None:
            if(self.freevolume >= thing.size and self.freevolume>=thing.capacity):
                if(self.capacity > thing.capacity):
                    self.length += thing.length
                    self.size += thing.size
                    self.freevolume -= thing.capacity
                    self.packed.append(thing)
                    return True
            else:
                return False
        else:
            return False
        
    # Check to see if a given 'thing' is within a
    # Container, or within a Container within the Container. Returns
    # True/False.
    def contains(self, thing):
        arr = self.pullItems(self.packed)
        for item in arr:
            if item == thing:
                return True
        return False

    # Recursive search for all elements within a list of lists
    # Returns 1d list
    def pullItems(self,iterable):
        result = []
        for x in iterable:
            if hasattr(x.packed, '__iter__'):
                result.append(x)
                result.extend(self.pullItems(x.packed))
            else:
                result.append(x)
        return result

    # This method can do two things. If 'thing' is
    # None or not provided, the last object added to the Container is
    # removed from the Container and returned. If a specific 'thing' is
    # specified, that specific 'thing' is removed. In either case, the
    # method returns either the removed object or `None` (if the
    # Container is empty or does not contain the specified object).
    def remove(self, thing=None):
        if self.packed == None:
            return None
        else:
            if thing == None:
                popped = self.packed[-1]
                del self.packed[-1]
                return popped
            else:
                self.packed.remove(thing)
                return thing

    # Attempt to put a given object into the Container.
    # Unlike add(), the method will attempt to find room for the object
    # inside any of the Containers within it.
    def pack(self,thing): 
        obj = self.pullItems(self.packed)
        obj = sorted(obj, key=lambda x:x.freevolume)
        success = False
        for o in obj:
            if thing.size <= o.freevolume:
                success = o.add(thing)
        return success

class Warehouse(Container):
    def __init__(self):
        Container.__init__(self,float("inf"))
class Shelf(Container):
    def __init__(self):
        Container.__init__(self,100)
class Bin(Container):
    def __init__(self):
        Container.__init__(self,10)
class Box(Container):
    def __init__(self):
        Container.__init__(self,5)
class Bag(Container):
    def __init__(self):
        Container.__init__(self,2)

