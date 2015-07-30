cohort1 = {
    'Avery': [63, 62, 41, 66, 84, 82, 73, 89, 69, 75],
    'Blake': [79, 97, 78, 78, 74, 69, 80, 100, 74, 70],
    'Casey': [93, 97, 99, 95, 98, 91, 96, 99, 100, 88],
    'Dakota': [71, 65, 72, 65, 24, 100, 84, 71, 59, 50],
    'Elliot': [84, 73, 90, 72, 69, 93, 61, 65, 81, 98],
    'Fox': [80, 91, 90, 80, 83, 73, 84, 89, 84, 84],
    'Gale': [41, 7, 64, 60, 78, 48, 73, 50, 69, 89]
}
#student_means: Return a new dictionary, with students as keys and their mean test score

#as the value. Then add an optional argument, drop_lowest. When true,
#drop each student's lowest score before calculating their mean.
#student_grades: Return a new dictionary, with students as keys and
#their grade as the value. Add the optional drop_lowest argument like in student_means.
# A is 90+, B is 80-89, C is 70-79, D is 60-69, F is below 60.
#all_scores: Return a list of all the students' test scores.
#class_mean: Return a float, the mean score for the entire class across all tests.
#score_histogram: Return a new dictionary. Each key is a letter grade (A, B, C, D, F). The value for each is all the students' test scores that fall within that grade range.
def mean(nums, drop_lowest =False):
    if drop_lowest:
        nums = sorted(nums[1:])
    return sum(nums) / len(nums)

def grade_means(cohort1, drop_lowest = False):
    return {student: mean(cohort1[student], drop_lowest=False) for student in cohort1 for student
         in cohort1}
print(grade_means(cohort1,drop_lowest = False))
