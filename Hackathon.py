#Plan 
"""
-need to get user input
-need some sort of dictionary DONE
-need conditionals
-maybe a user greeting DONE
-confimation that user wants to go with password
-make sure that user wants a certian case
-added date and time DONE
"""


#time/date
import random
from datetime import datetime
presentime = datetime.now()
print(presentime)

#\/\/\/ COME BACK TO \/\/\/

choice = ""
choice2 = ""
passwords = []
password = ""
generator = ""
userpassword = ""

#Menu


print("\n")
print("\nWelcome to The Offical Password Manager!! ")
print("                     ,----.")
print(".                   ( WOW! )                        .-.")
print("                     `----' _                        \ \ ")
print("                         (_)                         \ \ ")
print("                             O                       | |")
print("                               o                     | |")
print("                                 . /\---/\   _,---._ | |")
print("                                  /^   ^  \,'       `. ;")
print("       (\-.                      ( O   O   )           ;")
print("       / _`>   .---------.        `.=o=__,'              \ ")
print("  _)   |  _)=  |'-------'|               /                 \ ")
print(" (     / _/    |O   O   o|              /  _ )   ,' `-. `-.  \ ") 
print("  `__.(___)_   | o O . o |             / ,' /  ,'      \ \ \  \ ")
print("               `---------'            / /  / ,'         \ \ \  \ ")
print("                                     / /  / ,'          (,_)(,_)")
print("                                   (,;)  (,,)")      
print("\n") 
#Main choice menu

while choice != "exit":
  print("\n Generator \n Manager \n Exit")
  choice = choice.lower()
  choice = input(": ")

#Generator
  
  if choice == "generator":   
    #215 words in the list
      password=[]
      words= ['people', 'history', 'way', 'art', 'world', 'information', 'map', 'two', 'family','government','health','system', 'computer', 'meat', 'year', 'thanks', 'music', 'person', 'reading', 'method', 'data', 'food', 'understanding', 'theory', 'law', 'bird', 'literature', 'problem', 'software', 'control', 'knowledge', 'power', 'ability', 'economics', 'love', 'internet', 'television', 'science', 'library', 'nature', 'fact', 'product', 'idea', 'temperature', 'investment', 'area', 'society', 'activity', 'story','industry','media','thing','oven','community','definition','safety','quality','development','language','management','player','variety','video','week','security','country','exam','movie','organization','equipment','physics','analysis','policy','series', 'thought','basis','boyfriend','direction', 'strategy', 'technology', 'army', 'camera','freedom','paper','environment','child','instance','month', 'truth','marketing','university', 'audience', 'fishing','growth', 'income', 'marriage','user','combination','failure','meaning', 'medicine','philosophy','teacher','communication','night','chemistry', 'disease', 'disk', 'energy', 'nation', 'road', 'role', 'soup', 'advertising', 'location', 'success', 'addition', 'apartment','education','math','moment','painting','politics','attention','decision','event','property','shopping','student','wood','competition','distribution','entertainment','office','population','president','unit','category','cigarette','context','introduction','opportunity','performance','driver', 'flight', 'magazine','newspaper', 'relationship','teaching','cell','dealer','debate','finding','lake','member','message','phone','scene','appearance','association','concept','customer','death','discussion','housing','inflation','insurance','mood','woman','advice','blood','effort','expression','importance','opinion', 'payment', 'reality', 'responsibility', 'situation', 'skill', 'statement','wealth','application','editor','efficiency','excitement','extent','feedback','guitar','homework','leader','mom','outcome','permission','presentation','promotion','reflection','refrigerator','resolution','revenue','session','singer','tennis','basket','bonus','smile','spell','stretch','stupid','tear','temporary','tomorrow','wake','wrap','yesterday']
      #under here
      choice = ""
      random_index = random.randint(0,len(words)-1)
      #print(words[random_index])
      
      
      password.append(words[random_index])
      
      for i in range(0,5):
       n = random.randint(1,1500)
      password.append(n)

      import random
      choice = ""
      random_index = random.randint(0,len(words)-1)
      #print(words[random_index])

      password.append(words[random_index])
      
      for i in range(0,5):
       n = random.randint(1,1500)
      password.append(n)
      #print(password)
      
      finalpassword = ("".join(map(str,password)))
      print("Your new password is " +finalpassword)
      passwords.append(finalpassword)
    
      finalpass=[]
      finalpass.append("".join(map(str,password)))
        

#Password manager
      
  elif choice == "manager":
    choice2 = input("\n Add \n Retrieve \n Exit \n:")
    choice = choice.lower()
          
    if choice2 == "add":
      userpassword = input("Enter password:")
      passwords.append(userpassword)
      print(passwords)
      choice2 = "exit"

      #Retrieving passwords
            
    if choice2 == "retrieve":
      print(passwords)
      choice2 = "exit"
        

#Goodbye/Thank you message with exit function 
print("Thank you for using The Offical Password Manager®")
print("\n")
print("HAVE A NICE DAY!!")
exit()
  



