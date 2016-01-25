from reader import init_data, build_cuisines, recipe
from predictor import slow_predictor, predictor
from visualizer import setup_graph, display
import time, csv

# Sets up the training and testing lists
start_time = time.time()
training_set = init_data("train.json", 'train')
testing_set = init_data("test.json", 'test')
print("Reading Input in --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
c, i = build_cuisines(training_set)
print("Building cuisine and ingredient lists in --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
solution = slow_predictor(testing_set, c)
#solution = predictor(tesing_set, training_set, i)
print("Predicting cuisines for the test set in --- %s seconds ---" % (time.time() - start_time))

with open('submission.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(solution)

start_time = time.time()
data_lst = []
for i, k in c.items():
   ntrace = setup_graph(k, i)
   data_lst.append(ntrace)

display(data_lst)
print("Visualizing cuisines for the test set in --- %s seconds ---" % (time.time() - start_time))
