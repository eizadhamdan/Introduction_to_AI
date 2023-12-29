from logic import *

rain = Symbol("rain")       # means it is raining
hagrid = Symbol("hagrid")       # Harry visited Hagrid
dumbledore = Symbol("dumbledore")       # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),         # if it isn't raining then harry visited hagrid
    Or(hagrid, dumbledore),                 # harry visited hagrid or dumbledore
    Not(And(hagrid, dumbledore)),           # but harry didn't visit both
    dumbledore                                          # harry visited dumbledore
)

print(knowledge.formula())
print(model_check(knowledge, rain))
