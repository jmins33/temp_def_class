# main.py dir에서 calculation.py 정의한 함수 불러오기
# -*- coding:utf-8 -*-

import calculation as cal
from arithmetic import plus
from arithmetic import subtract
from dataPreprocessing import processing
from dataPreprocessing import importData

a = 30
b = 40

def main():
    print("~~ 사칙 연산을 시작합니다 ~~ ")
    print('a+b = ', plus.plus(a,b))
    print('a+b = ', subtract.subtract(a,b))
    print("~~ 사칙 연산을 종료합니다 ~~ ")

## 데이터 전처리 시작
data = importData.readData()
processing.process_data(data)

if __name__ == '__main__':
    main()