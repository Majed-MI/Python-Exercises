# Dictionary format alphabet written for child
while(True):
    dict = {
    'A' : 'Apple','B' : 'Ball','C' : 'Cat','D' : 'Dog','E' : 'Elephant','F' : 'Frog','G' : 'Girl',
    'H' : 'Hat','I' : 'Ink','J' : 'Jungle','K' : 'Kite','L' : 'Lamp','M' : 'Mango','N' : 'Net',
    'O' : 'Owl','P' : 'Pencil','Q' : 'Queen','R' : 'Rat','S' : 'Star','T' : 'Tap','U' : 'Umbrella',
    'V' : 'Van','W' : 'Window','X' : 'X-ray','Y' : 'Yoke','Z' : 'Zebra',
    }

    # Capital alphabet input taken from user
    word = input("Type An Alphabet: ")
    # showing the alphabet for with the word
    print(word, "for" , dict[word])


