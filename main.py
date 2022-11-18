input_card1 = input(" Enter your name:")
input_card2 = input("Enter yore age:")
input_card3 = input("Enter your address:")
if input_card2.isdigit() and not input_card1.isspace() and not input_card3.isspace():
    input_card1 = str(input_card1)
    input_card2 = int(input_card2)
    if input_card1 and input_card2 and input_card3:
        print("Hello,thanks for being one of our community,enjoy")
    else:print("Error value")
