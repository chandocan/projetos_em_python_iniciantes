lista_email = []

while True:
    d = input('deseja fazer um cadastro ? [s] ou [n] :').lower()
    if d == 's':
        email  = input('digite o e-mail :')
        lista_email.append(email)
    print(lista_email)
    
    pergunta = input('deseja fazer uma busca ? [s] ou [n] :').lower()
    if pergunta == 's':
        busca = input('buscando email :')    
        for i in lista_email:
            
            if busca == i:
                print('e-mail cadastrado')
                print(i)
            if busca not in lista_email:
                print('e-mail não cadastrado')
                break
            
            if pergunta == 'n':
                continue
                
    q = input('escreva [sair] para fechar o programa ou [enter] para continuar ').lower()
    if q == 'sair':
        break
