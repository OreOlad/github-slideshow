def most_money(students):
    a = list()
    for name in students:
        f5ves, t3ns, twent20s = name.fives * 5, name.tens * 10, name.twenties * 20
        a.append(sum([f5ves, t3ns, twent20s]))
    if len(students) == 1: return students[0].name
    return students[a.index(max(a))].name if len(students) > 1 and max(a) != min(a) else "all"
    
