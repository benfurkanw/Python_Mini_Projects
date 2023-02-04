print("Welcome to the Caesar Code Cracking Program.")
sifresiz=input("Enter the text to be decrypted:")
def encrypt(text):
    YourCipherText=""
    for character in text:
        asciikod=ord(character)
        asciikod=asciikod-3
        karakterkod=chr(asciikod)
        YourCipherText=YourCipherText+karakterkod
    print("password unbroken text:",text,"\ndecrypted text:",YourCipherText)

encrypt(sifresiz)