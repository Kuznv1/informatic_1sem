n, m = map(int, input().split( ))
People = list(map(int, input().split()))

To = [0 for i in range(m)]

def time(People, Checkout):
    for person in People:
        free_checkout = min(Checkout)
        Checkout[Checkout.index(free_checkout)] += person
    time = max(Checkout)
    return time
#print(To)
print(time(People, To))

    
