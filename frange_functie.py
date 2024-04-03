def frange(start, stop, step=1.0, endpoint=False):
    numbers = []
    while True:
        numbers.append(start)

        start += step # start = start + step

        if start > stop and endpoint or start >= stop and not endpoint:
            break
        
        # Zelfde als hiervoor alleen dan in leesbaardere regels
        if endpoint:
            if start > stop:
                break
        else:
            if start >= stop:
                break
    
    return numbers

print(frange(1, 5, 0.5, True))