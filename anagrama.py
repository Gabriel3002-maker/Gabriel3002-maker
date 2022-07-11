#COMO SE SI DOS STRINGS SON UN ANAGRAMA

def run():
    #pedimos los strings
    word_1 = input('Digite una palabra')
    word_2 = input('Digite otra palabra')
    print(f'¿La palabra"{word_1}"es anagrama de "{word_2}? {set(word_1) == set(word_2)}"')

if __name__ == '__main__':
    run()
