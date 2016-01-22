from reader import init_train, build_cuisines, recipe
from predictor import slow_predictor
import time

# Sets up the training and testing lists
start_time = time.time()
tr = init_train("train.json", 'train')
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
te = init_train("test.json", 'test')
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
c = build_cuisines(tr)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
slow_predictor(te, c)
print("--- %s seconds ---" % (time.time() - start_time))


