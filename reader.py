import os, re, json, sys

class recipe(object):

   def __init__(self, r_id, r_name, r_ingr):
      self.idf = r_id
      self.name = r_name
      self.ingr = r_ingr

# reads the recipies and creates training and testing sets
def init_train(fn, indicator):
   train = []
   test = [] 

   try:
       f = open(fn, 'rb')
   except IOError:
      print "Could not read file:", fn
      sys.exit()

   with f:
      data = json.loads(f.read())
  
   if indicator is 'train':
      for d in data:
         train.append(recipe(d['id'], d['cuisine'], d['ingredients']))
      return train 
   
   if indicator is 'test':
      for d in data:
         test.append(recipe(d['id'], None, d['ingredients']))
      return test

# Compiles all the ingredients of each cuisine
def build_cuisines(recipies):
   cuisines = {}
   for r in recipies:
      if r.name not in cuisines:
         cuisines[r.name] = r.ingr
      else:
         cuisines[r.name].extend(r.ingr)

# Sets up the training and testing lists
tr = init_train("train.json", 'train')
te = init_train("test.json", 'test')
build_cuisines(tr)

