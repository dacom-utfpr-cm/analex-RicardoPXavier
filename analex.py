from automata.fa.Moore import Moore
import sys, os

from myerror import MyError

error_handler = MyError('LexerErrors')

# Conjunto de caracteres válidos
caracteres_validos = set(
    ['i', 'e', 'r', 'v', 'w', 'f', 'n', 'l', 't', 's', 'o', 'a', 'u', 'd', 'h',
     '+', '-', '*', '/', '<', '=', '>', '!', ';', ',', '(', ')', '[', ']', '{', '}', ' ', '\n',
     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
)

# Função para verificar se um caractere é inválido
def caractere_invalido(caractere):
    return caractere not in caracteres_validos

moore = Moore(
  ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
   'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q18', 'q19', 'q20', 'q21',
   'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31',
   'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 
   'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 
   'q52', 'q53', 'q54', 'q55', 'q56'],
 
  ['i', 'e', 'r', 'v', 'w', 'f', 'n', 'l', 't', 's', 'o', 'a', 'u', 'd', 'h',
      '+', '-', '*', '/', '<', '=', '>', '!', ';', ',', '(', ')', '[',
   ']', '{', '}', ' ', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

  ['IF', 'ELSE', 'INT', 'RETURN', 'VOID', 'WHILE', 'PLUS', 'MINUS', 'TIMES',
   'DIVIDE', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL', 'DIFFERENT',
   'SEMICOLON', 'COMMA', 'LPAREN', 'RPAREN', 'LBRACKETS', 'RBRACKETS', 'LBRACES',
   'RBRACES', 'ATTRIBUTION', 'EQUALS', 'NUMBER'],
 
  {
    'q0': { 'i': 'q1', 'e': 'q3', 'r': 'q10', 'v': 'q15', 'w': 'q19', '+':  'q23',
           'a': 'q50', 'u': 'q50', 'd': 'q50', 'h': 'q50', 's': 'q50', 'o': 'q50',
            't': 'q50', 'l': 'q50', 'n': 'q50', 'f': 'q51', '-': 'q24', '*':'q25',
            '/': 'q26', '<': 'q27', '>': 'q30', '=': 'q33', '!': 'q34', ';':'q44',
            ',': 'q45', '(': 'q37', ')': 'q38', '[': 'q39', ']': 'q40', '{':'q41',
            '}': 'q42', '0': 'q48', '1': 'q48', '2': 'q48', '3': 'q48', '4':'q48',
            '5': 'q48', '6': 'q48', '7': 'q48', '8': 'q48', '9': 'q48', ' ': 'q0',
            '\n': 'q0' },
    'q1': { 'f': 'q2', 'n': 'q7' }, 'q2': { '' : 'q0' }, 'q3': { 'l': 'q4', 't': 'q11' }, 'q4': { 's': 'q5' }, 'q5': { 'e': 'q6' }, 'q6': { '' : 'q0' },
    'q7': { 't': 'q8' }, 'q8': { '\n': 'q9', ' ': 'q9' }, 'q9': { '' : 'q0' }, 'q10': { 'e': 'q46' }, 'q11': { 'u': 'q12' }, 'q12': { 'r': 'q13' },
    'q13': { 'n': 'q14' }, 'q14': { '' : 'q0' }, 'q15': { 'o': 'q16', '' : 'q50' },'q16': { 'i': 'q17' }, 'q17': { 'd': 'q18' }, 'q18': { '' : 'q0' },
    'q19': { 'h': 'q20' }, 'q20': { 'i': 'q47' }, 'q21': { 'e': 'q22' }, 'q22': { '' : 'q0' }, 'q23': { '' : 'q0' },
    'q24': { '' : 'q56', '1': 'q48', '2': 'q48', '3': 'q48', '4': 'q48', '5': 'q48', '6': 'q48', '7': 'q48', '8': 'q48', '9': 'q48' },
    'q25': { '' : 'q0' }, 'q26': { '' : 'q0' }, 'q27': { '': 'q28', '=': 'q29' }, 'q28': { '' : 'q0' }, 'q29': { '' : 'q0' }, 'q30': { '': 'q31', '=': 'q32' },
    'q31': { '' : 'q0' }, 'q32': { '' : 'q0' }, 'q33': { '': 'q43', '=': 'q35' }, 'q34': { '=': 'q36' },
    'q35': { '' : 'q0' }, 'q36': { '' : 'q0' }, 'q37': { '' : 'q0' }, 'q38': { '' : 'q0' }, 'q39': { '' : 'q0' }, 'q40': { '' : 'q0' }, 'q41': { '' : 'q0' },
    'q42': { '' : 'q0' }, 'q43': { '' : 'q0' }, 'q44': { '' : 'q0' }, 'q45': { '' : 'q0' }, 'q46': { 't': 'q11' }, 'q47': { 'l': 'q21' },
    'q48': { '0': 'q48', '1': 'q48', '2': 'q48', '3': 'q48', '4': 'q48', '5': 'q48', '6': 'q48', '7': 'q48', '8': 'q48', '9': 'q48', '': 'q49'},
    'q49': { '' : 'q0' }, 'q50': { '' : 'q0' }, 'q51': { 'l': 'q52' }, 'q52': { 'o': 'q53' }, 'q53': { 'a': 'q54' }, 'q54': { 't': 'q55' },
    'q55': { '' : 'q0' },'q56': { '' : 'q0' },
  },
  #Estado inicial 
  'q0',
  {
    'q0': '', 'q1': '', 'q2': 'IF', 'q3': '', 'q4': '', 'q5': '', 'q6': 'ELSE', 'q7': '', 'q8': '',
    'q9': 'INT', 'q10': '', 'q11': '', 'q12': '', 'q13': '', 'q14': 'RETURN', 'q15': '', 'q16': '',
    'q17': '', 'q18': 'VOID', 'q19': '', 'q20': '', 'q21': '', 'q22': 'WHILE', 'q23': 'PLUS',
    'q24': '', 'q25': 'TIMES', 'q26': 'DIVIDE', 'q27': '', 'q28': 'LESS', 'q29': 'LESS_EQUAL',
    'q30': '', 'q31': 'GREATER', 'q32': 'GREATER_EQUAL','q33': '', 'q34': '', 'q35': 'EQUALS',
    'q36': 'DIFFERENT', 'q37': 'LPAREN', 'q38': 'RPAREN', 'q39': 'LBRACKETS', 'q40': 'RBRACKETS',
    'q41': 'LBRACES', 'q42': 'RBRACES', 'q43': 'ATTRIBUTION', 'q44': 'SEMICOLON', 'q45': 'COMMA',
    'q46': '', 'q47': '', 'q48': '', 'q49': 'NUMBER', 'q50': '', 'q51': '', 'q52': '', 'q53': '',
    'q54': '', 'q55': 'FLOAT', 'q56': 'MINUS',
  },
)

# Função para analisar o código fonte
def analysis(sourceFileString):
    # Variáveis
    estado = moore.initial_state
    tabela_saida = moore.output_table
    alfabeto_entrada = moore.input_alphabet
    tokens = []
    var = ''
    saida = 'q0'
    inicio_reservada = False
    inicio_comentario = False
    eh_comentario = False
    fim_comentario = False
    inicio_numero = False
    fim_numero = False
    simbolo_anterior = ''

    # Loop através do código fonte
    for simbolo in sourceFileString:
        # Número: início e fim
        if simbolo in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and not inicio_numero:
            inicio_numero = True
        if inicio_numero and simbolo not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            inicio_numero = False
            fim_numero = True

        # Comentários
        if inicio_comentario and simbolo != '*':
            inicio_comentario = False
        if eh_comentario and simbolo == '*' and not fim_comentario:
            fim_comentario = True
        if eh_comentario and simbolo == '/' and fim_comentario:
            eh_comentario = False
            fim_comentario = False
            continue
        if simbolo == '*' and inicio_comentario:
            tokens.pop()
            inicio_comentario = False
            eh_comentario = True
        if simbolo == '/' and not inicio_comentario:
            inicio_comentario = True
        if eh_comentario:
            continue

        # Verificação de caracteres inválidos
        if caractere_invalido(simbolo):
            tokens.append(('ERROR', 'ERR-LEX-INV-CHAR'))
            continue

        # Caracteres válidos
        if (simbolo in alfabeto_entrada and var == ''):
            # Tratamento de menos quando não é um número
            if (simbolo_anterior == '-' and simbolo != ' ' and simbolo != '\n' and simbolo not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                tokens.append(('MINUS', simbolo))
                inicio_reservada = False

            # Transição para o próximo estado quando há uma transição vazia
            if ('' in moore.transitions[estado] and (simbolo == ' ' or (simbolo_anterior == '-' and simbolo not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))) or fim_numero:
                saida = moore.transitions[estado]['']
                estado = saida
                fim_numero = False
                if tabela_saida[saida] != '':
                    tokens.append((tabela_saida[saida], simbolo))

            # Identificadores
            if (inicio_reservada and (simbolo not in ['i', 'e', 'r', 'v', 'w', 'f', 'n', 'l', 't', 's', 'o', 'a', 'u', 'd', 'h']) and simbolo != ' ' and simbolo != '\n'):
                tokens.append(('ID', simbolo))
                inicio_reservada = False
            if (simbolo in ['i', 'e', 'f', 'v', 'w', 'r'] and not inicio_reservada):
                inicio_reservada = True

            # Transição para o próximo estado
            if simbolo in moore.transitions[estado]:
                saida = moore.transitions[estado][simbolo]
            else:
                saida = moore.transitions[moore.initial_state][simbolo]

            # Números
            if saida == 'q50':
                var += simbolo

            # Tratamento de '!'
            if saida == 'q34':
                inicio_reservada = False
            elif tabela_saida[saida] != '':
                tokens.append((tabela_saida[saida], simbolo))
                inicio_reservada = False

            # Atualização do estado
            estado = saida
        else:
            var += simbolo
            if var != '' and (simbolo in alfabeto_entrada and (simbolo not in ['i', 'e', 'r', 'v', 'w', 'f', 'n', 'l', 't', 's', 'o', 'a', 'u', 'd', 'h'] or len(var) == 1)):
                if (simbolo in ['(', ')', '[', ']', '{', '}', ' ', '\n', ';', ',', '+', '-', '*', '/', '<', '=', '>', '!']):
                    saida = moore.transitions[moore.initial_state][simbolo]
                    tokens.append(('ID', var))
                    tokens.append((tabela_saida[saida], simbolo))
                    var = ''
                    inicio_reservada = False

        # Atualização do símbolo anterior
        simbolo_anterior = simbolo

    # Filtra tokens vazios
    tokens = list(filter(lambda x: x[0] != '', tokens))

    return tokens

def main():
    verifica_cm = False
    verifica_chave = False
    
    for idx, arg in enumerate(sys.argv):
        # print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'cm':
            verifica_cm = True
            idx_cm = idx

        if(arg == "-k"):
            verifica_chave = True
    
    # print ("No. of arguments passed is ", len(sys.argv))

    # Caso esteja comentado, nao passa no 1 teste do array 
    if(len(sys.argv) < 3):
         raise TypeError(error_handler.newError(verifica_chave, 'ERR-LEX-USE'))

    if not verifica_cm:
      raise IOError(error_handler.newError(verifica_chave, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(verifica_chave, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        dados = open(sys.argv[idx_cm])
        arquivo_fonte = dados.read()
        tokens = analysis(arquivo_fonte)
        for token in tokens:
            if (token[0] == 'ERROR'):
                raise IOError(error_handler.newError(verifica_chave, token[1]))
            else:
                print(token[0])

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)