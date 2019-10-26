import random
import pyrebase
import collections
import authentication as auth

# Choose what message will send
def message():
    msgs = auth.db.child("msgs").get()
    aux = list(msgs.val().items()) # Catch all items from msgs (an ordered dict) and transform in a list to access them
    aux = aux[0][1]
    return aux[random.randrange(1, len(aux))]

# Add in the database
data = {
    '15':'Melhor uma pedra no caminho do que uma no rim, então: beba água',
    '16':'Beba água, vc vai me agradecer depois',
    '17':'Coé, meno, já bebeu sua água hoje?',
    '18':'Rosas são vermelhas, violetas são azuis, vai tomar água',
    '19':'Aviso pra tomar água',
    '20':'Olha a hora mano, é hora de tomar água',
    '21':"Mein, pela sua saude, vai beber água",
    '22':"Pelo amor de Deus, camarada, não aguento mais manda tu tomar agua!!!",
    '23':"Ainn, tenho ranço de quem não está tomando água agr, então vai lá tomar pq não quero ter ranço de voce...",
    '24':'Seu rim vai agradecer se tomar água agora',
    '25':"Keep calm and vai tomar água, patrão",
    '26':"Convenhamos, talvez já seja hora de tomar água, né...",
    '27':"Não é querendo pressionar nem nada, mas voce está se hidratando corretamente? Se não, tome água, se sim, tome água também",
    '28':"Voce tem certeza de que o que voce está fazendo agora é mais importante que se hidratar?"
}

def main():
    # child() method is used to create or access a paths

    ref = ('msgs/drink_water/') # To access a path or to create a new one
    auth.db.child(ref).update(data) # Function to add the data JSON in the ref path
    # auth.db.child(ref).child("15").remove() # Function to remove a message

    # msgs = auth.db.child("msgs").get() # Return from a path
    # aux = list(msgs.val().items()) # val() return a orderedDict, this convert to a list to make facilitate access data
    # aux = aux[1][1] # Choose what path will access
    # aux1 = random.randrange(1, len(aux)) # Chose a random message in a certain path
    # print(aux[aux1]) # For testing purpose -> Verify if the there is not a error to access the database data


if __name__=='__main__':
    main()