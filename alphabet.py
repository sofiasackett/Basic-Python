#This program will print the alphabet from the two strings 'acegikmoqsuwy' and 'bdfhjlnprtvxz'

#input strings
alph1 = "acegikmoqsuwy"
alph2 = "bdfhjlnprtvxz"

#set accumulator variable alph_accum to an empty string to begin
alph_accum = ""

#add the strings together using a for loop (first letter of alph 1 then first letter of alph2, second letter of alph1, and so on..)
for i in range(13):
    alph_accum = alph_accum + alph1[i] + alph2 [i]

#create a third string from the accumulator alph_accum
alphabet = alph_accum

#print alphabet
print(alphabet)

