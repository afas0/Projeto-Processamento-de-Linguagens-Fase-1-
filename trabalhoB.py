from graphviz import Digraph
import argparse
import json

counter = 1 # para comecar em q1 a numeracao dos estados
novas_transicoes : dict = {}
temp = {}

#expressao é o simbolo e estado é para alterar os estados
def alt(expressao1, expressao2, estado1, estado2, final): # args = ['a','ab*']             q1,q2,q3,q4,q5,
    #counters defaults
    global counter
    global novas_transicoes
    global temp #guarda o ultimo estado
   
    novo_estado_1 = f'q{counter}'
    counter = counter + 1
    novo_estado_2 = f'q{counter}'
    counter = counter + 1
    novo_estado_3 = f'q{counter}'
    counter = counter + 1
    novo_estado_4 = f'q{counter}'
    counter = counter + 1
    novo_estado_5 = f'q{counter}'
    counter = counter + 1
    novo_estado_6 = f'q{counter}'
    counter = counter + 1
    if counter == 7 :
        temp = novo_estado_6
    
    novas_transicoes[novo_estado_1] = {"ε": (novo_estado_2, novo_estado_3)}
    novas_transicoes[novo_estado_2] = {expressao1: novo_estado_4}
    novas_transicoes[novo_estado_3] = {expressao2: novo_estado_5}
    novas_transicoes[novo_estado_4] = {"ε": novo_estado_6}
    novas_transicoes[novo_estado_5] = {"ε": novo_estado_6} 
    # so sao criados novos counters se cumprir os requesitos
    #no automato expressao 1 é a parte de cima e expressao 2 é parte de baixo do x|x
    if estado1 and estado2:
        novo_estado_7 = f'q{counter}'
        novo_estado_8 = f'q{counter+1}'
        novas_transicoes[novo_estado_1] = {"ε": (novo_estado_7,novo_estado_8)}
        novas_transicoes.pop(novo_estado_2)
        novas_transicoes.pop(novo_estado_3) 
        novas_transicoes.pop(novo_estado_4) 
        novas_transicoes.pop(novo_estado_5)    
    elif estado1:
        novo_estado_7 = f'q{counter}'       
        novas_transicoes[novo_estado_1] = {"ε": (novo_estado_3, novo_estado_7)} 
        #eliminar os dois estados a mais estado criado anteriormente
        novas_transicoes.pop(novo_estado_2)
        novas_transicoes.pop(novo_estado_4)             
    elif estado2:
        novo_estado_7 = f'q{counter}'      
        novas_transicoes[novo_estado_1] = {"ε": (novo_estado_2, novo_estado_7)}
        novas_transicoes.pop(novo_estado_3)
        novas_transicoes.pop(novo_estado_5)
    
    if final:
        novas_transicoes[novo_estado_6] = {"ε": temp}        

def seq(expressao1, expressao2, estado1, estado2, final): # args = ['a','ab*']             -> args = ["a"]
    global temp
    global counter
    global novas_transicoes
    novo_estado_1 = f'q{counter}'
    counter = counter + 1
    novo_estado_2 = f'q{counter}'
    counter = counter + 1
    novo_estado_3 = f'q{counter}'
    counter = counter + 1
    novo_estado_4 = f'q{counter}'
    counter = counter + 1
    if counter == 5 :
        temp = novo_estado_4
    novas_transicoes[novo_estado_1] = {expressao1: novo_estado_2}
    novas_transicoes[novo_estado_2] = {"ε": novo_estado_3}
    novas_transicoes[novo_estado_3] = {expressao2: novo_estado_4}
    #para caso o args[0] tenha o simbolo ou o args[1]
    if estado1 and estado2:  ##VER MELHOR ESTE CASO VERRRRRRRRRRRRRRRRRRRRRRRR
        #novo_estado_5 = f'q{counter}'
       # novo_estado_6 = f'q{counter+1}'
        #novas_transicoes[novo_estado_1] = {expressao1: (novo_estado_5)}
        #novas_transicoes[novo_estado_5] = {"ε": (novo_estado_3)}
        #novas_transicoes[novo_estado_3] = {expressao2: (novo_estado_6)}       
       # novas_transicoes.pop(novo_estado_2,novo_estado_4,) 
        pass
    elif estado1:
        novo_estado_5 = f'q{counter}'
        novas_transicoes[novo_estado_5] = {expressao1: novo_estado_2}  # ver melhor
        #novas_transicoes.pop(novo_estado_1)
    elif estado2:
        novo_estado_5 = f'q{counter}'
        novas_transicoes[novo_estado_3] = {expressao2: novo_estado_5}
        #novas_transicoes.pop(novo_estado_3) 
    #return novas_transicoes
    if final:
        novas_transicoes[novo_estado_4] = {"ε": temp}

