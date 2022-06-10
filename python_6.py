""""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

def int_func(word:str):
    word = word[0].upper() + word[1:]
    return word

print(int_func("text"))
