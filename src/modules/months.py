import random

# escolhe um mês do ano aleatório e traduz do inglês pro português 

Months = {
     'January': 'janeiro',
     'February': 'fevereiro',
     'March':  'março',
     'April': 'Abril',
     'May': 'maio',
     'June':'junho',
     'July':'julho',
     'August': 'agosto',
     'September':'setembro',
     'October':'outubro',
     'November' : 'novembro',
     'December' : 'dezembro',
}

def start (self):
  english_month = random.choice(list(self.months.keys()))
     print (f "the translation of : '{english_month}' to Portuguese is:")
user_answer = input ("your answer").strip().lower()


If check_answer(english_month, user_answer):

     print("t: the answer is correct!")
     print( "one more point!")

else: 
      print ("the answer is incorrect.")
      print(" minus one point.")

def check_answer (english_month, user_answer):
    correct_translation = months [english_month]
    return user_answer == correct_translation

if__name_=='__main__' :
   Months ()
