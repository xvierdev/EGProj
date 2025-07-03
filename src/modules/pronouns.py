import random

def pronouns_test():

 random_pronoun = random.randint(1, 4)
 match random_pronoun:
   
    
    case 1:

     quest1 = input("A tradução de 'he' é: ")
    
     if quest1 == 'ele':
      print('Correct!')
    
     elif quest1 == 'Ele':
       print('Correct!')

     else:
       print('incorrect')



    case 2:
     
      quest2 = input("A tradução de 'she' é: ")
      
      if quest2 == 'ela':
        print('Correct')
      
      elif quest2 == 'Ela':
        print('Correct')
      
      else: 
        print('Incorrect!')



    case 3:
    
      quest3 = input("A tradução de 'they' é: ")
    
      if quest3 == 'eles':
        print('Correct!')
      
      elif quest3 == 'Eles':
        print('Correct!')

      elif quest3 == 'elas':
        print('Correct!')

      elif quest3 == 'Elas':
        print('Correct!')
      
      else: 
        print('incorrect!')



    case 4:
    
     quest4 = input("A tradução de 'you' é: ")
    
     if quest4 == 'Você':
       print('Correct!')

     elif quest4 == 'você':
       print('Correct!')
     
     elif quest4 == 'Voce':
       print('Correct!')

     elif quest4 == 'voce':
       print('Correct!')
     
     else: 
       print('Incorrect!')
    


    case 5:
     
     quest5 =  input("A tradução de 'I' é: ")
     
     if quest5 == 'Eu':
       print('Correct!')
     
     elif quest5 == 'eu':
       print('Correct!')

     else: 
       print('Incorrect!')

pronouns_test()

