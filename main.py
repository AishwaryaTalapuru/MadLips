import random
#Reading inputs of different parts of speech from the user
proper_noun = input("Enter a PROPER NOUN : ")
proper_noun = proper_noun[0].upper()+proper_noun[1: ].lower()
gender = input("Enter gender (female/male): ")
if gender.lower()=="female":
    gender = "She"
else:
    gender = "He"
noun = input("\n Enter a NOUN: ").lower()
verb = input("\n Enter a VERB: ").lower()
adjective = input("\n Enter an ADJECTIVE: ").lower()

mad_lips = []
# Appending the phrases to the array
mad_lips.append(f"{proper_noun} was a great human. {gender} would eat {noun} everyday to stay fit and \
healthy. {gender} would ocassionally {verb} but never felt ill. So congratulations to the \
{adjective} human ")

mad_lips.append(f"{proper_noun} is a social activist. {gender} prefers driniking {noun} over tea. {gender} \
believes in gender equality and strives {adjective} to maintain it. Having a good balance between {verb} and personal life\
 {gender} proves to be good leader")

# Randomly selecting a phrase from all the phrases
print(mad_lips[random.randint(0, len(mad_lips)-1)])   
