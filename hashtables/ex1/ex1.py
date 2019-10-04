#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# Returns a tupple of 2 weights that add up to limit 
def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    answer = None

    i=0
    for weight in weights:
        hash_table_insert(ht, weight, i)
        i+=1

    weightIndex=0
    for weight in weights:
        otherHalf = limit - weight
        otherHalfIndex = hash_table_retrieve(ht, otherHalf)
        if otherHalfIndex:
            if weight > otherHalf:
                answer = (weightIndex, otherHalfIndex)
                print(answer[0], answer[1])
                return answer
            else:
                answer = (otherHalfIndex, weightIndex)
                print(answer[0], answer[1])
                return answer
        weightIndex+=1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
