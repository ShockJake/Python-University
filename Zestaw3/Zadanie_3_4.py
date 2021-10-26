# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x. 
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop. 
# Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.

def main_loop():
    while(True):
        user_input = input("Write real number or write \'stop\' to end the program: ")
        if(user_input == 'stop'):
            break
        try:
            user_input = float(user_input)
            num_3th = pow(user_input, 3)
            print("Written number: " + str(user_input) + " Third power of written number: " + str(num_3th))
        except ValueError:
            print('You didn\'t write a number, try again')

def main():
    main_loop()

if __name__ == "__main__":
    main()