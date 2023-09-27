import numpy
import random

print("привеу! не буду тянуть у тебя квартира есть?(я чувствительна к регистру реестру я че знаю чтоле хихи~)")
house = input()
print("панятна, а рэп любиш?")
rap = input()
if house == "да":
    house = 1
elif house == "нет":
    house = 0
if rap == "да":
    rap = 1
elif rap == "нет":
    rap = 0


def activation(x):
    return 0 if x < 0.5 else 1


def go(house, rap, face):
    x = numpy.array([house, rap, face])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = numpy.array([w11, w12])
    weight2 = numpy.array([-1, 1])

    sumh = numpy.dot(weight1, x)
    # print("Значения сумм на нейронах скрытого слоя: " +str(sumh))

    outh = numpy.array([activation(x) for x in sumh])
    # print("Значения сумм на выходах нейронов скрытого слоя: " +str(outh))

    sume = numpy.dot(weight2, outh)
    y = activation(sume)
    # print("Выходное значение нейронной сети:" +str(y))

    return y


face = random.randint(0, 1)
if face == 1:
    print("ну красивы малый")
else:
    print("стремный чел")
res = go(house, rap, face)
if res == 1:
    print("ты прикольный")
else:
    print("иди маме расскажи какой ты сигма")
