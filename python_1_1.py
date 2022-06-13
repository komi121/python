import random as rd


def premium():
    return rd.randint(3000, 100000)


def bid():
    return rd.choice([1000, 1500, 2000, 2500])


def time():
    return rd.randint(150, 200)
