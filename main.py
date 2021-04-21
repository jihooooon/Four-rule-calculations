from calc.plus_model import Plus
from calc.minus_model import Minus
from calc.multiply_model import Multiply
from calc.divide_model import Divide
import random
import numpy as np
from calc.get_data import GetData

def mean_squared_error(t_val, p_val):
    return np.square(np.subtract(t_val, p_val)).mean()

calc_sign = "+"

num_epochs = 100
all_scores = []

model = Plus()
model = model.build_model()
#model.summary()

for _ in range(num_epochs):
    customData = GetData(calc_sign)
    x, y = customData.get_data()
    x = x.reshape(100, 2, 1)

    model.fit(x, y, epochs=1, batch_size=1, verbose=2)

print("Train Fin!")

testData = GetData(calc_sign)
test_data, test_label = testData.get_data()
test_data = test_data.reshape(100,2,1)

res = model.predict(test_data)

exp = [testData.invert(x) for x in test_label]
pred = [testData.invert(x) for x in res[:,0]]

from math import sqrt
rmse = sqrt(mean_squared_error(exp, pred))
print("RMSE :", rmse)

err_sum = 0
for i in range(len(exp)):
    err = exp[i] - pred[i]
    print("Real : {}, predicted : {}, err={}".format(exp[i], pred[i], (err)))
    err_sum += err
print("aver Err : {}".format(err_sum/len(exp)))
    

dic = {"+":"plus", "-":"minus", "*":"multiply", "/":"divide"}
model.save(dic[calc_sign]+'_model.h5')

