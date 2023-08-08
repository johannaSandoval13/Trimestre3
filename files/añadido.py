from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
counters.update({str(digit): 0 for digit in range(10)})
counters.update({'special': 0})
file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # Si es una letra
            if char.isalpha():
                counters[char.lower()] += 1
            # Si es un numero
            elif char.isdigit():
                counters[char] += 1
            else:
                # Si no es letra ni numero
                counters['especial'] += 1

    file.close()
    for char, count in counters.items():
        if count > 0:
            if char == 'especial':
                print("Caracteres especiales", '->', count)
            else:
                print(char, '->', count)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
