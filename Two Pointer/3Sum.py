class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3Sum is a tough problem to understand how to approach at first.
        # However, after learning how to solve similar problems, the solution
        # becomes easier to understand. Notably after doing 2Sum sorted,
        # we realize we can approach 3Sum in a similar manner (to save space instead of using
        # a hashmap or dictionary). 
        
        # This time, we need a 3rd number to be fixed because 
        # we are summing three numbers instead of two. 
        # Again, remember first we have to sort the array to use this approach
        # We can use a for loop to keep track of our third number
        # and have it iterate through every element in the array except
        # the last two. Why not check the last two? We have our left
        # and right pointers to take care of that! We also need to check
        # for duplicate triplets. In order to do this we have to ensure
        # we are not setting our three pointers equal to similar elements.
        # this means keeping our left pointer in front of the for loop pointer
        # and also making sure none of our pointers run into a duplicate on 
        # the next iteration. We can achieve this using a while loop
        # (see comments) inside the code.

        # Aside from this additional logic, the inner workings of our code
        # work just like from the 2sum sorted array problem. If our total
        # is less than 0, we know we need to move our left pointer up.
        # If it is greater than 0, we know we need to move our right pointer up.
        # We do this while the left pointer is less than the right pointer, this is 
        # how we know we are not over-checking and our solution is still valid.
        # If our total is 0, we know we can add our set of solutions to our array
        # which should be returned. Now we still have to continue checking the rest of 
        # the array, so we should have a while loop which moves the left pointer up,
        # making sure we are not checking the same element again. The right pointer will
        # be taken care of automatically by our code

        toReturn = []
        nums.sort()

        for i in range(len(nums) - 2):
            # slight optimization - we know if our leftmost element is greater
            # than 0 there is no chance we can solve the problem anymore
            if nums[i] > 0:
                break
            
            # skipping duplicates
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # simple two sum logic
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # adjusting our pointers necessarily...
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    toReturn.append([nums[i], nums[left], nums[right]])

                    # we are done with the left and right and need to update them
                    left += 1
                    right -= 1
                    
                    # make sure we are not checking left pointers twice
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return toReturn
