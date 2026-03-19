###
def upset_probability(matchups):
    result = []
    
    for match in matchups:
        seed1 = match[1]
        seed2 = match[3]
        
        higher_seed = max(seed1, seed2)
        lower_seed = min(seed1, seed2)
        
        prob = lower_seed / (higher_seed + lower_seed)
        
        result.append(round(prob, 2))
    
    return result
