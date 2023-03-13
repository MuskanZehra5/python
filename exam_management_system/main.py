import persons
import quiz

if __name__ == '__main__':
    inst = persons.Instructor()
    inst.add_instructor()

    # make student class list/array
    students = []

    # make quiz class list/array
    quiz_list = []

    print('\t\t\tEXAM MANAGEMENT SYSTEM\t\t\t')

    while True:
        print('\nSelect any option')
        print('1) Instructor')
        print('2) Student')
        print('3) Exit')
        choice = input()

        #  INSTRUCTOR

        if choice == '1':
            print('\t\t\t\tLOGIN')
            id_ = input('Enter Instructor id ')
            if inst.id == id_:
                print('\t\t\t\tLogin Successful')
                while True:
                    print('\nSelect any option')
                    print('1) Add Student')
                    print('2) Add Quiz')
                    print('3) Show Students')
                    print('4) Show Quizzes')
                    print('5) Exit')
                    opt = input()

                    if opt == '1':

                        stu = persons.Student()
                        stu.add_student()
                        students.append(stu)

                    elif opt == '2':
                        print('\t\t\t\tAdd Quiz')
                        inst_quiz = quiz.Quiz()
                        inst_quiz.add_quiz()
                        quiz_list.append(inst_quiz)

                    elif opt == '3':
                        for i in students:
                            i.print_stu()

                    elif opt == '4':
                        for i in quiz_list:
                            i.print_all()

                    elif opt == '5':
                        break

                    else:
                        print('\t\t\t\tInvalid Input')

            else:
                print('\t\t\t\tInvalid Credential')

        # STUDENT
        elif choice == '2':
            print('\t\t\t\tLOGIN')
            id_st = input('Enter Student id : ')

            for st in students:
                print(st.name)
                if id_st == st.id:
                    print('\t\t\t\tLogin successful')

                    while True:
                        print('\nSelect any option')
                        print('1) Take Quiz')
                        print('2) Show Result')
                        print('3) Exit')
                        opt = input()

                        if opt == '1':

                            num = 1

                            for i in quiz_list:
                                print(str(num) + ') ' + i.course_name)
                                num += 1

                            inp = input('Enter course name from the list')
                            score = 0
                            for i in quiz_list:
                                if inp.lower() == i.course_name.lower():
                                    for key, value in i.questions.items():
                                        print(key)
                                        x = value[:-1]
                                        for j in range(len(x)):
                                            print(str(j + 1) + ' ) ' + x[j])

                                        ans = input("Enter your answer ").lower()

                                        actual_ans_list = value[-1]
                                        actual_ans = actual_ans_list[:-10]
                                        print('Correct ANS ' + actual_ans)
                                        if ans == actual_ans.lower():
                                            score += 5

                            st.marks[i.course_name] = score

                        elif opt == '2':
                            st.print_stu()

                        elif opt == '3':
                            break

                        else:
                            print('Invalid Input')

                else:

                    continue

        elif choice == '3':
            print('\t\t\t\t...Exiting...')
            break

        else:
            print('\t\t\t\tInvalid Input')
