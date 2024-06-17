def update_student_locations(students):
    updated_students = []
    for student in students:
        if 'location' not in student:
            updated_student = student.copy()
            updated_student['location'] = 'remote'
            updated_students.append(updated_student)
        else:
            updated_students.append(student.copy())
    return updated_students