grafo = {}

grafo["lucas"] = ["ana","henrique","luiz"]

grafo["ana"] = ["lucas","pedro","marcos"]

grafo["luiz"]= ["lucas","martins","helena"]

grafo["pedro"] = ["lucas", "marcos"]

grafo["helena"] = ["lucas", "martins"]

grafo["martins"] = ["lucas","helena"]

grafo["marcos"] = ["pedro", "lucas"]

grafo["henrique"] = ["ana", "luiz"]



print(grafo)




def pesquisa(pessoa):

    verificados = []

    fila = []

    caminho = ["lucas"]

    fila += grafo["lucas"]
    verificados.append("lucas")

    while fila:
        
        for pesG in fila:

            if pesG == pessoa:
                
                caminho.append(pesG)
                return pesG
                break

            else:
                if pesG not in verificados:
                    verificados.append(pesG)
                    fila.pop(0)
                    fila += grafo[pesG]

                else:
                    fila.remove(pesG)
                    continue

    else:
        return "esse nome não esta na vizinhaça"



        

print(pesquisa("marcos"))



print("fim")