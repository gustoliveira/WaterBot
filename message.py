import random
import pyrebase
import collections
import authentication_h as auth

# Choose what message will send
def message():
    msgs = auth.db.child("msgs").get()
    aux = list(msgs.val().items()) # Catch all items from msgs (an ordered dict) and transform in a list to access them
    aux = aux[0][1]
    return aux[random.randrange(1, len(aux))]

# Add in the database
data = {
    '28':"Voce tem certeza de que o que voce está fazendo agora é mais importante que se hidratar?",
    '29':"Voce sabia? Quem bebe água frequentemente tem 90% de chance de entrar na faculdade, e quem já entrou consegue sair ainda mais rápido desse inferno?",
    '30':"Beba água pra chorar com tranquilidade quando tiver uma crise <3",
    '31':"Beba água AGORA! Se não eu vou contar pra sua mãe",
    '32':"Sai do celular seu preguiçoso e vai tomar uns golão de água",
    '33':"Beba água, seja asseado, lave a louça, e durma cedo",
    '34':"Fotos bebendo água>>>>>Nudes",
    '35':"QUer dar orgulho a sua familia? Então drink água",
    '36':"Cerveja? To fora, pego meu galão de água e dou fora",
    '37':"'Beba água seu porra' EINSTEIN, Albert",
    '38':"Só é corno quem não toma água, pronto falei",
    '39':"Beber água é melhor do que beber semem, então beba água!",
    '40':"Tive um pesadelo horroroso, sonhei que meus seguidores não tomam água direito, credo"
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