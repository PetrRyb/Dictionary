
robot ={ 
 "R2D2":"opravář", 
}
hodnota = input("opravář") 
klíč = input("Jaké je jméno robota?")
for klíč in robot.items:
     print(f"{hodnota}, {robot[hodnota]}")  
else:
    Odpověď = input(" Robot není v seznamu chcete ho přidat do seznamu, jakožto nového robota?")

if Odpověď == "ano":
    klíč = input("Zadejte název robota")
for klíč in robot: 
    print(robot)    

 while True:
    klíčové_slovo = input( "Napište "konec" pokavaď už nechcete přidávat robota či odpovídat na otázku ohledně jeho jména"):
