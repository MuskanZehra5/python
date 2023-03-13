class Quiz:
    def __init__(self):
        self.course_name = ''
        self.total_questions = 0
        self.questions = {}

    def add_quiz(self):
        self.course_name = input('Course Name')
        x = int(input('Total Questions'))
        self.total_questions += x

        # inputs from the user

        for i in range(0, x):
            ques = input('Enter question number ' + str(i + 1) + ' : ')
            option1 = input('Option 1')
            option2 = input('Option 2')
            option3 = input('Option 3')
            solution = input('Solution') + '= solution'

            options_list = [option1, option2, option3, solution]

            self.questions[ques] = options_list

    def print_all(self):
        print('\n\t\t\t\tCourse : ' + self.course_name)
        for i, j in self.questions.items():
            print('\n')
            print("question : ", i)
            print('options : ', j)

    def delete(self):
        x = int(input('input the id of question you want to delete'))

        if x < self.total_questions:
            self.questions.pop(x)
            self.total_questions -= 1

        else:
            print('\t\t\t\tinvalid number')
