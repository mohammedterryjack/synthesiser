from src.synthesiser import SimpleSynthesiser


x = SimpleSynthesiser("sounds")

#this = ["ð","i","s"]
#x.synthesise(this)

#these = ["ð","i:","z"]
#x.synthesise(these)

#people = ["p","h","i:","p","h","u:"]
#x.synthesise(people)



#EG1: ARE YOU HAVING A LAUGH
"ɑː juː haviŋ a lɑːf" #BBC english
"iavina laf" #Northern English:   

#x.synthesise(["ɑ:","'","i","u:","'","h","a","v","i","ŋ","'","ɑ","'","l","ɑ:","f"]) #BBC english
#x.synthesise(["i","a:","v","i","ŋ","a","'","l","a:","f"]) #Northern English (y'avin a laugh)

#http://ipa-reader.xyz/?text=ɑː juː haviŋ a lɑːf&voice=Emma
#http://ipa-reader.xyz/?text=iavina laf&voice=Emma


#EG2 ITS KIND OF BROKEN
"its kɑind of broʊkn" #BBC english
"s kaj:nda bro en" #Southern English
#x.synthesise(["k","ɑ","i","n","d","'","o","f","'","b","r","o","u:","k","n"]) #BBC english
#x.synthesise(["k","a:","i:","n","d","'","a","'","b","r","o","u:","'","n"]) #Southern English - Kinda bro'en 

#http://ipa-reader.xyz/?text=its kɑind of broʊkn&voice=Emma
#http://ipa-reader.xyz/?text=s kaj:nda bro en&voice=Emma 


#EG3 SHUT UP
"ʃɑtɑp" #BBC english
"ʃa ɑp"  #London Cockney 
"ʃorɑp"  #Northern English

#x.synthesise(["ʃ","ɑ","t","'","a","p"]) #BBC english
#x.synthesise(["ʃ","a:","ɑ","p"]) #London Cockney 

#http://ipa-reader.xyz/?text=ʃɑtɑp&voice=Emma
#http://ipa-reader.xyz/?text=ʃa ɑp&voice=Emma
#http://ipa-reader.xyz/?text=ʃorɑp&voice=Emma


#EG4 BRITISH
"bɹ'ʃ" #Cockney English
"britiʃ" #South african
x.synthesise(["b","ɹ","i","'","ʃ"]) 
x.synthesise(["b","r","i","t","i","ʃ"]) 