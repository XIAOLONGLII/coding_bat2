"""

Author: Shay
Date: June 7, 2020


Given an int array length 2, return True if it contains a 2 or a 3.

"""

def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
  if nums[1] == 2 or nums[1] == 3:
    return True
  return False  

