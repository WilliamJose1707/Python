def Conversion_Binario(n):
    if n == 0:
        return '0'
    else:
        binario = ''
        while n > 1:
            resto = n%2
            n = int(n/2)
            binario += str(resto)
        binario += '1'
    return binario[-1::-1]

def Conversion_Octal(n):
    if n == 0:
        return '0'
    else:
        octal = " "
        while n > 0:
            remainder = n % 8
            n = n // 8
            octal = str(remainder) + octal
        return octal
	
while True:

    i = int(input('Digite o numero qual deseja realizar a conversão: '))
    print('''Abaixo são as opções de conversão do Nosso Sistema
    [1] Converter para binário
    [2] Converter para Octal
    [3] Converter para hexadecimal
    [0] Sair do Sistema''')

    option   = int(input('Escolha a Opção: '))

    if option == 0:
        print('Obrigado por utilizar nosso sistema!')
        quit()
    else:
        
        if option == 1:
            print('O Resultado da Conversão do número inteiro : ', i , 'para Binario é: ', Conversion_Binario(i))

        elif option == 2:
            print('O Resultado da Conversão do número inteiro : ', i , 'para Octal é: ', Conversion_Octal(i))
                
        elif option == 3:
            def  Conversion_Hexadecimal(i):
                    if i == 15:
                            return "F"
                    elif i == 14:
                            return "E"
                    elif i == 13:
                            return "D"
                    elif i == 12:
                            return "C"
                    elif i == 11:
                            return "B"
                    elif i == 10:
                            return "A"
                    else:
                            return str(i)
                    
            continua = True
            while continua:
                    
                    result = ""
                    enum = 0
                    size = 1
                    num = i 
                    while True:		
                            if num > size * 16 ** enum:
                                    if size == 16:
                                            size = 1				
                                            enum += 1
                                    elif size < 16:
                                            size += 1
                            elif num == size * 16 ** enum:
                                    result += Conversion_Hexadecimal(size) + "0" * enum
                                    break
                            elif num < size * 16 ** enum:
                                    result += Conversion_Hexadecimal(size - 1)
                                    num -= ((size -1) * (16 ** enum))			
                                    size = 1
                                    enum = 0
                            if num <= 0:
                                    break
                    print(f"O Resultado da Conversão do numero {i} para Hexadecimal é : {result}")
                    continua = False
                    
        else:
            print('Opção Inválida !')







