import time

def slow_predictor(test, cuisines):
   for t in test:
      counts = {}
      for i, k in cuisines.items():
         c = len(set(k) & set(t.ingr))
         if len(t.ingr) - c is 0:
            t.name = i
         else: 
            counts[i] = len(t.ingr) - c

      if t.name is None:
         t.name = min(counts.items(), key=lambda x: x[1])[0]
            
