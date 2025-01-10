all = input('Digita alguma coisa ai: ')
print('O tipo desse valor é ', type(all))
print('Só tem espaço? ', all.isspace())
print('É um número? ', all.isnumeric())
print('É alfabético? ', all.isalpha())
print('É alfanúmerico? ', all.isalnum())
print('Está em maiúsculas? ', all.isupper())
print('Está em minúsculas? ', all.islower())
print('Está capitalizada? ', all.istitle())

# O all usado anterior ao is é um objeto que tem atributos e metodos. foi usado como metodo no exemplo