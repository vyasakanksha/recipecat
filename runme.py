from reader import init_train, build_cuisines, recipe
from predictor import slow_predictor
from visualizer import setup_graph, display
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

#start_time = time.time()
#slow_predictor(te, c)

#for t in te:
#   print t.idf, t.name
#print("--- %s seconds ---" % (time.time() - start_time))

data_lst = []
for i, k in c.items():
   ntrace = setup_graph(k, i)
   data_lst.append(ntrace)

display(data_lst)
