# Написать генератор который будет возвращать последовательные целочисленные значения с возможностью задать начальное
# значение(не меньше единици), по умолчанию 1.
import itertools


def gen(start=None, stop=10):
    start = start if start and start > 1 else 1
    while start < stop:
        yield start
        start += 1

g = gen()
for _ in range(10):
    try:
        print(g.__next__())
    except StopIteration:
        print('finish')


# Создать класс коллекцию которая будет в себе хранить список пользователей(классы которые писали для мужчин и женщин)
# При добавлении присваивать уникальный айдентификатор полученный с помощью генератора, идетификатор можно сделать
# частью класса описывающего человека.


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.humans = []

    def __str__(self):
        return "My name is %s, I am %s years old, my sex is %s" % (self.name, self.age, self.sex)


class Women(Human):

    def __init__(self, name, age):
        super().__init__(name, age, 'female')


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, 'male')


class HumanCollection:
    def __init__(self):
        self.humans = []
        self.human_id = 0

    def __str__(self):
        return " %s" % self.humans

    def generator_id(self):
        while True:
            self.human_id += 1
            yield self.human_id

    def append_human(self, human):
        id_ = self.generator_id()
        self.humans.append((id_.__next__(), human))
        return self.humans

    def print_older_human(self, age=None):
        age = age if age else 21
        older_humans = list(itertools.filterfalse(lambda human: human[1].age < age, self.humans))
        for human in older_humans:
            print("id %s , human %s" % (human[0], human[1]))

    def print_smaller_human(self, age=None):
        age = age if age else 21
        smaller_humans = list(itertools.filterfalse(lambda human: human[1].age > age, self.humans))
        for human in smaller_humans:
            print("id %s , human %s" % (human[0], human[1]))

    def print_male(self):
        male_humans = list(itertools.filterfalse(lambda human: human[1].sex == 'female', self.humans))
        for human in male_humans:
            print("id %s , human %s" % (human[0], human[1]))

    def print_female(self):
        female_humans = list(itertools.filterfalse(lambda human: human[1].sex == 'male', self.humans))
        for human in female_humans:
            print("id %s , human %s" % (human[0], human[1]))


Mary = Women('Mary', 20)
Sara = Women('Sara', 15)
Ann = Women('Ann', 22)
Jon = Man('Jon', 27)
Ben = Man('Ben', 19)
Ron = Man('Ron', 22)
humans = HumanCollection()
humans.append_human(Mary)
humans.append_human(Sara)
humans.append_human(Ann)
humans.append_human(Jon)
humans.append_human(Ben)
humans.append_human(Ron)

humans.print_male()
print("*"*10, "возвращает только женщин")
humans.print_female()
print("*"*10, " возвращает только тех кто старше заданного возраста, по умолчанию 21")
humans.print_older_human()
print("*"*10, " возвращает только тех кто младше заданного возраста, по умолчанию 21")
humans.print_smaller_human()





