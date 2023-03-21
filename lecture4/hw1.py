"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline

    def is_deadline_passed(self):
        return self.deadline < 1


class Result:
    def __init__(self, author, solution, homework):
        self.author = author
        self.solution = solution
        self.homework = homework
        self.checked = False

    def __len__(self):
        return len(self.solution)


class Student:
    def __init__(self, second_name, first_name):
        self.second_name = second_name
        self.first_name = first_name

    def do_homework(self, homework: Homework, solution):
        if homework.deadline < 0:
            raise DeadlineError("You are late")
        else:
            return Result(self, solution, homework)


class Teacher:
    homework_done = {}

    def __init__(self, second_name, first_name):
        self.second_name = second_name
        self.first_name = first_name

    def check_homework(self, result: Result):
        if len(result) > 5:
            if not result.checked:
                self.__class__.homework_done[result.homework].append(result)
                result.checked = True
            return True
        return False

    @classmethod
    def create_homework(cls, title, deadline):
        homework = Homework(title, deadline)
        cls.homework_done[homework] = []
        return homework

    @classmethod
    def reset_results(cls):
        cls.homework_done.clear()


class DeadlineError(Exception):
    pass
