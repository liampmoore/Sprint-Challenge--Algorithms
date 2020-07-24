#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  
    # The space complexity is O(1) since we always save a single value regardless of the size of the input.
    a = 0
    # This line begins a loop which should perform O(n^3) iterations. This is polynomial time complexity, really bad.
    while (a < n * n * n):
        # This line however allows us to skip iterations. We skip through the n^3 total loops in steps of n^2 iterations.
        # That means we can divide the total iterations by the number of iterations we skip. n^3/n^2 = n
        # Therefore we have O(n) speed complexity.
        a = a + n * n
```

```python
b)  
    # We save one variable here for the sum, and one variable below in the for loop, j. 
    # Two variables regardless of the size of inputs. That means we have constant space complexity, O(1)
    sum = 0
    # The outer loop will run n times. This gives us a speed complexity of O(n).
    for i in range(n):
        j = 1
        # The inner loop is set to have n iterations.
        while j < n:
            # However, we are again skipping through the total iterations of the inner loops.
            # We double the amount of iterations we are skip each time.
            # Since we are moving through the inputs faster and faster as we go, the speed complexity here is O(log n)
            j *= 2
            sum += 1

        # The outer loop will n times, and the inner loop will run O(log n) iterations for each outer loop iteration.
        # We can multiply outer times the inner for a total time complexity of O(n*log(n))
```


```python
c)  
    # The base amount of iterations of this recursive function can be measured by the number input bunnies,
    # since we are counting down from the value bunnies to zero.
    def bunnyEars(bunnies):
        # This base case tells us where we will end.
        if bunnies == 0:
            return 0
        # The value we put into the recursive call tells us the size of the steps we will take through the base number of iterations.
        # It seems we are counting down through bunnies in decrements of one, which means we complete n iterations in total.
        return 2 + bunnyEars(bunnies-1)
    # Since we are executing this function n times, the speed complexity will be O(n)
    # Since we are using recursion, we will be pushing each call to the call stack, building up the call stack to n total calls.
    # Therefore our space complexity is also O(n).
```

## Exercise II

Understand
    - Inputs:
    - n story building, each floor n has a value True or False for whether the egg will break.
    - Output:
    - Find floor f in the least guesses possible

    - We have to drop eggs from various floors to figure out the first floor f where they begin to break.
    - We want to drop the least eggs possible (make the least amount of guesses).

Plan   
    1. We can use some sort of search algorithm, probably binary search since it has log(n) guesses/operations.
    2. Determine the steps necessary to make a guess.
    3. Write psuedocode.

Execution
    Step 1: Make a guess at the middle index. If the value is True, meaning the egg breaks, then we know that the floor f is
    equal to or less than the guess. Otherwise f must be higher.
    Step 2: If the previous guess was True, make a guess at the middle value between the 0 index and the previous guess.
            If the previous guess was False, make a guess starting at the previous guess + 1, up until the previous maximum.
    Step 3: When the maximum equals the minumum range and the value is true, we have our value. When the minimum equals the maximum and the value is still false, somehow the eggs are magically surviving a drop from the top floor.

Review
    The runtime complexity of the above binary search algorithm I described is O(log n) since each time we make a guess we cut the amount of guesses in half.