def kle(expressao1, expressao2, estado1, estado2, final):
    global counter
    global novas_transicoes
    global temp
    novo_estado_1 = f'q{counter}'
    counter = counter + 1
    novo_estado_2 = f'q{counter}'
    counter = counter + 1
    novo_estado_3 = f'q{counter}'
    counter = counter + 1
    novo_estado_4 = f'q{counter}'
    counter = counter + 1
    if counter == 5 :
        temp = novo_estado_4
    
    novas_transicoes[novo_estado_1]= {"ε": (novo_estado_2, novo_estado_4)}  
    novas_transicoes[novo_estado_2]= {expressao1: novo_estado_3}    
    novas_transicoes[novo_estado_3]= {"ε": (novo_estado_2, novo_estado_4)}
    if estado1| estado2:
        novo_estado_5 = f'q{counter}'
        novo_estado_6 = f'q{counter+1}'
        novas_transicoes[novo_estado_1] = {expressao2: novo_estado_5}
        novas_transicoes[novo_estado_6] = {"ε": (novo_estado_4,novo_estado_5)}
        novas_transicoes[novo_estado_5] = {expressao2: novo_estado_6}
        novas_transicoes.pop(novo_estado_2)
        novas_transicoes.pop(novo_estado_3)
    if final:
        novas_transicoes[novo_estado_4] = {"ε": temp}
    #return novas_transicoes

def trans(expressao1, expressao2, estado1, estado2, final):

    global counter
    global novas_transicoes
    global temp
    novo_estado_1 = f'q{counter}'
    counter = counter + 1
    novo_estado_2 = f'q{counter}'
    counter = counter + 1
    novo_estado_3 = f'q{counter}'
    counter = counter + 1
    novo_estado_4 = f'q{counter}'
    counter = counter + 1
    if counter == 5 :
        temp = novo_estado_4

    novas_transicoes[novo_estado_1]= {"ε": novo_estado_2}
    novas_transicoes[novo_estado_2]= {expressao1: novo_estado_3}
    novas_transicoes[novo_estado_3]= {"ε": (novo_estado_2, novo_estado_4)}
    if estado1| estado2:
        novo_estado_5 = f'q{counter}'
        novas_transicoes[novo_estado_3] = {expressao2: novo_estado_5}

    #return novas_transicoes
    if final:
        novas_transicoes[novo_estado_4] = {"ε": temp}

def collect_op_occurrences(obj, op_list=None):
    if op_list is None:
        op_list = []

    if isinstance(obj, dict):
        if 'op' in obj:
            op_list.append(obj['op'])
        for value in obj.values():
            collect_op_occurrences(value, op_list)
    elif isinstance(obj, list):
        for item in obj:
            collect_op_occurrences(item, op_list)
    return op_list   
#def expressoes (arv, args):    
def get_args_for_op(obj, target_op):
    if isinstance(obj, dict):
        if "op" in obj and obj["op"] == target_op:
            return obj.get("args", [])
        elif "args" in obj:
            # Recursively search for the target_op in the "args"
            for arg in obj["args"]:
                result = get_args_for_op(arg, target_op)
                if result:
                    return result
    return []

