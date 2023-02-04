def ceaser(message):
    encrypted_message = ''

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in message:

        if i not in alphabet:
            encrypted_message += i
        else:
            encrypted_message += alphabet[
                (alphabet.index(i)+3) % len(alphabet)]

    print("The encrypted message is:", encrypted_message)

text = input("Your message: ").lower()
ceaser(text)