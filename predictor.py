import time
from sklearn import datasets, svm, metrics
import numpy as np


# Checks to see how many ingredients in the recipe match the 
# ingredients in a particular cuisine. If the current recipe
# is a proper subset of any cuisine, we have a winner. If not, 
# we go with the cuisine that has the maximum common ingredients
def slow_predictor(test, cuisines):
   output = []
   for t in test:
      counts = {}
      for i, v in cuisines.items():
         c = len(set(v) & set(t.ingr))
         if len(t.ingr) - c is 0:
            t.name = i
         else: 
            counts[i] = len(t.ingr) - c

      if t.name is None:
         t.name = min(counts.items(), key=lambda x: x[1])[0]
      output.append([t.idf, t.name]) 
   return output

# We convert the recipies of the training set into a binary matrix and
# train a SVM on that matrix with the cuisines as lables. Then we 
# use the SVM to predict the cuisines from the testing set. 

#Currently this is broken :(
def predictor(test, train, ingredients):
   output = []
   sample = np.zeros((len(train),len(ingredients)))
   names = [None] * len(train)

   for t in range(len(train)):
       names[t] = train[t].name
       for i in train[t].ingr:
           sample[t][ingredients.index(i)] = 1
   
   classifier = svm.SVC(gamma=0.001)
  
   # These keep crashing :'( 

   #classifier.fit(sample, names)
   #predicted = classifier.predict(data_test)
   for t in range(len(test)):
       output.append([test[t].idf, predicted[t]]) 
   return output


