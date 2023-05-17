import os
import random
import time
import playsound

def clear():
    #Função para limpara  tela
    os.system ("cls" if os.name == "nt" else "clear")
    def play_sound(sound_file):
    playsound.playsound(sound_file)

def get_random_word():
    # Função para escolher uma palavra aleatória da lista de palavras
    word_list = ["python", "programacao", "computador", "teclado", "mouse", "monitor", "jogos"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Função para exibir a palavra escondida, com as letras adivinhadas reveladas
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def draw_hangman(guesses):
    # Função para exibir o boneco dependendo do número de erros
    if guesses == 0:
        clear()
        print("""
           ____
          |/       |
          |
          |
          |
          |
        _|___
        |         |
        |___|
        """)
    elif guesses == 1:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |
          |
          |
        _|___
        |         |
        |___|
        """)
    elif guesses == 2:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |        |
          |
          |
        _|___
        |         |
        |___|
        """)
    elif guesses == 3:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |       /|
          |
          |
        _|___
        |         |
        |___|
        """)
    elif guesses == 4:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |       /|\\
          |
          |
        _|___
        |         |
        |___|
        """)
    elif guesses == 5:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |       /|\\
          |        |
          |
        _|___
        |         |
        |___|
        """)
    else:
        clear()
        print("""
           ____
          |/       |
          |       (_)
          |       /|\\
          |        |
          |       / \\
        _|___
        |         |
        |___|
        """)

def main():
    # Inicializa as variáveis
    word = get_random_word()
    guessed_letters = set()
    guesses = 0

    # Loop principal do jogo
    while True:
        draw_hangman(guesses)
        display = display_word(word, guessed_letters)
        print(display)

        # Verifica se o jogador venceu ou perdeu
        if "_" not in display:
            play_sound("confetti.mp3")
            print("Parabéns! Você acertou a palavra.")
            break
        elif guesses >= 6:
            play_sound("car_crash.mp3")
            print(f"Fim de jogo, a palavra era '{word}'. Tente novamente.")
            break
