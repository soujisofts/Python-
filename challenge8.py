n1 = float(input('Digite quantos metros deseja saber os centimetros e os milimetros: '))
cm = n1 * 100
mm = n1 * 1000

print('Centimetros: {}cm\nMilimetros: {}mm'
      .format(cm, mm))
# Basta multiplicar por 100 e 1000, já que a expressão {:.2f} e {:.3f} não funciona pra essa questão.