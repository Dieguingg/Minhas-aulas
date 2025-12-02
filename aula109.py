
# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
def soma(a, b, /, *, c, **kwargs):  # / indica que a e b são apenas posicionais
    print(kwargs)  # kwargs é um dicionário de argumentos nomeados
    print(a + b + c) # c é um argumento nomeado obrigatório


soma(1, 2, c=3, nome='teste') # Chamada com argumentos posicionais e nomeados
