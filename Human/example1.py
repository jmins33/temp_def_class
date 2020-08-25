# -*- coding:utf-8 -*-

class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f'{self.name}의 나이는 {self.age}이다.'

    def say(self, content):
        return f'{self.name}이 {content}에 대해 말하고 있다.'

    def race(self, race):
        return f'{self.name}의 인종은 {race}이다.'

class asian(human):
    pass

class european(human):
    pass

class african(human):
    pass

if __name__== '__main__':
    jessica = asian('jessica', 27)
    jane = european('jane', 25)
    kile = african('kile',22)

    print(jessica.race('yellow race'))
    print(jane.race('white race'))
    print(kile.race('black race'))