def evaluate(arv, args, op):
    global counter
    
    op_variables = {}
    op_list = collect_op_occurrences(arv)
    max_length = len(op_list)
    contador_aux = 1
    #simb_elements = get_simb_elements(arv["args"])
    #expressoes(arv, args)
    #simb = get_simb(arv)
    #target_op = "seq"

# Get args for the target op
    
    if isinstance(arv, dict):
        if 'op' in arv:       
            for function_name in op_list:               
                aux = True
                aux2 = True
                final = False
                args_for_op = get_args_for_op(arv, function_name)  
                function = globals().get(function_name)
                try:
                    expressao1 = args_for_op[0]["simb"]        
                except:
                    expressao1 = "ε"  
                    aux = False 
                try:
                    expressao2 = args_for_op[1]["simb"]        
                except:
                    expressao2 = "ε"  
                    aux2 = False                
                if(aux and aux2):
                    #Para ativar o alterar o proximo estado caso haja + que 1 operacao
                    if len(op_list) > 1 and contador_aux < max_length:
                        function(expressao1,expressao2,False, False, final)
                    elif contador_aux == max_length:
                        final = True
                        function(expressao1,expressao2,False, False, final)                            
                    else:
                        function(expressao1,expressao2,False, False, final)  
                elif(aux):
                    if len(op_list) > 1 and contador_aux < max_length:
                        function(expressao1,expressao2,False, True, final)
                    elif contador_aux == max_length:
                        final = True
                        function(expressao1,expressao2,False, False, final)
                    else:
                        function(expressao1,expressao2,False, False, final)  
                elif(aux2):
                    if len(op_list) > 1 and contador_aux < max_length:
                        function(expressao1,expressao2,True, False, final)
                    elif contador_aux == max_length:
                        final = True
                        function(expressao1,expressao2,False, False, final) 
                    else:
                        function(expressao1,expressao2,False, False, final)               
                else:
                    if len(op_list) > 1 and contador_aux < max_length:
                        function(expressao1,expressao2,True,True, final)
                    elif contador_aux == max_length:
                        final = True
                        function(expressao1,expressao2,False, False, final)              
                #function(expressao1,expressao2)
                contador_aux = contador_aux +1
        elif 'simb' in arv:
            return arv['simb']
    #raise Exception("Formato de árvore de expressão regular inválido")

def main():
    global counter
    global novas_transicoes
    unique_elements_following_states = {}
    with open("er.json", "r") as f:
        arvore = json.load(f)
        evaluate(arvore, arvore['args'], arvore['op'])

    unique_states = set()
    for source_state, transitions in novas_transicoes.items():
        # Adicione o estado de origem ao conjunto de estados únicos
        unique_states.add(source_state)
        # Percorra todas as transições do estado de origem
        for transition_symbol, target_states in transitions.items():
            # Se o alvo das transições for uma lista, significa que há várias transições possíveis
            if isinstance(target_states, list):
                # Adicione todos os estados de destino únicos à lista de estados únicos
                unique_states.update(target_states)
            # Se o alvo das transições for uma string, é apenas um estado único
            elif isinstance(target_states, str):
                # Adicione o estado de destino único ao conjunto de estados únicos
                unique_states.add(target_states)
    estado_inicial =  next(iter(novas_transicoes))
    
    Group1 = []
    Group2 = []

    for key, value in novas_transicoes.items():
        Group1.append(key)
        for state, transitions in value.items():
            if isinstance(transitions, tuple):
                Group2.extend(transitions)
            else:
                Group2.append(transitions)

    Group1 = list(set(Group1))
    Group2 = list(set(Group2))

    diff = set(Group2) - set(Group1)

    values = []
    #criar a lista do vocabulario
    for key, value in novas_transicoes.items():
        for k, v in value.items():
            if k not in values:
                values.append(k)
    json_output = {
        "Q": list(unique_states),
        "V": values,
        "q0": estado_inicial,
        "F": list(diff),
        "delta": novas_transicoes
    }

    with open("saida.json", "w",encoding="utf-8") as f:
        json.dump(json_output, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()