"""Tests the cosine similarity function

    Author: Josh"""

from AndysSkeletonProgram.cosineSimilarity import cosineSimilarity

testQ = [1,2,3]
testC = [[1,2,3],[-1,-2,-3],[-1,-2,3]]
cosineMatrix = cosineSimilarity(testQ, testC)
print(cosineMatrix)






