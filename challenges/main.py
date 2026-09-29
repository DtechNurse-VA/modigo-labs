def count_unique_visitors(visitors):
    # TODO: convert `viitors` to a set to remove duplicates, then return its length
    
    visitord = set(visitors)
    #visitor.append(visitor)
    return len(visitord)
print(count_unique_visitors(['Ada', 'Bola', 'Ada']))