def text_stadistics():
    text = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way 
    to do it.
    Although that way may not be obvious at first unless you're 
    Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good 
    idea.
    Namespaces are one honking great idea -- let's do more of 
    those!"""

    total_lines = text.split(".\n")

    total_words = text.split()

    suma = 0
    for line in total_lines:
        suma += len(line.split())
    words_prom = suma/len(total_lines)

    higher_prom = [f"\"{line}\"" + f" {len(line.split())} palabras)"
                   for line in total_lines 
                   if len(line.split()) > words_prom]

    print(f"Total de lineas: {len(total_lines)}")
    print(f"Total de palabras: {len(total_words)}")
    print(f"Promedio de palabras por linea: {words_prom}")
    for line in higher_prom:
        print(line)