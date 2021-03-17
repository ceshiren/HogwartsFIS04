"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/16 9:36 下午'
"""
import copy

nums = [1,2,3]
nums1 = nums

nums1 = [1,2,3,4]
print(id(nums))
print(id(nums1))

# 浅拷贝
num2 = nums.copy()
# words1 是words的浅拷贝
words = ['hello','hogwarts',['hurry','tom']]
# words1 = words.copy()
#
# words[0] = "哈啰"
# print(words1)
# print(words)
#
# words[2][0]="赫敏"
# print(words)
# print(words1)

# 浅拷贝， 就是只拷贝第一层
# 深拷贝， 完全拷贝出一个新的内容，
words2 = copy.deepcopy(words)
words[0] = "哈啰"
words[2][0]="赫敏"
print(words2)
print(words)