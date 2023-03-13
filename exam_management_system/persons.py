import quiz


class Person:
    def __init__(self):
        self.id = 0
        self.name = ''

    def add(self):
        self.id = input("Input ID ")
        self.name = input('Input Name')

    def print_person(self):
        print('Id : ' + self.id, 'Name : ' + self.name)


class Instructor(Person):
    def __init__(self):
        super()
        self.department = ''

    def add_instructor(self):
        print('Add Instructor ')
        self.department = input('Input Department ')
        self.add()

    def print(self):
        print('\t\t\t\tINSTRUCTOR INFORMATION')
        self.print_person()
        print('Department : ' + self.department)

    # iska koi kaam ni aya
    def quiz_operations(self):

        quizz = quiz.QuizList()

        while True:
            print('\n\t\t\t\tINSTRUCTOR')

            print('1) Add Quiz')
            print('2) Show Quiz')
            print('3) Remove Quiz')
            print('4) Exit')
            x = input('Select an option ')
            if x == '1':
                quizz.add()

            elif x == '2':
                quizz.show()

            elif x == '3':
                quizz.delete()

            elif x == '4':
                print('\t\t\t\tExiting...')
                break

            else:
                print('\t\t\t\tInvalid Input')
        return quizz


class Student(Person):
    def __init__(self):
        super()
        self.marks = {}

    def add_student(self):
        print('Add Student')
        self.add()

    def print_stu(self):
        print('\t\t\t\tSTUDENT INFORMATION')
        print("Name : " + self.name)
        print("Id : " + self.id)
        print('Marks')
        for i, j in self.marks.items():
            print('Course : ' + str(i), '\tMarks : ' + str(j))

