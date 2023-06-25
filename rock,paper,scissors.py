import random 
options=("paper","rock","scissors")
ruinning=True
while ruinning:
  omar= None
  ali=random.choice(options)
  while omar not in options :
    omar=input("enter your option (paper,rock,scissors) : ")
    print(f"omar: {omar}")
    print(f"ali: {ali}")
    if omar==ali:
     print("let's do it again ")
    elif omar=="scissors" and ali=="paper":
     print("Omar win ")
    elif omar=="paper" and ali=="rock":
     print("Omar win ")
    elif omar=="rock" and ali=="scissors":
     print("Omar win ")
    else:
     print("Ali win ")

     playing_again=input("play again ? (y/n)").lower()
     if not playing_again=="y":
      ruinning=False
print("thanks for playing ! ")