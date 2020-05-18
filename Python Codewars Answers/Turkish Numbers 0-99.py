def get_turkish_number(num):
    turk_dict, tens = { 0 : "sıfır",  1 : "bir", 2 : "iki", 3 : "üç", 4 : "dört", 5 : "beş", 6 : "altı", 7 : "yedi", 8 : "sekiz", 9 : "dokuz", 10 : "on", 20 : "yirmi", 30 : "otuz", 40 : "kırk", 50 : "elli", 60 : "altmış", 70 : "yetmiş", 80 : "seksen", 90 : "doksan"}, [10, 20, 30, 40, 50, 60, 70, 80, 90]
    if not num in tens: num = [i for i in str(num)]
    else: num = [str(num)] 
    nums = len(num)
    if nums > 1: num[0], num[1] = int(num[0]) * 10, int(num[1])
    else: num[0] = int(num[0])
    if nums > 1: return str(turk_dict[num[0]])+ " " + str(turk_dict[num[1]])
    else: return str(turk_dict[num[0]])
