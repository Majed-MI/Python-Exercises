# Receipt Generator for a shop
# declaring sum as 0 to calculate
sum = 0
# initializing dict as a list of products
dict = {
        'logo' : 10, 'tshirt' : 20, 'flyer' : 30, 'business card' : 5, 'web design' : 50,
        'brochure' : 15, 'banner' : 25, 'web develop' : 30, 'software design' : 50,
        'android web develop' : 100, 'video editing' : 20, 'game develop' : 100
    }
i=0
# getting the product keys
for item in dict.keys():
    i+=1
    print(i,".",item,end="\t\t")
    if i%5 == 0:
        print(end="\n")
# while loop to continue till no error
while True:
    # product input taken from user or quit option
    userInput = input("\nType A product for pricing or press q to quit: ")
    # if not quit then adding product function
    if userInput != 'q':
        # showing the product for the money
        print(userInput, "for", dict[userInput], "USD($)")
        # adding product price one by one
        sum = sum+dict[userInput]
        print(f"Your order total so far = {sum}")
    # if user press quit then
    else:
        print("Thanks for using our service")
        print(f"Your Bill Total is = {sum}. Thanks for being with us")
        break