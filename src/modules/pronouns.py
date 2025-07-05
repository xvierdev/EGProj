import random

def pronouns_test():
  response_quest1 = ["ele"]
  response_quest2 = ["ela"]
  response_quest3 = ["eles", "elas"]
  response_quest4 = ["voce","voçe"]
  response_quest5 = ["eu"]
  random_pronoun = random.randint(1, 4)
  match random_pronoun:
   
    case 1:

     quest1 = input("A tradução de 'he' é: ")
    
     if quest1.lower() == response_quest1[0].lower():
      print('Correct!')
    
     else:
       print('incorrect')

    case 2:
     
      quest2 = input("A tradução de 'she' é: ")
      
      if quest2.lower() == response_quest2[0].lower():
        print('Correct')
      
      else: 
        print('Incorrect!')

    case 3:
    
      quest3 = input("A tradução de 'they' é: ")
    
      if quest3.lower() == response_quest3[0].lower():
        print('Correct!')

      elif quest3.lower() == response_quest3[1].lower():
        print('Correct!')

      else: 
        print('incorrect!')

    case 4:
    
     quest4 = input("A tradução de 'you' é: ")
    
     if quest4.lower() == response_quest4[0].lower():
      print('Correct!')

     elif quest4.lower() == response_quest4[1].lower():
      print('Correct!')

     else: 
      print('Incorrect!')
    
    case 5:
     
     quest5 =  input("A tradução de 'I' é: ")
     
     if quest5.lower() == response_quest5[0].lower():
       print('Correct!')

     else: 
       print('Incorrect!')
#apagar uso para teste
pronouns_test()

