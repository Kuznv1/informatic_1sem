N = 42
NO = N
prime_dividers = []
for i in range(2,N):
    t = 0
    if N % i > 0:
        continue
    for j in prime_dividers:
        if i % j == 0:
            t = 1
    if t == 1:
        continue
    prime_dividers.append(i)



# dividers_power = [0] * len(prime_dividers)
# for i in range(len(prime_dividers)):
#     while N % prime_dividers[i] == 0:
#         N //= prime_dividers[i]
#         dividers_power[i] += 1

# print(prime_dividers)
# print(dividers_power)

power_dict = {number: 0 for number in prime_dividers}
for number in prime_dividers:
    while N % number == 0:
        N //= number
        power_dict[number] += 1

decomposition = ""
for number in prime_dividers:
    decomposition += str(number) + '^' + \
        str(power_dict[number])
    if number != prime_dividers[-1]:
        decomposition += ' * '

print(f"{NO} = " + decomposition)
