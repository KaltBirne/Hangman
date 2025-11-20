import random
#import pygame

#Início do jogo
def forca():
  #Configuração de dificuldade
  while True:
   difficulty = input("Escolha a dificuldade: EASY, MEDIUM, HARD \n").lower()
   if difficulty == "easy":
    attempts = 7
    hint_attempts = 5
    break
   elif difficulty == "medium": 
    attempts = 5
    hint_attempts = 3
    break
   elif difficulty == "hard":
    attempts = 3
    hint_attempts = 1
    break
   else:
    print("Dificuldade inválida. Tente novamente.")
    continue

  #Array das possíveis palavras
  word_list = ["gato", "rato","cachorro"]
  #Escolha aleatória da palavra correta
  correct_answer = random.choice(word_list)
  #Comprimento da palavra correta
  word_length = len(correct_answer)
  print(f"Bem-vindo ao jogo da forca!\n Você escolheu a dificuldade {difficulty}.\n")
  print(f"A palavra correta tem {word_length} letras.")

  #Lógica de reinício
  #def restart():
   #pass

   #Lógica da dica
  def hint():
   nonlocal hint_attempts
   
   #Fornece a dica se for compatível
   if hint_attempts > 0 and correct_answer == "gato":
    print("Animal fofo como um gato!")
    hint_attempts -= 1
  
   if hint_attempts > 0 and correct_answer == "cachorro":  
    print("Animal peludo como um cachorro!")
    hint_attempts -= 1
  
   if hint_attempts > 0 and correct_answer == "rato":
    print("Animal pequeno como um rato!")
    hint_attempts -= 1

   elif hint_attempts == 0 : print("Desculpe, você não tem mais dicas disponíveis.")
   
   if hint_attempts > 0 :
    print (f"Você ainda tem {hint_attempts} dica(s) disponívelis.")
   else: print("Você não tem mais dicas disponíveis.") 
     
  #Loop principal do jogo
  while True:
   #User input
   attempt_input = input('Digite uma palavra ou peça por uma "dica" \n').lower()
   

   #Comparar o  indice da tentativa com o indice da resposta correta 
   #Mostrar um output com base nisso

   #word_position = len(correct_answer)
   #correct_position = len(correct_answer)
   #wrong_position = len(correct_answer)

   #print(wrong_position)
   #print(correct_position)
   #print(word_position)

   #EXIT
   if attempt_input == "sair":
    print("Jogo encerrado. Até a próxima!")
    exit()
   #Relata o sucesso do usuário
   if attempt_input == correct_answer :
    print ("Você acertou!")
    forca()                                                              #Def reinício

   #Fornece uma dica ao usuário
   if attempt_input == ("dica") :
    hint()                                                               #Def hint
   #Computa a perda de uma tentativa
   elif  attempt_input != correct_answer :
    attempts = attempts - 1
    print (f"Você errou! Restam {attempts} tentativa(s). ")
   #Relata a derrota do usuário
   if attempts <= 0 :
    print ("Você perdeu. Que pena!")
    print (f"A resposta correta era \"{correct_answer}\"")
    forca()                                                              #Def reinício
forca()