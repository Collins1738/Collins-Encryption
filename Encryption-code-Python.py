print("WELCOME TO THE COLLINS ENCRYPTION CODE")
class encryption():
  def __init__(self):
    return

  def encrypt(self):
    self.encrypted=[]
    unencrypt=input("Type in a string or sentence you wish to encrypt")
    key=int(input("Type in encryption key"))
    for i in unencrypt:
      if ord(i) in range(65, 91):
        i=chr((((ord(i)-65)+(key%26))%26)+65)
        self.encrypted.append(i)
      elif ord(i) in range(97, 123):
        i=chr((((ord(i)-97)+(key%26))%26)+97)
        self.encrypted.append(i)
      else:
        self.encrypted.append(i)
    return "".join(self.encrypted)

  def decrypt(self):
    self.decrypted=[]
    undecrypt=input("Type in a string or sentence you wish to decrypt")
    key=int(input("Type in encryption key used to encrypt the data"))
    for i in undecrypt:
      if ord(i) in range(65, 91):
        i=chr((((ord(i)-65)-(key%26))%26)+65)
        self.decrypted.append(i)
      elif ord(i) in range(97, 123):
        i=chr((((ord(i)-97)-(key%26))%26)+97)
        self.decrypted.append(i)
      else:
        self.decrypted.append(i)
    return "".join(self.decrypted)
      

      



mad=encryption()
answer="babie doll"
while answer!="C":
  answer=input("What do you wish to do (A or B or C)\n[A] Encrypt a code\n[B] Decrypt an encrypted code\n[C] Exit\n")
  if answer=="A":
    print(mad.encrypt())

  elif answer=="B":
    print(mad.decrypt())
