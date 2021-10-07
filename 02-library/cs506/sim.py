def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

import math

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    intersect = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersect
    return float(intersect) / union

def cosine_sim(x, y):
    # Dot and norm
    dot = sum(a*b for a, b in zip(x, y))
    norm_x = sum(a*a for a in x) ** 0.5
    norm_y = sum(b*b for b in y) ** 0.5

    # Cosine similarity
    if (norm_x*norm_y)==0:
        return "Division by 0"
    else: 
        cos_sim = dot / (norm_x*norm_y) 
    
    return cos_sim

# Feel free to add more
