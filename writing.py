filename = 'data.txt'


with open(filename, 'r') as f:
    headers = f.readline().strip().split(',')
    
    # Lege dict
    d = {h:[] for h in headers}
    
    # Per regel
    for line in f.readlines():
        # Lees de values
        values = line.strip().split(',')

        # Per header-value paar:
        # voeg de value toe aan de lijst van header in de dict
        for h,v in zip(headers,values):
            d[h].append(v)


print(d)