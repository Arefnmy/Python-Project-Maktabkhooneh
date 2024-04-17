from fetch import fetcher
from ml import ML

fetcher()
m = ML()
m.learn()
print(m.predict([['BMW', 0]]))
