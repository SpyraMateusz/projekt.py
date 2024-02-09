import random
import string

def generate_password(length):
    """Generuje losowe hasło o zadanej długości."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Podaj długość hasła: "))
        if length <= 0:
            print("Długość hasła musi być większa od zera.")
            return
        password = generate_password(length)
        print("Wygenerowane hasło:", password)
    except ValueError:
        print("Wprowadzona wartość nie jest liczbą.")

if __name__ == "__main__":
    main()
    #Uruchomienie tego programu spowoduje wygenerowanie losowego hasła o danej przez użytkownika długości.