import json
with open('afnd.json', encoding="utf-8") as file:
    data = json.load(file)

estados = data["Q"]
vocabulario = data["V"]
vocabulario_afd = [letter for letter in data["V"] if letter != 'ε']
estado_inicial = data["q0"]
estados_finais = data["F"]
#transicoes = OrderedDict(sorted(data["delta"].items(), key=lambda item: int(item[0][1:])))
transicoes = data["delta"]

def tabelafechoepsilon(transicoes, estado_inicial):
    estado_aux = set()
    estado_aux2 = set()
    estado_aux2.add(estado_inicial)

    # Função auxiliar para calcular o fecho epsilon para um estado
    def fecho_epsilon_para_estado(estado_atual):
        fecho = set()
        fecho.add(estado_atual)
        if "ε" in transicoes.get(estado_atual, {}):
            for prox_estado in transicoes[estado_atual]["ε"]:
                fecho.add(prox_estado)
        return fecho

    while True:
        estado_aux = set()  # Reseta estado_aux em cada iteração
        for estado in estado_aux2:
            fecho_estado = fecho_epsilon_para_estado(estado)
            estado_aux.update(fecho_estado)

        # Verifica se houve alguma adição de novos estados em estado_aux
        if estado_aux == estado_aux2:
            break  # Se não houver novos estados, sai do loop
        else:
            estado_aux2.update(estado_aux)  # Atualiza estado_aux2 com os novos estados encontrados

    #estado_aux2_ordenado = OrderedDict(sorted(estado_aux2.items()))
    return estado_aux2

#fecho_epsilon_inicial = tabelafechoepsilon(transicoes, estado_inicial)
estados_finais_afd = []
transicoes_afd : dict  = {}
transicoes_afd_2 : dict  = {}  # Esta serve para guardar os valores e nao o nome
contador2 = 2
contador = 1 
#estado_aux4 = set()
#novo_estado_inicial = f'N{contador}' + fecho_epsilon_inicial
if  estado_inicial not in estados_finais:   
    estado_aux3 = set()   
    estado_aux4 = []
    total_symbols = len(vocabulario_afd)
    #fecho_epsilon_inicial = tabelafechoepsilon(transicoes, estado_inicial)
    while True:
        simbolo_aux = {}
        contador_simbolos = 1
        if contador == 1:
            fecho_epsilon_inicial = tabelafechoepsilon(transicoes, estado_inicial)
        else:
            fecho_epsilon_inicial = estado_aux3
            #estado_aux4.extend(list(estado_aux3))
           
            if estado_aux3 in estado_aux4:
                break
            else:
                 estado_aux4.append(set(estado_aux3))          
            #estado_aux4.extend("-")
            estado_aux3 = set()     
        for simbolo in vocabulario_afd:
            teste = False
            # Verifica se há uma transição para cada símbolo do vocabulário
            for estado in fecho_epsilon_inicial:
                # Verifica se há uma transição do estado atual com o símbolo atual       
                if estado in transicoes and simbolo in transicoes[estado]:
                    teste = True
                    prox_estado = transicoes[estado][simbolo]
                    for estado_now in prox_estado: # ver se isto nao esta a dar loop a mais
                        fecho_prox_estado = tabelafechoepsilon(transicoes, estado_now)
                        simbolo_aux = simbolo
                    # Calcula o fecho epsilon para o próximo estado            
                    # Adiciona o próximo estado e seu fecho epsilon ao conjunto estado_aux3
                    estado_aux3.update(fecho_prox_estado)
            #adiciona apenas quando encontrar algo no if em cima
            if teste and  estado_aux3 not in estado_aux4 :
                booleana=True
                for key in transicoes_afd_2:
                    # Check if estado_aux3 is equal to the key
                    if estado_aux3 == key:
                        transicoes_afd[f'N{contador}'] = {simbolo: transicoes_afd_2[key][simbolo] }
                        
                        bool = False
                        break
                    elif contador_simbolos == total_symbols:
                        pass  #ver esta parte
                if booleana:    
                    transicoes_afd[f'N{contador}'] = {simbolo: f'N{contador2}'}
                    transicoes_afd_2[tuple(estado_aux3)] = {simbolo: f'N{contador2}'}            
                if contador_simbolos == total_symbols:
                    contador += 1
                
                #estado_aux3 = sorted(list(estado_aux3))
                    
                if set(estados_finais).issubset(estado_aux3):          
                    #contador = 1
                    estados_finais_afd.append(f'N{contador2}') # adicionar a uma lista de estados finais e nao so ter 1 valor
                    contador2 += 1
                #verifica se já existe na lista para nao criar um novo estado
                else:
                    contador = contador + 1  
            elif teste and  estado_aux3 in estado_aux4:
                contador = contador + 1 
                transicoes_afd[f'N{contador}'] = {simbolo: f'N{contador}'}
                transicoes_afd_2[tuple(estado_aux3)] = {simbolo: f'N{contador}'}   
            contador_simbolos += 1                   
                
estados_unicos_afd = set()     
for source_state, transitions in transicoes_afd.items():
        # Adicione o estado de origem ao conjunto de estados únicos
        estados_unicos_afd.add(source_state)
        # Percorra todas as transições do estado de origem
        for transition_symbol, target_states in transitions.items():
            # Se o alvo das transições for uma lista, significa que há várias transições possíveis
            if isinstance(target_states, list):
                # Adicione todos os estados de destino únicos à lista de estados únicos
                estados_unicos_afd.update(target_states)
            # Se o alvo das transições for uma string, é apenas um estado único
            elif isinstance(target_states, str):
                # Adicione o estado de destino único ao conjunto de estados únicos
                estados_unicos_afd.add(target_states)

estado_inicial_afd =  next(iter(transicoes_afd))
afd : dict  = {}    
afd["Q"] = estados_unicos_afd
afd["V"] = vocabulario_afd
afd["q0"] = estado_inicial_afd
afd["F"] = estados_finais_afd
afd["delta"] = transicoes_afd
#output_file = open('output.json', 'w+')
#json.dump(dfa, output_file, separators=(',\t', ':'))

json_output = {
        "Q": list(estados_unicos_afd),
        "V": vocabulario_afd,
        "q0": estado_inicial_afd,
        "F": estados_finais_afd,
        "delta": transicoes_afd
    }

with open("output.json", "w",encoding="utf-8") as f:
    json.dump(json_output, f, indent=4, ensure_ascii=False)