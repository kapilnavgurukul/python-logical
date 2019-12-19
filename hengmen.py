import random
import string
from image import IMAGES

# this function for choice a word randomly
def sec_word():
	word_list=["kapil","rahul","satyam" ,"aanand","jaiprakash","yogendra","mahendra"]
	secret_word=random.choice(word_list)
	return secret_word
# print (sec_word())


def available_letter(gussid_word):
	avai_letter=string.ascii_lowercase
	b=list(avai_letter)
	for i in gussid_word:
		if i in b:
			b.remove(i)
	b="".join(b)
	return b
# print (available_letter("kapil"))


def word_guisses(secret_word,gussid_word):
	flag=True
	for i in secret_word:
		if i in gussid_word:
			continue
		else:
			flag=False
			return False
	if flag==True:
		return True



def get_guissed_word(gussid_word):
	index=0
	you_gussid=""
	while index<len(secret_word):
		if secret_word[index] in gussid_word:
			you_gussid+=secret_word[index]
		else:
			you_gussid+="_"
		index+=1
	return you_gussid

hard=[IMAGES[1],IMAGES[3],IMAGES[5],IMAGES[7]]
mediam=[IMAGES[1],IMAGES[3],IMAGES[4],IMAGES[5],IMAGES[6],IMAGES[7]]                
secret_word=sec_word()
def hangman():
	print ("welcome to the hangman")
	print ("letter in sec_word =  " +str(len(secret_word)))
	print ("")
	leval=str(input("easy ki liye-a ,mediam ke liye-b, and hard k liye-c ")).lower()
	gussid_word=''
	z=0
	if leval=="c":
		lives=4
	elif leval=="b":
		lives=6
	else:
		lives=8
	while lives>0:
		print ("available lives  -",lives)
		avail_letter=available_letter(gussid_word)
		print ("available letter  -  " +avail_letter)
		print ("")
		user=str(input("guisse kro\n"))
		user=user.lower()
	
		gussid_word+=user
		if z==0:
			if user=="hint":
				z=1
				user=random.choice(list(secret_word))
		if user in secret_word:
			your_gussid=get_guissed_word(gussid_word)
			print (your_gussid)
			a=word_guisses(secret_word,gussid_word)
			if a==True:
				print ("congrats !  you win")
				break
		else:
			print ("oops! wrong guisse")
			if leval=="c":
				print (hard[4-lives])
				lives-=1
			elif leval=="b":
				print (mediam[6-lives])
				lives-=1
			else:
				print (IMAGES[8-lives])
				lives-=1
	else:
		print ("sorry ! you lose this game")
		print ("the secret_word was - ",secret_word)

# # call this function
# hangman()