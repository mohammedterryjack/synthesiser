from src.synthesiser import SimpleSynthesiser


x = SimpleSynthesiser("sounds")

#this = ["ð","i","s"]
#x.synthesise(this)

#these = ["ð","i:","z"]
#x.synthesise(these)

#people = ["p","h","i:","p","h","u:"]
#x.synthesise(people)

#ARE YOU HAVING A LAUGH
"ɑː juː haviŋ ɑ lɑːf" #BBC english
"iavina laf" #Northern English
#x.synthesise(["ɑ:","'","i","u:","'","h","a","v","i","ŋ","'","ɑ","'","l","ɑ:","f"]) #BBC english
#x.synthesise(["i","a:","v","i","ŋ","a","'","l","a:","f"]) #Northern English (y'avin a laugh)

#SHUT UP
"ʃɑtɑp" #BBC english
"ʃa ɑp"  #London Cockney 
"ʃorɑp"  #Northern English 
#x.synthesise(["ʃ","ɑ","t","'","a","p"]) #BBC english
#x.synthesise(["ʃ","a:","ɑ","p"]) #London Cockney 

#ITS KIND OF BROKEN
"its kɑind of broʊkn" #BBC english
"s kaj:nda bro en" #Southern English
#x.synthesise(["k","ɑ","i","n","d","'","o","f","'","b","r","o","u:","k","n"]) #BBC english
#x.synthesise(["k","a:","i:","n","d","'","a","'","b","r","o","u:","'","n"]) #Southern English - Kinda bro'en 