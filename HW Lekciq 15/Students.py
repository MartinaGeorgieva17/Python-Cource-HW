class Student: 
    def __init__(self, name, student_id):
        self.name = name 
        self.student_id = student_id
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
        

    def remove_course(self, course_name): 
        if course_name in self.courses:
            self.courses.remove(course_name)
        else:
            print (f'{course_name} is not in the list of courses')

    def list_courses(self):
        print (f'Courses:', ", ".join(self.courses))



student1 = Student("Alice", 12345)
student1.add_course("Math")
student1.add_course("History")
student1.list_courses()