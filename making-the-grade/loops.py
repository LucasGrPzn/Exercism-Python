"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_list = []
    for item in student_scores:
        new_item = round(item)
        new_list.append(new_item)

    return new_list


def count_failed_students(student_scores: list) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    passed_students = 0
    for grade in student_scores:
        if grade <= 40:
            passed_students += 1
    
    return passed_students


def above_threshold(student_scores: list, threshold: int) -> list:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for item in student_scores:
        if item >= threshold:
            best_scores.append(item)

    return best_scores


def letter_grades(highest: int) -> list:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    lower_threshold_scores = []
    range_value = (highest - 40) // 4
    start_value = 41

    for loop in range(4):
        if loop == 0:
            lower_threshold_scores.append(41)
            continue
        start_value += range_value
        
        lower_threshold_scores.append(round(start_value))

    return lower_threshold_scores


def student_ranking(student_scores: list, student_names: list):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    new_list = []
    
    for position, name in enumerate(student_names):
        item_formated = f"{position + 1}. {name}: {student_scores[position]}"
        new_list.append(item_formated)

    return new_list


def perfect_score(student_info: list):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if student[1] == 100:
            return student
        
    return []
