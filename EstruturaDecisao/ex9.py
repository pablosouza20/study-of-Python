-'''
09 - Faça um programa que leia três números e mostre em ordem descrecente
'''
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('1 - {} \n2 - {} \n3 - {} '.format(num3, num2, num1))
    else:
        print('1 - {} \n2 - {} \n3 - {} '.format(num2, num3, num1))
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print('1 - {} \n2 - {} \n3 - {} '.format(num3, num1, num2))   
    else:
        print('1 - {} \n2 - {} \n3 - {} '.format(num1, num3, num2))             
else:
    if num1 > num2:
        print('1 - {} \n2 - {} \n3 - {} '.format(num2, num1, num3)) 
    else:
        print('1 - {} \n2 - {} \n3 - {} '.format(num1, num2, num3))           