#Cipher project

def cEncrypt(message, shift):
  newMsg= ""
  for char in message:
    newNum=ord(char)+shift
    newMsg+=chr(newNum)    
  return newMsg

def cDecrypt(phrase, shift):
  newMsg=""
  for char in phrase:
    newNum=ord(char)-shift
    newMsg+=chr(newNum)
  return newMsg

def AtBastEncrpyt():
  WordToEncrypt = input("AtBash cipher: Please enter message to encrpypt: ")
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
  lettersBackwards = "ZYXWVUTSRQPONMLKJIHGFEDCBA/"
  lettersNormal = []
  lettersBack = []
  EncryptedString = ""
  found = False
  for i in range(27):
    lettersNormal.append(letters[i])
  for i in range(27):
    lettersBack.append(lettersBackwards[i])
  for char in WordToEncrypt:
    for lettersCheck in lettersNormal:
      if char.upper() == lettersCheck:
        indexNum = lettersNormal.index(lettersCheck)
        EncryptedString += lettersBack[indexNum] 
        found = True
    if not found:
      EncryptedString += char
    found = False
  EncryptedString = EncryptedString.lower()
  print(EncryptedString)
  
def AtBastDecrypt():
  WordtoDecrpypt = input("AtBash cipher: Please enter message to decrpypt: ")
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
  lettersBackwards = "ZYXWVUTSRQPONMLKJIHGFEDCBA/"
  lettersNormal = []
  lettersBack = []
  DecryptedString = ""
  Found = False
  for i in range(27):
    lettersNormal.append(letters[i])
  for i in range(27):
    lettersBack.append(lettersBackwards[i])
  for charDecrypt in WordtoDecrpypt:
    for lettersCheckDecrypt in lettersBack:
      if charDecrypt.upper() == lettersCheckDecrypt:
        indexNum = lettersBack.index(lettersCheckDecrypt)
        DecryptedString += lettersNormal[indexNum]
        Found = True
    if not Found:
      DecryptedString += charDecrypt
    Found = False
  DecryptedString = DecryptedString.lower()
  print(DecryptedString)

def OwnCipherEncryption():
  message = input("Madeup cipher: Please enter a message to encrypt: ")
  ForwardRoll = int(input("Madeup cipher: Enter a number to forward roll: "))
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
  lettersJumbled1 = "OPFAYTCVQWMBSLJ XGEKZDHNURI"
  lettersNormal = []
  lettersJumbled = []
  EncryptedString1 = ""
  EncryptedString = []
  EncryptedString2 = ""
  found = False
  for i in range(27):
    lettersNormal.append(letters[i])
  for i in range(27):
    lettersJumbled.append(lettersJumbled1[i])
  for char in message:
    for letters1 in lettersNormal:
      if char.upper() == letters1:
        indexNum = lettersNormal.index(letters1)
        EncryptedString1 += lettersJumbled1[indexNum] 
        found = True
    if not found:
      EncryptedString1 += char
    found = False
  EncryptedString1 = EncryptedString1.lower()
  for characters in EncryptedString1:
    newnum = ord(characters) + ForwardRoll
    EncryptedString.append(newnum)
  for char in EncryptedString:
    EncryptedString2 = EncryptedString2 + str(char) + " " 
  print(EncryptedString2)
    
def OwnCipherDecryption():
  message = input("Madeup cipher: Enter the numbers seperated with space (example: 1 10 20 30): ")
  message = message.split()
  BackwardRoll = int(input("Madeup cipher: Enter a number to backward roll: "))
  lettersJumbled1 = "OPFAYTCVQWMBSLJ XGEKZDHNURI"  
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
  lettersNormal = []
  lettersJumbled = []
  DecryptedString1 = ""
  DecryptionProcess = []
  i = 0
  found = False
  for i in range(27):
    lettersNormal.append(letters[i])
  for i in range(27):
    lettersJumbled.append(lettersJumbled1[i])
  for i in range(len(message)):
    message[i] = int(message[i]) - BackwardRoll
  for char in message:
    for letters1 in lettersJumbled:
      if chr(char).upper() == letters1:
        indexNum = lettersJumbled.index(letters1)
        DecryptedString1 += lettersNormal[indexNum] 
        found = True
    if not found:
      DecryptedString1 += chr(char)
    found = False
  DecryptedString1 = DecryptedString1.lower()
  print(DecryptedString1)
  
while True:
  choice = input("Which cipher do you want to use? Enter 'c' for Ceasar cipher or Enter 'at' for AtBash cipher or Enter 'm' for madeup cipher or 'end' to end:")
  if choice.lower()=="c":
    while True:
      choiceOne = input("Enter 'ce' for ceasar encrypt and 'cd' for ceasar decrypt or 'end' to return to main menu: ")
      if choiceOne.lower() == "ce":
        phrase = input("Ceasar cipher: Please enter a message to encrypt:")
        num = int(input("Ceasar cipher: Please enter a number to Forward Roll: "))
        print(cEncrypt(phrase, num))
      elif choiceOne.lower() == "cd":
        phrase = input("Ceasar cipher: Please enter a message to decrypt:")
        num = int(input("Ceasar cipher: Please enter a number to Backward Roll: "))
        print(cDecrypt(phrase, num))
      elif choiceOne.lower() == "end":
        break
      else:
        print("Invalid entry, please try again!")
        continue
  elif choice.lower() == "at":
    while True:
      choiceTwo = input("Enter 'ae' for Atbash encrypt and 'ad' for Atbast decrypt or 'end' to return to main menu: ")
      if choiceTwo.lower() == "ae":
        AtBastEncrpyt()
      elif choiceTwo.lower() == "ad":
        AtBastDecrypt()
      elif choiceTwo.lower() == "end":
        break
      else:
        print("Invalid entry, please try again!")
        continue
  elif choice.lower() == "m":
    while True:
      choiceThree = input("Enter 'me' for madeup encrypt and 'md' for madeup decrypt or 'end' to return to main menu: ")
      if choiceThree.lower() == "me":
        OwnCipherEncryption()
      elif choiceThree.lower() == "md":
        OwnCipherDecryption()
      elif choiceThree.lower() == "end":
        break
      else:
        print("Invalid entry, please try again!")
        continue
  elif choice.lower() == "end":
    print("Thank you for using my program! Please run it again to encrypt or decrypt anything!")
    break
  else:
    print("Invalid entry, please try again!")
    continue