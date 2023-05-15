print ("Simulador de Memória")

enderecos = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000']

opcoes = ''

while opcoes != 'P':
  
    opcoes = input("Escolha uma Opção: \n E - Escrever \n L - Ler \n S - Status da memória \n P - Parar \n : ")

#Parte 1: Operação de Leitura
    if opcoes == 'L':
        #vai pedir pro usuário Escolher o endereço
        endereco_ler_binario = input("Escolha um endereço: ")

        # condicional 
        if len(endereco_ler_binario) == 4:
            endereco_ler = int(endereco_ler_binario, 2)
          
            if endereco_ler >= 0 and endereco_ler <= 15:
                print("Endereço", endereco_ler_binario, "->", enderecos[endereco_ler])
              
            else:
                print("Endereço inválido. Digite um endereço binário: ")
              
        else:
            print("Endereço inválido. Digite um endereço binário: ")

#Parte 2: Operação de Escrita
    elif opcoes == 'E':
        endereco_escolhido_binario = input("Escolha um endereço: ")
      
        if len(endereco_escolhido_binario) == 4:
            endereco_escolhido = 0
          
            for bit in endereco_escolhido_binario:
                if bit == '1':
                  
                    endereco_escolhido = (endereco_escolhido << 1) + 1
                  
                else:
                    endereco_escolhido = endereco_escolhido << 1
                  
            if endereco_escolhido >= 0 and endereco_escolhido <= 15:
                valor = input("Digite o valor em binário a ser armazenado: ")
              
                if len(valor) == 4:
                    enderecos[endereco_escolhido] = valor
                  
                    print("Valor", valor, "armazenado no endereço", endereco_escolhido_binario, ".")
                else:
                    print("Valor incorreto. Digite um valor em binário: ")
                  
            else:
                print("Endereço inválido. Digite um endereço binário: ")
              
        else:
            print("Endereço inválido. Digite um endereço binário: ")

#Parte 3: Aqui mostra o Status da Memória
    elif opcoes == 'S':
        print("Status da memória: ")
        for i in range(16):
            endereco_binario = format(i, '04b')
            print(endereco_binario, "-", enderecos[i])

#Parte 4: Já aqui fica a condição de parada
    elif opcoes == 'P':
        print("Obrigada. Simulação Finalizada.")

#Parte 5: Caso aperte errado ou número esteja errado ele vai dizer que é invalida a entrada
    else:
        print("Opção inválida. Escolha uma opção válida.")

