###
def average_time(total, completed):
    # Split the time string into hours, minutes, seconds
    h, m, s = map(int, total.split(":"))
    
    # Convert everything to seconds
    total_seconds = h * 3600 + m * 60 + s
    
    # Calculate average and round to nearest second
    avg = round(total_seconds / completed)
    
    return avg
