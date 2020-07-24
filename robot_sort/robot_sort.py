class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # First we will swap None for the first item in the array.
        # We are now holding the first item in the array.
        # We will now move right and keep checking if the item in the current position is
        # less than the item we are holding. If so we will pick up the smaller item.
        # We'll keep comparing like this until we reach the end, then go all the way back to the left
        # and swap the smallest item in that run for our None value.
        # Then we'll swap our None value for the item in the next position.
        # We now know that everything to the left of the None value is sorted.
        # We will repeat this process until we find that our None value reaches the end of the array, meaning the array is fully sorted.
        
        # Swap the held None for the first item, leaving the None in the first position.
        self.swap_item()
        # We will loop until we hit the return statement.
        while True:
            # If you can move right,
            if self.can_move_right():
                # move right. 
                self.move_right()
                # If the item in this position is lower than the held item, swap the held item for said item.
                if self.compare_item() == 1:
                    self.swap_item()
            # If you can't move right anymore,
            else:
                # begin a loop to go back to the None value to add the currently held value to end of the sorted portion of the array.
                while True:
                    # Move left.
                    self.move_left()
                    # If compare_item returns None then you have reached the sorted marker.
                    if self.compare_item() == None:
                        # Swap the held item for the sorted marker.
                        self.swap_item()
                        # Move right.
                        self.move_right()
                        # If you are at the end, then the list is completely sorted return.
                        if not self.can_move_right():
                            return
                        # Else if you aren't at the end of the array, 
                        else:
                            # put down the sorted marker None value and pick up the value in that position,
                            self.swap_item()
                            # and break back to the loop to begin moving right and comparing values again.
                            break



"""
Understand:

Inputs:
- List of values
Output:
- The same list of values sorted

Constraints:
- Must use predefined methods and attributes
- May use iterators, while, for, break, continue, and logical operators, and comparisons
- No variables
- Can not access class instance variables directly, must use methods and attributes
- No python libraries or methods
- You may define robot methods as long as they are constructed from other robot methods and use the rules

The Robots Methods:
The robot starts at the beginning of the list and has a true or false light.
It starts holding None as it's item.

Can move left and can move right: Determines if the robot is at the beginning or end of the list with booleans.
Move: Increments the time counter and attempts to move, returning true if successful

Swap item: Increments time and swaps held item with item at current position. If you are holding none this will make the item in the current position None.
Compare: Will return 1 if held item is greater, -1 if less, 0 if equal, None if any item is none.

Light: Sets light on or sets light off, or checks if light is on or off.


Plan
1. Figure out which type of sorting algorithm would be easiest and fastest to implement with this robot.
2. Match the steps in the algorithm to possible robot methods.
3. Write the pseudocode
4. Write the code.

Execute
    1. Which algorithm?
    - Seems like it must be iterative sorting.
    - Also must be in place sorting since we are swapping items and have no variables.
    - We don't have access to an index so we need an algorithm that sorts without the use of one.
    - An algorithm with very limited senses that works in place and only focuses on what is directly in front of it.
    - Can use a true or false boolean.
    - Might be able to use the None value as a sorted index point for in place selection sort.

    2. Match algorithm steps to robot methods
    - Swap the first item, leaving None in index 0.
    - Move right, compare, if lower, swap, until you reach the end if you reach the end start this inner loop:
        - Move left until you reach None and swap, then move right and if at the end return, otherwise swap None for the next item, then repeat outer loop.
    3. Write pseudocode.
    - Done inline above.
    4. Write code
    - Done.

Review
    1. Performance
    - This is an implementation of selection sort, so it's speed complexity is O(n^2) polynomial coming in at 0.077 seconds for the tests provided. It is in place however, so it's space complexity is O(1) constant.
    2. Readability
    - Could definitely put in some better comments that tie it in better to selection sort.
    - Doing that now.
    3. Edge Cases
    - One edge case might be if the array is empty or of one value. You could begin the function by checking if you can move left and right and if you can't go either way you return the already sorted array.
    
    Conclusion:
    It's a very interesting problem to implement sorting algorithms like this. Using a robot like this with just one bit of memory might be very similar to working on some type of system with very very limited memory and very few helper functions or modern libraries, where O(1) space might even be required.

"""


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)