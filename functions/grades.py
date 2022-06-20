
def grades(grade):
    final_grade = ''
    if 2 <= grade < 3:
        final_grade = "Fail"
    elif 3 <= grade < 3.5:
        final_grade = "Poor"
    elif 3.5 <= grade < 4.5:
        final_grade = "Good"
    elif 4.5 <= grade < 5.5:
        final_grade = "Very Good"
    elif 5.5 <= grade <= 6:
        final_grade = "Excellent"

    return final_grade


grade_score = float(input())

grade_result = grades(grade_score)
print(grade_result)
