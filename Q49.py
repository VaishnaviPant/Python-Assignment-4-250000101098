def total_marks(marks):
    return sum(marks)

def percentage(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def result(marks):
    if all(mark >= 35 for mark in marks):
        return "Pass"
    return "Fail"