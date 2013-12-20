mathematicsOperator = {"+", "-", "*", "/", "//", "**"}

relationalOperator = {"<", ">", "<=", ">=", "=="}

assignmentOperator = {"="}

bracket = {"[", "]"}

brace = {"{", "}"}

parenthesis = {"(", ")"}

keyword = {'if', 'while', 'return', 'yield', 'for', 'None', 'class', 'else', 'elif', 'True',
           'False', 'from', 'import', 'print', 'def'}

punctuation = {".", ",", "?", "!", ";", '"', "'", "_", ":", "@", "/", "\\"}

def my_gen(file_name):
    with open(file_name) as f:
        for line in f:
            line = line.split()
            for word in line:
                while len(word) > 0:
                    length = len(word)
                    index = 0
                    if word[0] in parenthesis:
                        yield word[0], 'parenthesis'
                        word = word[1:]
                    if len(word) > 0 and word[0].isdigit():

                        num_index = 1
                        num = word[0]
                        while len(word) > num_index and word[num_index].isdigit():
                            num += word[num_index]
                            num_index += 1
                        yield num, 'number'

                        word = word[num_index:]
                    elif len(word) > 1 and ((word[0] == '*' and word[1] == '*') or (word[0] == '/' and word[1] == '/')):
                        yield word[0] + word[1], 'mathematicsOperator'
                        word = word[2:]

                    elif len(word) > 0 and word[0] in mathematicsOperator:  #looking for len[1] mathematics operators
                        yield word[0], 'mathematicsOperator'
                        word = word[1:]

                    elif len(word) > 0 and word[0] in relationalOperator:
                        yield word[0], 'relationalOperator'
                        word = word[1:]
                    elif word[0:2] in relationalOperator:
                        yield word[0:2], 'relationalOperator'
                        word = word[2:]
                    elif len(word) > 0 and word[0] in assignmentOperator:
                        yield word[0], 'assignmentOperator'
                        word[0] == '=' and word[1:] != '='
                        word = word[1:]
                    elif len(word) > 0 and word[0] in bracket:
                        yield word[0], 'bracket'
                        word = word[1:]
                    elif len(word) > 0 and  word[0] in punctuation:
                        yield word[0], 'punctuation'
                        word = word[1:]
                    elif len(word) > 0 and word[0] in brace:
                        yield word[0], 'brace'
                        word = word[1:]
                    for k in keyword:
                        if k == word:
                            yield word, 'keyword'
                            word = ''
                    for p in punctuation:
                        if p == word:
                            yield word, 'punctuation'
                            word = ''
                    if len(word) > 0 and (word[0].isalpha() or word[0] == '_'):
                        word_index = 1
                        name = word[0]
                        while len(word) > word_index and (word[word_index].isalpha() or word[word_index] == '_'):
                            name += word[word_index]
                            word_index += 1
                        yield name, 'object name'

                        word = word[word_index:]



                        if len(word) == length:
                        yield word[0], 'unknown'
                        word = word[1:]



if __name__ =="__main__":
    tokens = my_gen('project_11.py')
    while True:
        try: print tokens.next()
        except StopIteration:
            break












