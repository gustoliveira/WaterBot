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

}

def main():
    # child() method is used to create or access a paths

    ref = ('msgs/sleep/') # To access a path or to create a new one
    auth.db.child(ref).update(data) # Function to add the data JSON in the ref path
    # auth.db.child(ref).child("15").remove() # Function to remove a message

    # msgs = auth.db.child("msgs").get() # Return from a path
    # aux = list(msgs.val().items()) # val() return a orderedDict, this convert to a list to make facilitate access data
    # aux = aux[1][1] # Choose what path will access
    # aux1 = random.randrange(1, len(aux)) # Chose a random message in a certain path
    # print(aux[aux1]) # For testing purpose -> Verify if the there is not a error to access the database data


if __name__=='__main__':
    main()