# https://www.chegg.com/homework-help/questions-and-answers/question-1-1-pts-true-false-apple-added-twice-set-added-set-b-set-set-b-would-considered-d-q35338479
# https://www.chegg.com/homework-help/questions-and-answers/login-new-account-feature-working-properly-wanted-know-fix-every-time-try-login-create-acc-q16775903
# https://www.chegg.com/homework-help/questions-and-answers/school-login-user-name--password--role-teacher-b-parent-c-student-d-foradministartor-quest-q437840


def question_id(url):
    ID = ""
    i = len(url)-1
    while i > 0:
        if url[i] != "q":
            ID = url[i] + ID
        else:
            return "q" + ID
        i -= 1