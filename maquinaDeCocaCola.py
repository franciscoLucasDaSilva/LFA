


produtos = {1:
            {"coca-cola":0.45}
            }
while True:
    while True:
        e = input("<Enter para iniciar>\n")
        print("Escolha um produto:")
        try:
            for idProduto in produtos:
                print(str(idProduto) + " -> " + list(produtos[idProduto].keys())[0]+"\n")
                
            e = input("Produto: ")
            opt = int(e)
            cancelar = False
            if opt in produtos:
                print("Para cancelar o processo todo, voce pode digitar a qualquer momento a letra X\n")
                prod = list(produtos[opt].keys())[0]
                prec = produtos[opt][prod]
                print("Escolha: "+ prod+"\n")
                print("Preço: "+str(prec)+"\n")

                listaMoedasInseridas = []
                moedasAceitas = [0.10,0.25]
                
                print("Insira as moedas, quando terminar digite a letra C para confirmar...\n")
                while True:
                    valor = input(">>> ")
                    if valor.lower().strip() == "c":
                        break
                    elif float(valor) in moedasAceitas:
                        listaMoedasInseridas.append(float(valor))
                    elif valor.lower().strip() == "x":
                        cancelar = True
                        break
                    else:
                        pass
                if cancelar:
                    break
                else:
                    soma = sum(listaMoedasInseridas)
                    if soma >= prec:
                        print("<Maquina cospe '"+prod+"' para o usuário>\n")
                        break
                    else:
                        print("Operação inválida, insira o valor correto\n")
            else:
                pass
            
        except:
            pass
