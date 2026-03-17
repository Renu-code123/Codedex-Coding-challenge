##
def lucky_river(river, hours):
    n = len(river)
    result = ['💧'] * n
    
    for i in range(n):
        if river[i] == '☘️':
            for j in range(i, min(i + hours + 1, n)):
                result[j] = '☘️'
    
    return result
  
