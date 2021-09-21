class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def teaching_assessment(self, course_name, lecturer, grade):
        if course_name in self.courses_in_progress and isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            if course_name in lecturer.lectur_grades:
                lecturer.lectur_grades[course_name] += [grade]
            else:
                lecturer.lectur_grades[course_name] = [grade]
        else:
            print(f'Лектор {lecturer.name} не преподает у студента {self.name}')
            return 'Ошибка'

    def average(self):
        if self.grades:
            res_list = []
            for value in self.grades.values():
                res_list += value
            average_rating = sum(res_list) / len(res_list)
        else:
            average_rating = 0
        return average_rating

    def __str__(self):
        if self.courses_in_progress:
            courses_progress = ', '.join(self.courses_in_progress)
        else:
            courses_progress = 'нет'
        if self.finished_courses:
            finish_courses = ', '.join(self.finished_courses)
        else:
            finish_courses = 'нет'
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average(), 2)}\nКурсы в процессе изучения: {courses_progress}\nЗавершенные курсы: {finish_courses}"
        return res

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.average() < other.average():
                res = f"Студент {self.name} {self.surname} в среднем хуже, чем студент {other.name} {other.surname}"
            elif self.average() > other.average():
                res = f"Студент {self.name} {self.surname} в среднем лучше, чем студент {other.name} {other.surname}"
            else:
                res = "Оба студента офигенные!"
        else:
            res = "Студента можно сравнить только со студентом"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectur_grades = {}

    def average(self):
        if self.lectur_grades:
            res_list = []
            for value in self.lectur_grades.values():
                res_list += value
            average_rating = sum(res_list) / len(res_list)
        else:
            average_rating = 0
        return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average(), 2)}"
        return res

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if self.average() < other.average():
                res = f"Лектор {self.name} {self.surname} хуже, чем лектор {other.name} {other.surname}"
            elif self.average() > other.average():
                res = f"Лектор {self.name} {self.surname} лучше, чем лектор {other.name} {other.surname}"
            else:
                res = "Оба лектора офигенные!"
        else:
            res = "Лектора можно сравнить только с лектором"
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print(f"Проверяющий {self.name} {self.surname} не может ставить оценки за курс {course}")
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


all_lecturers = []
all_students = []


def average_students_grades(course_name, students):
    grades = []
    course_flag = 1
    if all_students:
        for student in students:
            grades_list = student.grades.get(course_name)
            if grades_list:
                course_flag = 0
                for item in grades_list:
                    grades.append(item)
        if course_flag:
            return f"На курсе '{course_name}' нет ни одного студента"
        average_grade = sum(grades) / len(grades)
        return f"Средняя оценка за домашние задания по курсу '{course_name}': {average_grade}"
    else:
        return "Ни одного студента нет, университет пустой!"


def average_lectures_grades(course_name, lectures):
    grades = []
    course_flag = 1
    for lecture in lectures:
        grades_list = lecture.lectur_grades.get(course_name)
        if grades_list:
            course_flag = 0
            for item in grades_list:
                grades.append(item)
    if course_flag:
        return f"На курсе '{course_name}' никто не поставил оценок лектору"
    average_grade = sum(grades) / len(grades)
    return f"Средняя оценка за преподавание курса '{course_name}': {average_grade}"



student_1 = Student('Ипполит', 'Воробьянинов', 'м')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['JS']
student_1.finished_courses += ['C#']
student_2 = Student('отец', 'Федор', 'м')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['JS']
student_2.finished_courses += ['C#']
all_students.append(student_1)
all_students.append(student_2)

reviewer_1 = Reviewer('Авессалом', 'Изнуренков')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Никифор', 'Ляпис-Трубецкой')
reviewer_2.courses_attached += ['JS']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'JS', 10)
reviewer_1.rate_hw(student_2, 'Python', 20)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'JS', 20)

lectur_1 = Lecturer('Васисуалий', 'Лоханкин')
lectur_1.courses_attached += ['Python']
lectur_1.courses_attached += ['JS']
lectur_2 = Lecturer('Елена', 'Боур')
lectur_2.courses_attached += ['Python']
all_lecturers.append(lectur_1)
all_lecturers.append(lectur_2)

student_1.teaching_assessment('Python', lectur_1, 20)
student_1.teaching_assessment('Python', lectur_1, 20)
student_1.teaching_assessment('Python', lectur_1, 20)
student_1.teaching_assessment('JS', lectur_1, 30)
student_1.teaching_assessment('JS', lectur_1, 20)
student_1.teaching_assessment('Python', lectur_2, 20)
student_1.teaching_assessment('Python', lectur_2, 10)
student_1.teaching_assessment('JS', lectur_1, 20)

print("Студенты:")
print(student_1)
print(student_1.grades)
print('-' * 20)
print(student_2)
print(student_2.grades)
print('*' * 50)

print("Лекторы:")
print(lectur_1)
print('-' * 20)
print(lectur_2)
print('*' * 50)

print("Проверяющие:")
print(reviewer_1)
print('-' * 20)
print(reviewer_2)
print('*' * 50)

print(lectur_1 == lectur_2)
print(student_1 == student_2)
print('*' * 50)

print(average_students_grades('Python', all_students))
print(average_students_grades('C#', all_students))
print('-' * 20)
print(average_lectures_grades('Python', all_lecturers))
