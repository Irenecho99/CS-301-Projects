# project: p4
# submitter: kcho36
# partner: djang26

import pandas as pd

def predict1(glucose, bmi, age):
    if glucose <= 127.5:
        return False
    else:
        return True

#q1
predict1(glucose=128, bmi=25, age=40)

#q2
predict1(glucose=127, bmi=25, age=80)

#q3
predict1(glucose=127.5, bmi=25, age=20)


def predict2(glucose, bmi, age):
    if glucose >= 127.5:
        if bmi <= 29.95:
            return False
        else:
            return True
    else:
        return False

#q4
predict2(glucose=128, bmi=25, age=40)

#q5
predict2(glucose=128, bmi=30, age=40)

#q6
predict2(glucose=127.6, bmi=29.95, age=40)

#q7
predict2(glucose=120, bmi=25, age=20)

#q8
predict2(glucose=127.5, bmi=25, age=20)


def predict3 (glucose = None, bmi = None, age = None):
    if glucose == None:
        glucose = column_avg("glucose")
    if bmi == None:
        bmi = column_avg("bmi")
    if age == None:
        age = column_avg("age")
    if glucose <= 127.5:
        if age <= 28.5:
            if bmi <= 45.4:
                return False
            else:
                return True
        else:
            return False
    else:
        if bmi <= 29.95:
            if glucose <= 145.5:
                return False 
            else:
                return True
        return True
    return True

#q9
predict3(glucose=130, bmi=29.4, age=50)

#q10
predict3(glucose=148, bmi=28.15, age=25)

#q11
predict3(glucose=148, bmi=28.15, age=26.5)

#q12
predict3(glucose=130, bmi=30, age=28)

#q13
predict3(glucose=120, bmi=46, age=50)

#q14
predict3(glucose=120, bmi=46, age=20)

#q15
predict3(glucose=120, bmi=26, age=20)

def column_avg(column_name):
        return column_sum(column_name)/row_count()
    
dataset = pd.read_csv("diabetes.csv")


def column_sum(column_name):
    return dataset[column_name].sum()


def row_count():
    return len(dataset)

#q16: what is the average glucose level?
column_avg("glucose")

#q17: what is the average glucose level?
column_avg("insulin")



#q18
predict3(bmi=26, age=20)

#q19
predict3(glucose=150)

#q20
predict3(glucose=150, bmi=20)