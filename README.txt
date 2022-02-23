Python Coding Exercise: Model Warehouse
=======================================

This exercise should take no more than a couple of hours to implement,
including any docstrings and in-line comments. You have 48 hours after
downloading to complete it. You may use any version of Python 3.

NOTE: THESE FILES ARE NOT TO BE REDISTRIBUTED, IN WHOLE OR IN PART,
YOUR SOLUTION INCLUDED.

---

You have been given the task of implementing the basics of a warehouse
inventory management system. The warehouse contains Items packed into
Containers. There are several sizes of container, each with different
capacities:

**Container**  **Capacity** (in 'volume units')
 Warehouse     Infinite
 Shelf         100 units
 Bin           10 units
 Box           5 units
 Bag           2 units

While Containers are of fixed size, Items vary in size from 1 to 20 volume
units. Any Container can hold a combination of Items and other Containers
smaller than itself, up to that Container's maximum capacity. You can assume
that a Container's capacity is the same as its exterior size, so a Box would
occupy 5 volume units in a Bin. The exterior size of a Container is not
affected by its contents.

All Containers must have the following methods:

  - __len__(): Returns the total number of objects (Items and/or Containers)
    within the Container. Objects within Containers inside the Container are
    not counted; a Bin containing a Box containing a Bag containing an Item
    will have a length of 1.
  - count(): Return the total number of objects within the Container,
    including other Containers and their contents. A Bin containing a
    Box containing a Bag containing an Item will have a count() of 3.
  - add(thing): Attempt to put a given object ('thing') in the
    Container. If there is not enough room, the add fails and the method
    returns False. If successful, the method returns True.
  - contains(thing): Check to see if a given 'thing' is within a
    Container, or within a Container within the Container. Returns
    True/False.
  - remove([thing]): This method can do two things. If 'thing' is
    None or not provided, the last object added to the Container is
    removed from the Container and returned. If a specific 'thing' is
    specified, that specific 'thing' is removed. In either case, the
    method returns either the removed object or `None` (if the
    Container is empty or does not contain the specified object).
  - pack(thing): Attempt to put a given object into the Container.
    Unlike add(), the method will attempt to find room for the object
    inside any of the Containers within it.

Optionally, you may also implement any or all of the following:

Bonus 1: Limit the Shelf to storing only Items larger than 7 units.
Smaller Items must be within Containers.

Bonus 2: Have the add() and pack() methods automatically remove the added
object from the Container it previously occupied, so it cannot be in two
places at once.

Bonus 3: Implement a new Container method, extract(thing), which is similar
to remove(thing) but will remove a given object ('thing') from the Container
or any Container within it. Unlike remove(), this method requires a specific
object. This method should return the extracted object, or `None` if 'thing'
is not anywhere within the Container.

Note: in the descriptions above, 'thing' and 'object' can refer to either an
Item, or any type of Container that isn't specifically excluded.

---

Approach and implement this as if it were a real work assignment. Imagine
that other people will see and use your code, possibly years from now. As
such, it should contain appropriate docstrings and comments.

Your code should be implemented in the file `warehouse.py`. The file contains
a minimal implementation of an `Item` class, to be used within the various
Containers you implement. You may modify Item however you like, so long as
Item's __init__() method takes the Item's size as an argument. Container
__init__() methods should not require any arguments.

Your code must pass the tests implemented in `test_warehouse.py`, which
covers the basic, required functionality described above. The tests can be run
by executing the respective test scripts (e.g. `python test_warehouse.py` from
the command line).

The bonus problems can be tested via `test_warehouse_bonus.py`, which applies
all the standard tests, plus one for each of the bonus features. It is
permissible to fail tests for any specific bonus feature you did not attempt
to implement.
