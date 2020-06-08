def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)
    

bestStudents = [3, 5]
scholarships = [3, 5, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7] 

print(correctScholarships(bestStudents, scholarships, allStudents))