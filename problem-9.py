def special_pythagorean_triplet(target):

    for a in range(1, target):
        for b in range(a, target):
            c = (a ** 2 + b ** 2) ** 0.5
            
            if a + b + c == 1000:
                return int(a * b * c)

print(special_pythagorean_triplet(1000))