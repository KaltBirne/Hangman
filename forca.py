import random

#Início do jogo
def forca():
  #Disponibilidade de tentativas
  attempts = 5 
  #Array das possíveis palavras
  word_list = ["gato", "rato","cachorro"]
  #Limite de dicas
  hint_attempts = 2
  #Escolha aleatória da palavra correta
  correct_answer = random.choice(word_list)
  word_length = len(correct_answer)
  print("Bem-vindo ao jogo da forca!")
  print(f"A palavra correta tem {word_length} letras.")

  #Lógica de reinício
  def restart():
   pass

  #Lógica da dica
  def hint():
   nonlocal hint_attempts

   hint_words = {
    "rato": {"Animal pequeno como um rato!"},
    "gato": {"Animal fofo como um gato!"},
    "cachorro": {"Animal peludo como um cachorro!"}
    }
   
   #comparar correct_answer com as dicas dentro do dicionário de dicas

   if hint_attempts >= 1 and correct_answer == (hint_words):
    print(hint_words)
    print("Oi")
     
  #Loop principal do jogo
  while True:
   #User input
   attempt_input = input('Digite uma palavra ou peça por uma "dica" \n').lower()
   

   #Comparar o  indice da tentativa com o indice da resposta correta 
   #Mostrar um output com base nisso

   word_position = len(correct_answer)
   correct_position = len(correct_answer)
   wrong_position = len(correct_answer)

   print(wrong_position)
   print(correct_position)
   print(word_position)

   #EXIT
   if attempt_input == "sair":
    print("Jogo encerrado. Até a próxima!")
    exit()
   #Relata o sucesso do usuário
   if attempt_input == correct_answer :
    print ("Você acertou!")
    restart()                                                            #Def reinício

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
    restart()                                                              #Def reinício
forca()