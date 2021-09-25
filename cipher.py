from art import logo
import pyttsx3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices',  voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
restart_program = True    
while restart_program:

  speak("please tell us do you want to encode or decode a message")
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  speak("please enter the message below")
  text = input("Type your message:\n").lower()
  speak("enter the shift amount below")
  shift = int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


  def decrypt(cipher_text, shift_amount):

    plain_text = ""
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
    speak("do you wnt to encode or decode more")
  user_mind = input("do you want to do more  type yes or no : ")
  if user_mind=='no':
    restart_program=False
    

if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)

