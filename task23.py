__author__ = 'anastasia'

nums = [1,2,3,3,3,4]
'''def remove(nums):
  for i in nums:
    if nums[i] == nums[item+1]:
      return True
    return nums
  print (remove(nums))'''

def remove_adjacent(nums):
  i = 1
  while i < len(nums):
    if nums[i] == nums[i-1]:
      nums.pop(i)
      i -= 1
    i += 1
  return nums