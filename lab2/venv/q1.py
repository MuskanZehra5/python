def chicken_count(num):
    if num >= 10:
        return str("many")
    else:
        return num


print("Number of Chickens : {}".format(chicken_count(5)))
print("Number of Chickens : {}".format(chicken_count(23)))
