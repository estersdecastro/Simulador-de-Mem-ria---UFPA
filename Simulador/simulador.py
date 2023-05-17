print("Simulador de Memória")

memoria = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000']

menu = '' # declara a variável menu como vazia

while menu != 'P': # condição while de parada
  
    menu = input("Escolha uma Opção: \n E - Escrever \n L - Ler \n S - Status da memória \n P - Parar \n : ") # menu de opções

    # Parte 1: Operação de Leitura
    if menu == 'L': 
      
        # Vai pedir para o usuário escolher o endereço
        bin_endereco_leitura = input("Escolha um endereço: ")

        # Condicional 
        if len(bin_endereco_leitura) == 4: # Vai estabelecer a condição do tamanho do endereço inserido
            endereco_leitura = int(bin_endereco_leitura, 2) # Transforma o endereço inserido para o formato binário
          
            if 0 <= endereco_leitura <= 15: # Vai estabelecer a condição se o endereço está dentro do intervalo correto 
                print("Endereço", bin_endereco_leitura, "->", memoria[endereco_leitura]) # Vai retornar o endereço e o valor armazenado nele
              
            else: # Mensagem informando que o endereço é inválido
                print("Endereço inválido. Digite um endereço binário: ")
              
        else: # Mensagem informando que o tamanho do endereço está incorreto
            print("Endereço inválido. Digite um endereço binário: ")

    # Parte 2: Operação de Escrita
    elif menu == 'E':
        bin_endereco_escrita = input("Escolha um endereço: ")
      
        if len(bin_endereco_escrita) == 4: # Condição para verificar o tamanho do endereço
            endereco_escrita = 0 # inicia a variavel com valor 0 pra evitar erro

            # Transformar o endereço que foi inserido em binário para decimal indicando o índice da lista "memoria"
            endereco_escrita = int(bin_endereco_escrita, 2) # Transforma o endereço inserido para o formato binário
                  
            if 0 <= endereco_escrita <= 15:
                valor = input("Digite o valor em binário a ser armazenado: ")
              
                if len(valor) == 4:
                    memoria[endereco_escrita] = valor # Atribui o valor digitado ao índice em "memoria"
                  
                    print("Valor", valor, "armazenado no endereço", bin_endereco_escrita, ".") # Retorna o valor armazenado na memória e o local
                
                else:
                    print("Valor incorreto. Digite um valor em binário: ") # Mensagem de erro caso tenha menos de 4 caracteres
                  
            else:
                print("Endereço inválido. Digite um endereço binário: ") # Mensagem de erro caso esteja fora do intervalo
              
        else:
            print("Endereço inválido. Digite um endereço binário: ") 

    # Parte 3: Mostrar o Status da Memória
    elif menu == 'S':
        print("Status da memória: ")
        for i in range(16):
            endereco_binario = format(i, '04b') 
            print(endereco_binario, "-", memoria[i])

    # Parte 4: Condição de parada
    elif menu == 'P':
        print("Obrigada. Simulação Finalizada.")

    # Parte 5: Mensagem de opção inválida
    else:
        print("Opção inválida. Escolha uma opção válida.")

#


# variáveis do código: 

'''
valor: valor a ser armazenado

memoria: lista com índices de endereços da memória

e_endereco: endereço inserido pelo usuário em binário para operação de escrita

bin_e_endereco: endereço já transformado para binário para relacionar com o índice em "memoria" na operação de escrita

l_endereco: endereço inserido pelo usuário em binário para operação de leitura

bin_l_endereco: endereço já transformado para binário para relacionar com o índice em "memoria" na operação de leitura

menu: menu de opções
'''



