# name of the tool : PyPassCheck
import time as t
import os
import random as r
Welcome_Statement = """[+] Running PyPassCheck\n"""


Judging = ["Strong", "Medium" , "Weak"]

Counters =  {
    "Capital" : 0,
    "Small"   : 0,
    "Special" : 0,
    "Numbers" : 0
}



def welcome():
      print(Welcome_Statement)
      t.sleep(2)

def main():
    print("[+] Evaluating your password")
    print("[+] Generating Strong Passwords")
    print("\n[-] Enter [1/2]")
    options = input("> ")

    match options:
         case 1:
              Checking_Password_main()
         case 2:
              Generating_main()
         case _:
                os.system("cls ; clear")
                main()


def Checking_Password_main():
    password = input("[-] Enter your password : ")
    Response = f"Your Password is {Checking(password)}."
    print(Response)


def Counting(compare):
    for key in Counters:
        if Counters[key] < compare:
            return False
    return True


def Checking(s):
    total_points = 0

    for char in s:
        if ord(char) in range(65,90):
            Counters["Capital"]+=1
        elif ord(char) in range(97 , 122):
            Counters["Small"]+=1
        elif ord(char) in range(48 , 57):
            Counters["Numbers"]+=1
        else:
            Counters["Special"]+=1

    for key in Counters:
        total_points += Counters[key]

    if total_points >= 16 and Counting(4) :
            return Judging[0]
    elif total_points >= 8 and Counting(2):
            return Judging[1]
    else:
         return Judging[2]
         
def Generating_main():
     print(f"[+] your Password is : {Generating()}")


def Generating():
     Password = ""
     for idx in range(1 , 5):
          Password+=chr(r.randint(65,90))
     for idx in range(1 , 5):
          Password+=chr(r.randint(97,122))
     for idx in range(1 , 5):
          Password+=chr(r.randint(48,57))
     for idx in range(1 , 5):
          Password+=chr(r.randint(33,47))

     return Password


main() # initiating