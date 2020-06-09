import random

answer = random.randint(1,11)
print("Tebak angka 1-10")
guess = ""

while guess != answer:
  guess = int(input("Masukkan angka tebakan: "))
  if guess < answer:
    print("Kekecilan")
  elif guess > answer:
    print("Kebesaran")
  else: 
    print("Selamat")