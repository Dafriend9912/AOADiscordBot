'''
Created on Nov 10, 2019
for element in range(0, len(string_name)): 
    print(string_name[element]) 
@author: pikac
'''
import os
import sqlite3
import discord
import random
from attr import attr


token = "NjQyOTY0NDc5NDc0NDAxMjkw.Xce1sg.LScQs6bASbGXV_iBGI8KoE2Es_I"

client = discord.Client()
conn = None


Phase = ""

Update = ""

Not_VisitedAllies = []

VisitedAllies = []

Not_VisitedEnemies = []

VisitedEnemies = []

@client.event
async def on_ready():
    
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
        global Phase
        global Update
        global Not_VisitedAllies
        global Not_VisitedEnemies
        global VisitedAllies
        global VisitedEnemies
        try:
            conn = sqlite3.connect("CharacterDB.db")
            print(sqlite3.version)
        finally:
            if not conn:
                conn.close()
        
        cursor = conn.cursor()
        mess = message.content
        if message.author == client.user:
            return
        if message.content == '!roll d' + mess[7:]:
            if '+' not in mess:
                response = "```" + "You rolled a " + str(random.randint(1,int(mess[7:]))) + "```"
                await message.channel.send(response)
            elif '+' in mess:
                num1 = ""
                num2 = ""
                aaa = False
                for char in mess: 
                    if char.isdigit() and not aaa:
                        num1 += char + ""
                    elif char == '+':
                        aaa = True
                    elif char.isdigit() and aaa:
                        num2 += char + ""
                num3 = random.randint(1,int(num1))
                response = "```" + "You rolled a " + str(num3) + "\nSo your total is " + str(num3 + int(num2)) +"```"
                await message.channel.send(response)
                
        elif message.content == "!crit":
            num = random.randint(1,20)
            if num == 20:
                await message.channel.send("ITS A CRIT!!!")
            else: 
                await message.channel.send("Not a crit :(")
                
        elif message.content == "!crest":
            num = random.randint(1,5)
            if num == 5:
                await message.channel.send("THE CREST ACTIVATES")
            else: 
                await message.channel.send("Crest doesn't activate")
        
        elif message.content == "!AddCharacter"+ mess[13:]:
            count = 0
            Name = ""
            In = ""
            Health = ""
            Str = ""
            Mag = ""
            Def = ""
            Res = ""
            Spd = ""
            Skill = ""
            Luck = ""
            Class = ""
            Crest = ""
            Sword = ""
            Lance = ""
            Bow = ""
            Axe = ""
            Brawl = ""
            Reason = ""
            Faith = ""
            for char in mess: 
                    if char == ' ':
                        count += 1
                    elif count == 1:
                        Name += char + ""
                    elif count == 2:
                        Health += char + ""
                    elif count == 3:
                        Str += char + ""
                    elif count == 4:
                        Mag += char + ""
                    elif count == 5:
                        Def += char + ""
                    elif count == 6:
                        Res += char + ""
                    elif count == 7:
                        Spd += char + ""
                    elif count == 8:
                        Skill += char + ""
                    elif count == 9:
                        Luck += char + ""
                    elif count == 10:
                        Class += char + ""
                    elif count == 11 :
                        Crest += char + ""
                    elif count == 12:
                        Sword += char + ""
                    elif count == 13:
                        Lance += char + ""
                    elif count == 14:
                        Bow += char + ""
                    elif count == 15:
                        Axe += char + ""
                    elif count == 16:
                        Brawl += char + ""
                    elif count == 17:
                        Reason += char + ""
                    elif count == 18:
                        Faith += char + ""
            for row in cursor.execute("SELECT Name FROM Character WHERE Name = ?",[Name]):
                In = row[0]
            if In == Name:
                await message.channel.send("```" + Name +" is already in the Database please use !updatecharacter to change the character's stats```")
            else:
                cursor.execute('''INSERT INTO Character(NAME, HC, HT, STR, MAG, DEF, RES, SPD, SKILL, LUCK, CLASS, CREST, SWORD, LANCE, BOW, AXE, BRAWL, REASON, FAITH, Level, EXP) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (Name, Health, Health, Str, Mag, Def, Res, Spd, Skill, Luck, Class, Crest, Sword, Lance, Bow, Axe, Brawl, Reason, Faith, 1, 0))
                cursor.execute('''INSERT INTO Chargold(NAME, MONEY, Item1, Item2, Item3, Item4, Item5, Item1uses, Item2uses, Item3uses, Item4uses, Item5uses) 
                            VALUES(?,0,"x","x","x","x","x",0,0,0,0,0)''', [Name])
                await message.channel.send("```" + Name +" has been added```")
            conn.commit()
        elif message.content == "!fight" + mess[6:]:
            count = 0
            character1 = ""
            character2 = ""
            Class = ""
            att = ""
            str1 = 0
            defense = 0
            mag = 0
            res = 0
            health = 0
            healthx = 0
            dam = 0
            luck1 = 0
            luck2 = 0
            skl = 0
            spd = 0
            weapon = ""
            bonus = 0
            crit = False
            crest = False
            crest1 = False
            cresttype = ""
            cresttype1 = ""
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                    
                elif count == 1:
                    character1 += char + ""
                    
                elif count == 2:
                    character2 += char + ""
                    
                elif count == 3:
                    att += char + ""
                    
            for row in cursor.execute("SELECT STR,Name FROM Character WHERE Name = ?",[character1]):
                str1 = row[0]
                
            for row in cursor.execute("SELECT MAG, Name FROM Character WHERE Name = ?",[character1]):
                mag = row[0]
                
            for row in cursor.execute("SELECT DEF, Name FROM Character WHERE Name = ?",[character2]):
                defense = row[0]
                
            for row in cursor.execute("SELECT RES, Name FROM Character WHERE Name = ?",[character2]):
                res = row[0]
                
            for row in cursor.execute("SELECT HC, Name FROM Character WHERE Name = ?", [character2]):
                health = row[0]
             
            for row in cursor.execute("SELECT HC, Name FROM Character WHERE Name = ?", [character1]):
                healthx = row[0]
                
            for row in cursor.execute("SELECT CLASS, Name FROM Character WHERE Name = ?", [character1]):
                Class = row[0]
                
            for row in cursor.execute("SELECT LUCK, Name FROM Character WHERE Name = ?", [character1]):
                luck1 = row[0]
                
            for row in cursor.execute("SELECT LUCK, Name FROM Character WHERE Name = ?", [character2]):
                luck2 = row[0]
                
            for row in cursor.execute("SELECT SKILL, Name FROM Character WHERE Name = ?", [character1]):
                skl = row[0]
                
            for row in cursor.execute("SELECT SPD, Name FROM Character WHERE Name = ?", [character2]):
                spd = row[0]
                
            for row in cursor.execute("SELECT CREST, Name FROM Character WHERE Name = ?", [character2]):
                cresttype1 = row[0]
                
            for row in cursor.execute("SELECT CREST, Name FROM Character WHERE Name = ?", [character1]):
                cresttype = row[0]    
                
            if(att == "Sword"):
                for row in cursor.execute("SELECT SWORD, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Lance"):
                for row in cursor.execute("SELECT LANCE, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Bow"):
                for row in cursor.execute("SELECT BOW, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Axe"):
                for row in cursor.execute("SELECT AXE, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Brawl"):
                for row in cursor.execute("SELECT BRAWL, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Reason"):
                for row in cursor.execute("SELECT REASON, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
                    
            elif(att == "Faith"):
                for row in cursor.execute("SELECT FAITH, Name FROM Character WHERE Name = ?", [character1]):
                    weapon = row[0]
            
            if(weapon == "S+"):
                bonus = 30
                
            elif(weapon == "S"):
                bonus = 25
                
            elif(weapon == "A+" or weapon == "A"):
                bonus = 20
                
            elif(weapon == "B" or weapon == "B+"):
                bonus = 15
                
            elif(weapon == "C+" or weapon == "C"):
                bonus = 10
                
            elif(weapon == "D" or weapon == "D+"):
                bonus = 5
              
            hitrate = (skl * .8) + (luck1 * .5) + bonus + 100
            dodgerate = (spd) + (luck2 * .5)
            rannum = random.randint(1,100)
            hit = hitrate - dodgerate
            if(rannum < hit):
                if (att == "Reason" or att == "Faith"):
                    dam = int(mag) - int(res)
                    
                else:
                    dam = str1 - defense
                    
                if dam <= 0:
                    dam = 1
             
                if(Class == "Noble"):
                    num1 = random.randint(1,100)
                    if(num1 <= 22):
                        crest = True
                        
                if cresttype1 == "C":
                    num1 = random.randint(1,100)
                    if(num1 <= 22):
                        crest1 = True
                        
                if crest and cresttype == "A" and not crest1:
                    dam += 5
                
                    
                elif not crest and crest1:
                    damx = round(dam/5)
                    dam -= damx
                
                elif crest and cresttype == "A" and crest1:
                    dam += 5
                    damx = round(dam/5)
                    dam -= damx 
                
                lucktest = (round(luck1 *1.2) + 5) - luck2
                rannum2 = random.randint(1,100)
                print(rannum2)
                if(rannum2 < lucktest):
                    dam = dam * 3
                    crit = True
                    
                if crest and cresttype == "B" and crest1:
                    damx = round(dam/5)
                    dam -= damx
                    healthx = healthx + round(dam/10) 
                    
                elif crest and cresttype == "B" and not crest1:
                    healthx = healthx + round(dam/10)
                    
                health = int(health) - int(dam)
                
                cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[health, character2])
                
                        
                if(int(health) <= 0 and not crest and not crit and not crest1):
                    await message.channel.send("```" + str(character2) +" takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and crest and not crit and crest1):
                    await message.channel.send("```" + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and crest and not crit and cresttype == "A" and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage! "+ str(character2) +" takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and crest and not crit and cresttype == "A" and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage! "+ str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and crest and not crit and cresttype == "B" and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt!" + str(character2) +" takes " + str(dam) + " damage and has been knocked out!\n" + str(character1) + "now has " + str(healthx) + "health!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])
                    
                elif(int(health) <= 0 and crest and not crit and cresttype == "B" and crest1):                    
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt!" + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!\n" + str(character1) + "now has " + str(healthx) + "health!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])
                    
                elif(int(health) <= 0 and crest and cresttype == "A" and crit and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage and lands a critical hit! "+ str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                
                elif(int(health) <= 0 and crest and cresttype == "A" and crit and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage and lands a critical hit! "+ str(character2) +" takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                
                elif(int(health) <= 0 and crest and cresttype == "B" and crit and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt and lands a critical hit! "+ str(character2) +" takes " + str(dam) + " damage and has been knocked out!\n" + str(character1) + "now has " + str(healthx) + "health!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and crest and cresttype == "B" and crit and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt and lands a critical hit! "+ str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!\n" + str(character1) + "now has " + str(healthx) + "health!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and not crest and crit and not crest1):
                    await message.channel.send("```" + str(character1) + " lands a critical hit! "+ str(character2) +" takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(int(health) <= 0 and not crest and crit and crest1):
                    await message.channel.send("```" + str(character1) + " lands a critical hit! "+ str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage and has been knocked out!```")
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[character2])
                    
                elif(crest and crit and cresttype == "A" and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage and lands a critical hit! " + str(character2) +" takes " + str(dam) + " + what effect " + str(character1) +"'s crest has! They have " + str(health) + " health left!```")   
                     
                elif(crest and crit and cresttype == "A" and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage and lands a critical hit! " + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage. They have " + str(health) + " health left!```")   
                     
                elif(crest and crit and cresttype == "B" and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt and lands a critical hit! " + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " damage. They have " + str(health) + " health left!\n" + str(character1) + " now has " + str(healthx) + " health!```")        
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])
                    
                elif(crest and crit and cresttype == "B" and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt and lands a critical hit! " + str(character2) +" takes " + str(dam) + " damage. They have " + str(health) + " health left!\n" + str(character1) + " now has " + str(healthx) + " health!```")        
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])    
                     
                elif(not crest and crit and not crest1):
                    await message.channel.send("```" + str(character1) + " lands a critical hit! " + str(character2) +" takes " + str(dam) + " they have " + str(health) + " health left!```")
                    
                elif(not crest and crit and crest1):
                    await message.channel.send("```" + str(character1) + " lands a critical hit! " + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + " they have " + str(health) + " health left!```")    
                    
                elif(crest and cresttype == "A" and not crit and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage! " + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + "! They have " + str(health) + " health left!```")
                  
                elif(crest and cresttype == "A" and not crit and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and deals 5 extra damage! " + str(character2) +" takes " + str(dam) + "! They have " + str(health) + " health left```")  
                
                elif(crest and cresttype == "B" and not crit and crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt! " + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + "! They have " + str(health) + " health left!\n" + str(character1) + " now has " + str(healthx) + " health!```")
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])
                    
                elif(crest and cresttype == "B" and not crit and not crest1):
                    await message.channel.send("```" + str(character1) + "'s crest activates and heals for 10% of the damage dealt! " + str(character2) +" takes " + str(dam) + "! They have " + str(health) + " health left!\n" + str(character1) + " now has " + str(healthx) + " health!```")
                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?", [healthx, character1])
                    
                elif(not crest and not crit and crest1):
                    await message.channel.send("```" + str(character2) +"'s crest activates and reduces damage by 20% but still takes " + str(dam) + "! They have " + str(health) + " health left!```")    
                    
                else:
                    await message.channel.send("```" + str(character2) +" takes " + str(dam) + " they have " + str(health) + " health left```")
                    
            else:
                await message.channel.send("```" + str(character1) +"'s attack missed!```")
        
        elif message.content == "!deletecharacter" + mess[16:]:
            name = ""
            count = 0
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                    
                elif count == 1:
                    name += char + ""
            
            cursor.execute("DELETE from Character where NAME = ?", [name])
            cursor.execute("DELETE from Chargold where NAME = ?", [name])
            await message.channel.send("```" + str(name) + " has been deleted!```")
        
        elif message.content == "!updatecharacter" + mess[16:]:
            count = 0
            Name = ""
            Health = ""
            Str = ""
            Mag = ""
            Def = ""
            Res = ""
            Spd = ""
            Skill = ""
            Luck = ""
            Sword = ""
            Lance = ""
            Bow = ""
            Axe = ""
            Brawl = ""
            Reason = ""
            Faith = ""
            for char in mess: 
                    if char == ' ':
                        count += 1
                    elif count == 1:
                        Name += char + ""
                    elif count == 2:
                        Health += char + ""
                    elif count == 3:
                        Str += char + ""
                    elif count == 4:
                        Mag += char + ""
                    elif count == 5:
                        Def += char + ""
                    elif count == 6:
                        Res += char + ""
                    elif count == 7:
                        Spd += char + ""
                    elif count == 8:
                        Skill += char + ""
                    elif count == 9:
                        Luck += char + ""
                    elif count == 10:
                        Sword += char + ""
                    elif count == 11:
                        Lance += char + ""
                    elif count == 12:
                        Bow += char + ""
                    elif count == 13:
                        Axe += char + ""
                    elif count == 14:
                        Brawl += char + ""
                    elif count == 15:
                        Reason += char + ""
                    elif count == 16:
                        Faith += char + ""
            cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health, Name])
            cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str, Name])
            cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag, Name])
            cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def, Name])
            cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res, Name])
            cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd, Name])
            cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill, Name])
            cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck, Name])
            cursor.execute("UPDATE Character SET SWORD = ? WHERE Name = ?",[Sword, Name])
            cursor.execute("UPDATE Character SET LANCE = ? WHERE Name = ?",[Lance, Name])
            cursor.execute("UPDATE Character SET BOW = ? WHERE Name = ?",[Bow, Name])
            cursor.execute("UPDATE Character SET AXE = ? WHERE Name = ?",[Axe, Name])
            cursor.execute("UPDATE Character SET BRAWL = ? WHERE Name = ?",[Brawl, Name])
            cursor.execute("UPDATE Character SET REASON = ? WHERE Name = ?",[Reason, Name])
            cursor.execute("UPDATE Character SET FAITH = ? WHERE Name = ?",[Faith, Name])
            await message.channel.send("```" + str(Name) +" has been updated!```")
            
        elif message.content == "!heal" + mess[5:]:
            count = 0
            Name = ""
            amount = ""
            currhealth = 0
            healamount = 0
            maxhealth = 0
            currdam = 0
            for char in mess: 
                    if char == ' ':
                        count += 1
                    elif count == 1:
                        Name += char + ""
                    elif count == 2:
                        amount += char + ""
                        
            for row in cursor.execute("SELECT HC, Name FROM Character WHERE Name = ?", [Name]):
                currhealth = row[0]
            
            for row in cursor.execute("SELECT HT, Name FROM Character WHERE Name = ?", [Name]):
                maxhealth = row[0]

            if Name != "":
                if amount != "":                         
                    currdam = currhealth - maxhealth
                    healamount = currhealth + int(amount)
            
                    if currdam >= 0:
                        currdam = 0
                
                    if int(amount) > abs(currdam):
                        amount = abs(currdam)
                    else:
                        amount = amount
            
                    if healamount > maxhealth:
                        healamount = maxhealth

                    cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[healamount,Name])
                    await message.channel.send("```" + str(Name) +" has been healed for " + str(amount) + " health!```")
                else:
                    cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[Name])
                    await message.channel.send("```" + str(Name) +" has been restored to full health!```")
            else:
                cursor.execute("UPDATE Character SET HC = HT")
                await message.channel.send("```All characters have been restored to full health!```")
        elif message.content == "!cheal" + mess[6:]:
            count = 0
            Name = ""
            Name1 = ""
            healtype = ""
            Res = 0
            hc = 0
            ht = 0
            heal = 0
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     Name1 += char + ""
                elif count == 3:
                    healtype += char + ""
                
            for row in cursor.execute("SELECT HC, Name FROM Character WHERE Name = ?", [Name1]):
                hc = row[0]
            for row in cursor.execute("SELECT HT, Name FROM Character WHERE Name = ?",[Name1]):
                ht = row[0]
            for row in cursor.execute("SELECT MAG, Name FROM Character WHERE Name = ?",[Name]):
                Res = row[0]
            print(healtype)
            if healtype == "Physic":
                
                heal = int(Res/2)
                hc = hc + int(Res/2)
            else:
                heal = Res
                hc += Res
            if hc >= ht:
                cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[Name1])
                await message.channel.send("```" + str(Name) + " has healed "+ str(Name1) +" to full health!```")
            else: 
                cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[hc, Name1])
                await message.channel.send("```" + str(Name) + " has healed "+ str(heal) + " health to " + str(Name1) +"!```")
        
        elif message.content == "!fuckyou":
            await message.channel.send("```No fuck you!```")
        
        elif message.content == "!pay" + mess[4:]:
            count = 0
            Name = ""
            moneyc = 0
            monz = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     monz += char + ""
            for row in cursor.execute("SELECT MONEY, Name FROM Chargold WHERE Name = ?",[Name]):
                moneyc = row[0]
            moneyc += int(monz)
            cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneyc, Name])
            await message.channel.send("```" + str(Name) + " has earned "+ str(monz) + " gold! \nThey now have " + str(moneyc) + " gold in total!```")
                
        elif message.content == "!marketbuy" + mess[10:]:
            count = 0
            Name = ""
            Item = ""
            Itemval = ""
            Itemuses = ""
            money = ""
            monnum = 0
            Itemvalnum = 0
            moneya = 0
            Itemslot1 = ""
            Itemslot2 =""
            Itemslot3 = ""
            Itemslot4 = ""
            Itemslot5 = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     Item += char + ""
            for row in cursor.execute("SELECT MONEY, Name FROM Chargold WHERE Name = ?",[Name]):
                money = row[0]
            for row in cursor.execute("SELECT Item1, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot1 = row[0]
            for row in cursor.execute("SELECT Item2, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot2 = row[0]
            for row in cursor.execute("SELECT Item3, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot3 = row[0]
            for row in cursor.execute("SELECT Item4, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot4 = row[0]
            for row in cursor.execute("SELECT Item5, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot5 = row[0]
            for row in cursor.execute("SELECT VALUE, ITEM FROM Market WHERE ITEM = ?",[Item]):
                Itemval = row[0]
            for row in cursor.execute("SELECT USES, ITEM FROM Market WHERE ITEM = ?",[Item]):
                Itemuses = row[0]
            monnum = int(money)
            Itemvalnum = Itemval
            if monnum >= int(Itemvalnum):
                moneya = monnum - int(Itemvalnum)
                if int(Itemuses) >= 1:
                    if Itemslot1 == "x":
                        cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                        cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",[Item, Name])
                        cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[Itemuses, Name])
                        await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! \n" + str(Item) + " has been added to the first slot in their inventory!```")
                    elif Itemslot2 == "x":
                        cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                        cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",[Item, Name])
                        cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[Itemuses, Name])
                        await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! \n" + str(Item) + " has been added to the second slot in their inventory!```")
                    elif Itemslot3 == "x":
                        cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                        cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",[Item, Name])
                        cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[Itemuses, Name])
                        await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! \n" + str(Item) + " has been added to the third slot in their inventory!```")
                    elif Itemslot4 == "x":
                        cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                        cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",[Item, Name])
                        cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[Itemuses, Name])
                        await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! \n" + str(Item) + " has been added to the fourth slot in their inventory!```")
                    elif Itemslot5 == "x":
                        cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                        cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",[Item, Name])
                        cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[Itemuses, Name])
                        await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! \n" + str(Item) + " has been added to the fifth slot in their inventory!```")
                    else:
                        await message.channel.send("```" + str(Name) + " does not have any space the this item!```")
                else:
                    cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneya, Name])
                    await message.channel.send("```" + str(Name) + " uses "+ str(Itemval) + " gold to buy " + str(Item) + " they have " + str(moneya) + " left! They can use this at anytime!```")
                    if Item == "LevelUpPotion":
                       Level = ""
                       for row in cursor.execute("SELECT Level FROM Character WHERE Name = ?",[Name]):
                            Level = row[0]
            
                       Level = Level + 1
                       await message.channel.send("```" + str(Name) + " has leveled up! They are now level " + str(Level) + "!```")
                       cursor.execute("UPDATE Character SET Level = ? WHERE Name = ?",[Level , Name])
                       
            else:
                await message.channel.send("```" + str(Name) + " does not have enough money the this item!```")
        
        elif message.content == "!use" + mess[4:]:
            count = 0
            Name = ""
            slot = ""
            uses = ""
            usesleft = ""
            Item = ""
            Health = ""
            Healthcur = ""
            Healthmax = ""
            
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     slot += char + ""
            for row in cursor.execute("SELECT HC, Name FROM Character WHERE Name = ?",[Name]):
                    Healthcur = row[0]
            for row in cursor.execute("SELECT HT, Name FROM Character WHERE Name = ?",[Name]):
                    Healthmax = row[0]
            if slot == "1":
                for row in cursor.execute("SELECT Item1, Name FROM Chargold WHERE Name = ?",[Name]):
                    Item = row[0]
                for row in cursor.execute("SELECT Item1uses, Name FROM Chargold WHERE Name = ?",[Name]):
                    uses = row[0]
            elif slot == "2":
                for row in cursor.execute("SELECT Item2, Name FROM Chargold WHERE Name = ?",[Name]):
                    Item = row[0]
                for row in cursor.execute("SELECT Item2uses, Name FROM Chargold WHERE Name = ?",[Name]):
                    uses = row[0]
            elif slot == "3":
                for row in cursor.execute("SELECT Item3, Name FROM Chargold WHERE Name = ?",[Name]):
                    Item = row[0]
                for row in cursor.execute("SELECT Item3uses, Name FROM Chargold WHERE Name = ?",[Name]):
                    uses = row[0]
            elif slot == "4":
                for row in cursor.execute("SELECT Item4, Name FROM Chargold WHERE Name = ?",[Name]):
                    Item = row[0]
                for row in cursor.execute("SELECT Item4uses, Name FROM Chargold WHERE Name = ?",[Name]):
                    uses = row[0]
            elif slot == "5":
                for row in cursor.execute("SELECT Item5, Name FROM Chargold WHERE Name = ?",[Name]):
                    Item = row[0]
                for row in cursor.execute("SELECT Item5uses, Name FROM Chargold WHERE Name = ?",[Name]):
                    uses = row[0]
            usesleft = int(uses) - 1
            if Item != "x":
                if usesleft > 0:
                    if slot == "1":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP " + str(usesleft) + " it uses left!```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                    Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP " + str(usesleft) + " it uses left!```")
                    elif slot == "2":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP " + str(usesleft) + " it uses left!```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP " + str(usesleft) + " it uses left!```")
                    elif slot == "3":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP " + str(usesleft) + " it uses left!```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP " + str(usesleft) + " it uses left!```")
                    elif slot == "4":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP " + str(usesleft) + " it uses left!```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP " + str(usesleft) + " it uses left!```")
                    elif slot == "5":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP " + str(usesleft) + " it uses left!```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[usesleft, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP " + str(usesleft) + " it uses left!```")
                            
                    
                else:
                    if slot == "1":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```") 
                        elif Item == "ReviveCrystal":
                            cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and gets back up! But the crystal breaks... The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Elixar":
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Healthmax, Name])
                            cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores all their health! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")     
                    elif slot == "2":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```") 
                        elif Item == "ReviveCrystal":
                            cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and gets back up! But the crystal breaks... The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Elixar":
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Healthmax, Name])
                            cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores all their health! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")     
                    elif slot == "3":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```") 
                        elif Item == "ReviveCrystal":
                            cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and gets back up! But the crystal breaks... The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Elixar":
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Healthmax, Name])
                            cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores all their health! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")     
                    elif slot == "4":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```") 
                        elif Item == "ReviveCrystal":
                            cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and gets back up! But the crystal breaks... The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Elixar":
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Healthmax, Name])
                            cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores all their health! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")     
                    elif slot == "5":
                        if Item == "Vulnerary":
                            Health =int(Healthcur) + 10
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 10 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Concoction":
                            Health =int(Healthcur) + 40
                            if Health > Healthmax:
                                Health = Healthmax
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Health, Name])
                            cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores 40 HP! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```") 
                        elif Item == "ReviveCrystal":
                            cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and gets back up! But the crystal breaks... The " + str(slot) +" slot in their inventory is open again.```")
                        elif Item == "Elixar":
                            cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[Healthmax, Name])
                            cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",["x", Name])
                            cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[0, Name])
                            await message.channel.send("```" + str(Name) + " uses the " + str(Item) + " and restores all their health! But the item has been consumed...The " + str(slot) +" slot in their inventory is open again.```")     
            else:
                await message.channel.send("```The " + str(slot) + " slot in their inventory is empty. Please try again.```")
        elif message.content == '!inventory' + mess[10:]:
            count = 0
            Name = ""
            Item1 = ""
            Item2 =""
            Item3 = ""
            Item4 = ""
            Item5 = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""  
            for row in cursor.execute("SELECT Item1, Name FROM Chargold WHERE Name = ?",[Name]):
                Item1 = row[0]
            for row in cursor.execute("SELECT Item2, Name FROM Chargold WHERE Name = ?",[Name]):
                Item2 = row[0]
            for row in cursor.execute("SELECT Item3, Name FROM Chargold WHERE Name = ?",[Name]):
                Item3 = row[0]
            for row in cursor.execute("SELECT Item4, Name FROM Chargold WHERE Name = ?",[Name]):
                Item4 = row[0]
            for row in cursor.execute("SELECT Item5, Name FROM Chargold WHERE Name = ?",[Name]):
                Item5 = row[0]
            if Item1 == "x":
                Item1 = "No Item"
            if Item2 == "x":
                Item2 = "No Item"
            if Item3 == "x":
                Item3 = "No Item"
            if Item4 == "x":
                Item4 = "No Item"
            if Item5 == "x":
                Item5 = "No Item"
            await message.channel.send("```" + str(Name) + "'s Inventory \n 1. " + str(Item1) + "\n 2. " + str(Item2) + "\n 3. " + str(Item3) + "\n 4. " + str(Item4) + "\n 5. " + str(Item5) + "```")
            
        elif message.content == '!money' + mess[6:]:
            count = 0
            Name = ""
            Money = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + "" 
            for row in cursor.execute("SELECT MONEY, Name FROM Chargold WHERE Name = ?",[Name]):
                Money = row[0]
            await message.channel.send("```" + str(Name) + " has " + str(Money) + " gold!```")
        
        elif message.content == "!pairup" + mess[7:]:
            count = 0
            Name = ""
            Name1 = ""
            NameT = ""
            In = ""
            Health = ""
            Health1 = ""
            HealthT = ""
            Str = ""
            Str1 = ""
            StrT = ""
            Mag = ""
            Mag1 = ""
            MagT = ""
            Def = ""
            Def1 = ""
            DefT = ""
            Res = ""
            Res1 = ""
            ResT = ""
            Spd = ""
            Spd1 = ""
            SpdT = ""
            Skill = ""
            Skill1 = ""
            SkillT = ""
            Luck = ""
            Luck1 = ""
            LuckT = ""
            Class = ""
            Class1 = ""
            ClassT = ""
            Sword = ""
            Sword1 = ""
            SwordT = ""
            Lance = ""
            Lance1 = ""
            LanceT = ""
            Bow = ""
            Bow1 = ""
            BowT = ""
            Axe = ""
            Axe1 = ""
            AxeT = ""
            Brawl = ""
            Brawl1 = ""
            BrawlT = ""
            Reason = ""
            Reason1 = ""
            ReasonT = ""
            Faith = ""
            Faith1 = ""
            FaithT = ""
            crit = False
            crest = False
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                    
                elif count == 1:
                    Name += char + ""
                    
                elif count == 2:
                    Name1 += char + ""
            for row in cursor.execute("SELECT Name FROM Character WHERE Name = ?",[Name]):
                In = row[0]
            In += "+"
            for row in cursor.execute("SELECT Name FROM Character WHERE Name = ?",[Name1]):
                In += row[0]
                
            NameT = Name + "+" + Name1
            
            if In == Name:
                await message.channel.send("```This pairup is already in the Database please use !updatecharacter to change the character's stats```")
            else:
                for row in cursor.execute("SELECT HT,Name FROM Character WHERE Name = ?",[Name]):
                    Health = row[0]
                
                for row in cursor.execute("SELECT HT,Name FROM Character WHERE Name = ?",[Name1]):
                    Health1 = row[0]        
                    
                for row in cursor.execute("SELECT STR,Name FROM Character WHERE Name = ?",[Name]):
                    Str = row[0]
                
                for row in cursor.execute("SELECT STR,Name FROM Character WHERE Name = ?",[Name1]):
                    Str1 = row[0]
                
                for row in cursor.execute("SELECT Mag,Name FROM Character WHERE Name = ?",[Name]):
                    Mag = row[0]
                
                for row in cursor.execute("SELECT Mag,Name FROM Character WHERE Name = ?",[Name1]):
                    Mag1 = row[0]       
             
                for row in cursor.execute("SELECT DEF,Name FROM Character WHERE Name = ?",[Name]):
                    Def = row[0]
                
                for row in cursor.execute("SELECT DEF,Name FROM Character WHERE Name = ?",[Name1]):
                    Def1 = row[0]
                
                for row in cursor.execute("SELECT RES,Name FROM Character WHERE Name = ?",[Name]):
                    Res = row[0]
                
                for row in cursor.execute("SELECT RES,Name FROM Character WHERE Name = ?",[Name1]):
                    Res1 = row[0] 
                
                for row in cursor.execute("SELECT SPD,Name FROM Character WHERE Name = ?",[Name]):
                    Spd = row[0]
                
                for row in cursor.execute("SELECT SPD,Name FROM Character WHERE Name = ?",[Name1]):
                    Spd1 = row[0]
                
                for row in cursor.execute("SELECT SKILL,Name FROM Character WHERE Name = ?",[Name]):
                    Skill = row[0]
                
                for row in cursor.execute("SELECT SKILL,Name FROM Character WHERE Name = ?",[Name1]):
                    Skill1 = row[0] 
            
                for row in cursor.execute("SELECT LUCK,Name FROM Character WHERE Name = ?",[Name]):
                    Luck = row[0]
                
                for row in cursor.execute("SELECT LUCK,Name FROM Character WHERE Name = ?",[Name1]):
                    Luck1 = row[0]
                
                for row in cursor.execute("SELECT CLASS,Name FROM Character WHERE Name = ?",[Name]):
                    Class = row[0]
                
                for row in cursor.execute("SELECT CLASS,Name FROM Character WHERE Name = ?",[Name1]):
                    Class1 = row[0]         
            
                for row in cursor.execute("SELECT SWORD,Name FROM Character WHERE Name = ?",[Name]):
                    Sword = row[0]
                
                for row in cursor.execute("SELECT SWORD,Name FROM Character WHERE Name = ?",[Name1]):
                    Sword1 = row[0]       
             
                for row in cursor.execute("SELECT LANCE,Name FROM Character WHERE Name = ?",[Name]):
                    Lance = row[0]
                
                for row in cursor.execute("SELECT LANCE,Name FROM Character WHERE Name = ?",[Name1]):
                    Lance1 = row[0]
                
                for row in cursor.execute("SELECT BOW,Name FROM Character WHERE Name = ?",[Name]):
                    Bow = row[0]
                
                for row in cursor.execute("SELECT BOW,Name FROM Character WHERE Name = ?",[Name1]):
                    Bow1 = row[0] 
                
                for row in cursor.execute("SELECT AXE,Name FROM Character WHERE Name = ?",[Name]):
                    Axe = row[0]
                
                for row in cursor.execute("SELECT AXE,Name FROM Character WHERE Name = ?",[Name1]):
                    Axe1 = row[0]
                
                for row in cursor.execute("SELECT BRAWL,Name FROM Character WHERE Name = ?",[Name]):
                    Brawl = row[0]
                
                for row in cursor.execute("SELECT BRAWL,Name FROM Character WHERE Name = ?",[Name1]):
                    Brawl1 = row[0] 
            
                for row in cursor.execute("SELECT REASON,Name FROM Character WHERE Name = ?",[Name]):
                    Reason = row[0]
                
                for row in cursor.execute("SELECT REASON,Name FROM Character WHERE Name = ?",[Name1]):
                    Reason1 = row[0]
                
                for row in cursor.execute("SELECT FAITH,Name FROM Character WHERE Name = ?",[Name]):
                    Faith = row[0]
                
                for row in cursor.execute("SELECT FAITH,Name FROM Character WHERE Name = ?",[Name1]):
                    Faith1 = row[0]         
                
                if int(Health) > int(Health1):
                    HealthT = Health
                else:
                    HealthT = Health1
                
                StrT = Str1 + Str
                
                MagT = Mag + Mag1

                if int(Def) > int(Def1):
                    DefT = Def
                else:
                    DefT = Def1
                
                if int(Res) > int(Res1):
                    ResT = Res
                else:
                    ResT = Res1
                
                if int(Spd) > int(Spd1):
                    SpdT = Spd
                else:
                    SpdT = Spd1
                
                if int(Skill) > int(Skill1):
                    SkillT = Skill
                else:
                    SkillT = Skill1    
                
                if int(Luck) > int(Luck1):
                    LuckT = Luck
                else:
                    LuckT = Luck1    
                
                if Class == "Noble" or Class1 == "Noble":
                    ClassT = "Noble"
                else:
                    ClassT = "Commoner"
                    
                if Sword == "S+":
                    Sword = "1" 
                elif Sword == "S":
                    Sword = "2"      
                elif Sword == "A+":
                    Sword = "3"
                elif Sword == "A":
                    Sword = "4"    
                elif Sword == "B+":
                    Sword = "5"        
                elif Sword == "B":
                    Sword = "6"      
                elif Sword == "C+":
                    Sword = "7"       
                elif Sword == "C":
                    Sword = "8"          
                elif Sword == "D+":
                    Sword = "9"
                elif Sword == "D":
                    Sword = "10"
                elif Sword == "E":
                    Sword = "11"         
                    
                if Sword1 == "S+":
                    Sword1 = "1" 
                elif Sword1 == "S":
                    Sword1 = "2"      
                elif Sword1 == "A+":
                    Sword1 = "3"
                elif Sword1 == "A":
                    Sword1 = "4"    
                elif Sword1 == "B+":
                    Sword1 = "5"        
                elif Sword1 == "B":
                    Sword1 = "6"      
                elif Sword1 == "C+":
                    Sword1 = "7"       
                elif Sword1 == "C":
                    Sword1 = "8"          
                elif Sword1 == "D+":
                    Sword1 = "9"
                elif Sword1 == "D":
                    Sword1 = "10"
                elif Sword1 == "E":
                    Sword1 = "11"    
                    
                if Lance == "S+":
                    Lance = "1" 
                elif Lance == "S":
                    Lance = "2"      
                elif Lance == "A+":
                    Lance = "3"
                elif Lance == "A":
                    Lance = "4"    
                elif Lance == "B+":
                    Lance = "5"        
                elif Lance == "B":
                    Lance = "6"      
                elif Lance == "C+":
                    Lance = "7"       
                elif Lance == "C":
                    Lance = "8"     
                elif Lance == "D+":
                    Lance = "9"
                elif Lance == "D":
                    Lance = "10"
                elif Lance == "E":
                    Lance = "11"       
                    
                if Lance1 == "S+":
                    Lance1 = "1" 
                elif Lance1 == "S":
                    Lance1 = "2"      
                elif Lance1 == "A+":
                    Lance1 = "3"
                elif Lance1 == "A":
                    Lance1 = "4"    
                elif Lance1 == "B+":
                    Lance1 = "5"        
                elif Lance1 == "B":
                    Lance1 = "6"      
                elif Lance1 == "C+":
                    Lance1 = "7"       
                elif Lance1 == "C":
                    Lance1 = "8"     
                elif Lance1 == "D+":
                    Lance1 = "9"
                elif Lance1 == "D":
                    Lance1 = "10"
                elif Lance1 == "E":
                    Lance1 = "11"      
                        
                if Bow == "S+":
                    Bow = "1" 
                elif Bow == "S":
                    Bow = "2"      
                elif Bow == "A+":
                    Bow = "3"
                elif Bow == "A":
                    Bow = "4"    
                elif Bow == "B+":
                    Bow = "5"        
                elif Bow == "B":
                    Bow = "6"      
                elif Bow == "C+":
                    Bow = "7"       
                elif Bow == "C":
                    Bow = "8"     
                elif Bow == "D+":
                    Bow = "9"
                elif Bow == "D":
                    Bow = "10"
                elif Bow == "E":
                    Bow = "11"        
                        
                if Bow1 == "S+":
                    Bow1 = "1" 
                elif Bow1 == "S":
                    Bow1 = "2"      
                elif Bow1 == "A+":
                    Bow1 = "3"
                elif Bow1 == "A":
                    Bow1 = "4"    
                elif Bow1 == "B+":
                    Bow1 = "5"        
                elif Bow1 == "B":
                    Bow1 = "6"      
                elif Bow1 == "C+":
                    Bow1 = "7"       
                elif Bow1 == "C":
                    Bow1 = "8"     
                elif Bow1 == "D+":
                    Bow1 = "9"
                elif Bow1 == "D":
                    Bow1 = "10"
                elif Bow1 == "E":
                    Bow1 = "11"        
                        
                if Axe == "S+":
                    Axe = "1" 
                elif Axe == "S":
                    Axe = "2"      
                elif Axe == "A+":
                    Axe = "3"
                elif Axe == "A":
                    Axe = "4"    
                elif Axe == "B+":
                    Axe = "5"        
                elif Axe == "B":
                    Axe = "6"      
                elif Axe == "C+":
                    Axe = "7"       
                elif Axe == "C":
                    Axe = "8"     
                elif Axe == "D+":
                    Axe = "9"
                elif Axe == "D":
                    Axe = "10"
                elif Axe == "E":
                    Axe = "11"          
                     
                if Axe1 == "S+":
                    Axe1 = "1" 
                elif Axe1 == "S":
                    Axe1 = "2"      
                elif Axe1 == "A+":
                    Axe1 = "3"
                elif Axe1 == "A":
                    Axe1 = "4"    
                elif Axe1 == "B+":
                    Axe1 = "5"        
                elif Axe1 == "B":
                    Axe1 = "6"      
                elif Axe1 == "C+":
                    Axe1 = "7"       
                elif Axe1 == "C":
                    Axe1 = "8"     
                elif Axe1 == "D+":
                    Axe1 = "9"
                elif Axe1 == "D":
                    Axe1 = "10"
                elif Axe1 == "E":
                    Axe1 = "11"        
                     
                if Brawl == "S+":
                    Brawl = "1" 
                elif Brawl == "S":
                    Brawl = "2"      
                elif Brawl == "A+":
                    Brawl = "3"
                elif Brawl == "A":
                    Brawl = "4"    
                elif Brawl == "B+":
                    Brawl = "5"        
                elif Brawl == "B":
                    Brawl = "6"      
                elif Brawl == "C+":
                    Brawl = "7"       
                elif Brawl == "C":
                    Brawl = "8"     
                elif Brawl == "D+":
                    Brawl = "9"
                elif Brawl == "D":
                    Brawl = "10"
                elif Brawl == "E":
                    Brawl = "11"     
                    
                if Brawl1 == "S+":
                    Brawl1 = "1" 
                elif Brawl1 == "S":
                    Brawl1 = "2"      
                elif Brawl1 == "A+":
                    Brawl1 = "3"
                elif Brawl1 == "A":
                    Brawl1 = "4"    
                elif Brawl1 == "B+":
                    Brawl1 = "5"        
                elif Brawl1 == "B":
                    Brawl1 = "6"      
                elif Brawl1 == "C+":
                    Brawl1 = "7"       
                elif Brawl1 == "C":
                    Brawl1 = "8"     
                elif Brawl1 == "D+":
                    Brawl1 = "9"
                elif Brawl1 == "D":
                    Brawl1 = "10"
                elif Brawl1 == "E":
                    Brawl1 = "11"     
                    
                if Reason == "S+":
                    Reason = "1" 
                elif Reason == "S":
                    Reason = "2"      
                elif Reason == "A+":
                    Reason = "3"
                elif Reason == "A":
                    Reason = "4"    
                elif Reason == "B+":
                    Reason = "5"        
                elif Reason == "B":
                    Reason = "6"      
                elif Reason == "C+":
                    Reason = "7"       
                elif Reason == "C":
                    Reason = "8"     
                elif Reason == "D+":
                    Reason = "9"
                elif Reason == "D":
                    Reason = "10"
                elif Reason == "E":
                    Reason = "11"       
                        
                if Reason1 == "S+":
                    Reason1 = "1" 
                elif Reason1 == "S":
                    Reason1 = "2"      
                elif Reason1 == "A+":
                    Reason1 = "3"
                elif Reason1 == "A":
                    Reason1 = "4"    
                elif Reason1 == "B+":
                    Reason1 = "5"        
                elif Reason1 == "B":
                    Reason1 = "6"      
                elif Reason1 == "C+":
                    Reason1 = "7"       
                elif Reason1 == "C":
                    Reason1 = "8"     
                elif Reason1 == "D+":
                    Reason1 = "9"
                elif Reason1 == "D":
                    Reason1 = "10"
                elif Reason1 == "E":
                    Reason1 = "11"             
                        
                if Faith == "S+":
                    Faith = "1" 
                elif Faith == "S":
                    Faith = "2"      
                elif Faith == "A+":
                    Faith = "3"
                elif Faith == "A":
                    Faith = "4"    
                elif Faith == "B+":
                    Faith = "5"        
                elif Faith == "B":
                    Faith = "6"      
                elif Faith == "C+":
                    Faith = "7"       
                elif Faith == "C":
                    Faith = "8"     
                elif Faith == "D+":
                    Faith = "9"
                elif Faith == "D":
                    Faith = "10"
                elif Faith == "E":
                    Faith = "11"         
                        
                if Faith1 == "S+":
                    Faith1 = "1" 
                elif Faith1 == "S":
                    Faith1 = "2"      
                elif Faith1 == "A+":
                    Faith1 = "3"
                elif Faith1 == "A":
                    Faith1 = "4"    
                elif Faith1 == "B+":
                    Faith1 = "5"        
                elif Faith1 == "B":
                    Faith1 = "6"      
                elif Faith1 == "C+":
                    Faith1 = "7"       
                elif Faith1 == "C":
                    Faith1 = "8"     
                elif Faith1 == "D+":
                    Faith1 = "9"
                elif Faith1 == "D":
                    Faith1 = "10"
                elif Faith1 == "E":
                    Faith1 = "11"         
                        
                if int(Sword) > int(Sword1):
                    SwordT = Sword1
                else:
                    SwordT = Sword     
                    
                if int(Lance) > int(Lance1):
                    LanceT = Lance1
                else:
                    LanceT = Lance        
                    
                if int(Bow) > int(Bow1):
                    BowT = Bow1
                else:
                    BowT = Bow     
                    
                if int(Axe) > int(Axe1):
                    AxeT = Axe1
                else:
                    AxeT = Axe     
                    
                if int(Brawl) > int(Brawl1):
                    BrawlT = Brawl1
                else:
                    BrawlT = Brawl        
                    
                if int(Reason) > int(Reason1):
                    ReasonT = Reason1
                else:
                    ReasonT = Reason               
                        
                if int(Faith) > int(Faith1):
                    FaithT = Faith1
                else:
                    FaithT = Faith            
                        
                if FaithT == "1":
                    FaithT = "S+" 
                elif FaithT == "2":
                    FaithT = "S"      
                elif FaithT == "3":
                    FaithT = "A+"
                elif FaithT == "4":
                    FaithT = "A"    
                elif FaithT == "5":
                    FaithT = "B+"        
                elif FaithT == "6":
                    FaithT = "B"      
                elif FaithT == "7":
                    FaithT = "C+"       
                elif FaithT == "8":
                    FaithT = "C"     
                elif FaithT == "9":
                    FaithT = "D+"
                elif FaithT == "10":
                    FaithT = "D"
                elif FaithT == "11":
                    FaithT = "E"         
                       
                if ReasonT == "1":
                    ReasonT = "S+" 
                elif ReasonT == "2":
                    ReasonT = "S"      
                elif ReasonT == "3":
                    ReasonT = "A+"
                elif ReasonT == "4":
                    ReasonT = "A"    
                elif ReasonT == "5":
                    ReasonT = "B+"        
                elif ReasonT == "6":
                    ReasonT = "B"      
                elif ReasonT == "7":
                    ReasonT = "C+"       
                elif ReasonT == "8":
                    ReasonT = "C"     
                elif ReasonT == "9":
                    ReasonT = "D+"
                elif ReasonT == "10":
                    ReasonT = "D"
                elif ReasonT == "11":
                    ReasonT = "E"            
                    
                if BrawlT == "1":
                    BrawlT = "S+" 
                elif BrawlT == "2":
                    BrawlT = "S"      
                elif BrawlT == "3":
                    BrawlT = "A+"
                elif BrawlT == "4":
                    BrawlT = "A"    
                elif BrawlT == "5":
                    BrawlT = "B+"        
                elif BrawlT == "6":
                    BrawlT = "B"      
                elif BrawlT == "7":
                    BrawlT = "C+"       
                elif BrawlT == "8":
                    BrawlT = "C"     
                elif BrawlT == "9":
                    BrawlT = "D+"
                elif BrawlT == "10":
                    BrawlT = "D"
                elif BrawlT == "11":
                    BrawlT = "E"   
                    
                if AxeT == "1":
                    AxeT = "S+" 
                elif AxeT == "2":
                    AxeT = "S"      
                elif AxeT == "3":
                    AxeT = "A+"
                elif AxeT == "4":
                    AxeT = "A"    
                elif AxeT == "5":
                    AxeT = "B+"        
                elif AxeT == "6":
                    AxeT = "B"      
                elif AxeT == "7":
                    AxeT = "C+"       
                elif AxeT == "8":
                    AxeT = "C"     
                elif AxeT == "9":
                    AxeT = "D+"
                elif AxeT == "10":
                    AxeT = "D"
                elif AxeT == "11":
                    AxeT = "E"
                        
                if BowT == "1":
                    BowT = "S+" 
                elif BowT == "2":
                    BowT = "S"      
                elif BowT == "3":
                    BowT = "A+"
                elif BowT == "4":
                    BowT = "A"    
                elif BowT == "5":
                    BowT = "B+"        
                elif BowT == "6":
                    BowT = "B"      
                elif BowT == "7":
                    BowT = "C+"       
                elif BowT == "8":
                    BowT = "C"     
                elif BowT == "9":
                    BowT = "D+"
                elif BowT == "10":
                    BowT = "D"
                elif BowT == "11":
                    BowT = "E"    
                    
                if LanceT == "1":
                    LanceT = "S+" 
                elif LanceT == "2":
                    LanceT = "S"      
                elif LanceT == "3":
                    LanceT = "A+"
                elif LanceT == "4":
                    LanceT = "A"    
                elif LanceT == "5":
                    LanceT = "B+"        
                elif LanceT == "6":
                    LanceT = "B"      
                elif LanceT == "7":
                    LanceT = "C+"       
                elif LanceT == "8":
                    LanceT = "C"     
                elif LanceT == "9":
                    LanceT = "D+"
                elif LanceT == "10":
                    LanceT = "D"
                elif LanceT == "11":
                    LanceT = "E"    
                    
                if SwordT == "1":
                    SwordT = "S+" 
                elif SwordT == "2":
                    SwordT = "S"      
                elif SwordT == "3":
                    SwordT = "A+"
                elif SwordT == "4":
                    SwordT = "A"    
                elif SwordT == "5":
                    SwordT = "B+"        
                elif SwordT == "6":
                    SwordT = "B"      
                elif SwordT == "7":
                    SwordT = "C+"       
                elif SwordT == "8":
                    SwordT = "C"     
                elif SwordT == "9":
                    SwordT = "D+"
                elif SwordT == "10":
                    SwordT = "D"
                elif SwordT == "11":
                    SwordT = "E"        
                        
                cursor.execute('''INSERT INTO Character(NAME, HC, HT, STR, MAG, DEF, RES, SPD, SKILL, LUCK, CLASS, SWORD, LANCE, BOW, AXE, BRAWL, REASON, FAITH) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (NameT, HealthT, HealthT, StrT, MagT, DefT, ResT, SpdT, SkillT, LuckT, ClassT, SwordT, LanceT, BowT, AxeT, BrawlT, ReasonT, FaithT))
                cursor.execute('''INSERT INTO Character(NAME, HC, HT, STR, MAG, DEF, RES, SPD, SKILL, LUCK, CLASS, SWORD, LANCE, BOW, AXE, BRAWL, REASON, FAITH) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (Name1 + "+" + Name, HealthT, HealthT, StrT, MagT, DefT, ResT, SpdT, SkillT, LuckT, ClassT, SwordT, LanceT, BowT, AxeT, BrawlT, ReasonT, FaithT))
                
                await message.channel.send("```" + str(Name) + " and " + str(Name1) + " have been paired up! \nTo use the pairing use !fight " + str(NameT) + " [another character] [Weapon type]\nAlso don't forget to unpair them with !unpair " + str(NameT) + "```")
                
        elif message.content == "!disbandpair" + mess[12:]:
            count = 0
            count1 = 0
            Name = ""
            Namex = ""
            Namey = ""
            In = ""
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                    
                elif count == 1:
                    Name += char + ""
            
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                
                elif char == '+':
                    count1 = count1 + 1
                
                elif count == 2:
                    if count1 == 0:
                        Namex += char + ""
                    elif count1 == 1:
                        Namey += char + ""
                                        
            for row in cursor.execute("SELECT Name FROM Character WHERE Name = ?",[Name]):
                In = row[0]
            
            if In == Name:
                cursor.execute("DELETE FROM Character WHERE NAME = ?", [Name])
                cursor.execute("DELETE FROM Character WHERE NAME = ?", [Namey + "+" + Namex])
                await message.channel.send("```" + str(Namex) + " and " + str(Namey) + " have been unpaired!```")

            else:   
                await message.channel.send("```" + str(Namex) + "and " + str(Namey) + " have not been paired up before!```")
                
        elif message.content == "!hurt" + mess[5:]:
            count = 0
            Name = ""
            Dam = ""
            Health = 0
            HeathT = 0
            for char in mess:
                
                if char == ' ':
                    count = count + 1
                    
                elif count == 1:
                    Name += char + ""
                    
                elif count == 2:
                    Dam += char + ""
                    
            for row in cursor.execute("SELECT HC FROM Character WHERE Name = ?",[Name]):
                Health = row[0]
                
            HealthT = Health - int(Dam)
            
            if HealthT > 0 :
                await message.channel.send("```" + str(Name) + " takes " + str(Dam) + " damage and now has " + str(HealthT) + " health!```")
                cursor.execute("UPDATE Character SET HC = ? WHERE Name = ?",[HealthT, Name])
                
            else :
                await message.channel.send("```" + str(Name) + " takes " + str(Dam) + " damage and has been knocked out!```")
                cursor.execute("UPDATE Character SET HC = HT WHERE Name = ?",[Name])
                
        elif message.content == "!give" + mess[5:]:
            count = 0
            Name = ""
            Item = ""
            Itemval = ""
            Itemuses = ""
            Itemvalnum = 0
            Itemslot1 = ""
            Itemslot2 =""
            Itemslot3 = ""
            Itemslot4 = ""
            Itemslot5 = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     Item += char + ""
            for row in cursor.execute("SELECT Item1, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot1 = row[0]
            for row in cursor.execute("SELECT Item2, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot2 = row[0]
            for row in cursor.execute("SELECT Item3, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot3 = row[0]
            for row in cursor.execute("SELECT Item4, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot4 = row[0]
            for row in cursor.execute("SELECT Item5, Name FROM Chargold WHERE Name = ?",[Name]):
                Itemslot5 = row[0]
            for row in cursor.execute("SELECT VALUE, ITEM FROM Market WHERE ITEM = ?",[Item]):
                Itemval = row[0]
            for row in cursor.execute("SELECT USES, ITEM FROM Market WHERE ITEM = ?",[Item]):
                Itemuses = row[0]
            Itemvalnum = Itemval
            if int(Itemuses) >= 1:
                if Itemslot1 == "x":
                    cursor.execute("UPDATE Chargold SET Item1 = ? WHERE Name = ?",[Item, Name])
                    cursor.execute("UPDATE Chargold SET Item1uses = ? WHERE Name = ?",[Itemuses, Name])
                    await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " it has been added to the first slot in their inventory!```")  
                elif Itemslot2 == "x":
                    cursor.execute("UPDATE Chargold SET Item2 = ? WHERE Name = ?",[Item, Name])
                    cursor.execute("UPDATE Chargold SET Item2uses = ? WHERE Name = ?",[Itemuses, Name])
                    await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " it has been added to the second slot in their inventory!```")  
                elif Itemslot3 == "x":
                    cursor.execute("UPDATE Chargold SET Item3 = ? WHERE Name = ?",[Item, Name])
                    cursor.execute("UPDATE Chargold SET Item3uses = ? WHERE Name = ?",[Itemuses, Name])
                    await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " it has been added to the third slot in their inventory!```")  
                elif Itemslot4 == "x":
                    cursor.execute("UPDATE Chargold SET Item4 = ? WHERE Name = ?",[Item, Name])
                    cursor.execute("UPDATE Chargold SET Item4uses = ? WHERE Name = ?",[Itemuses, Name])
                    await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " it has been added to the fourth slot in their inventory!```")  
                elif Itemslot5 == "x":
                    cursor.execute("UPDATE Chargold SET Item5 = ? WHERE Name = ?",[Item, Name])
                    cursor.execute("UPDATE Chargold SET Item5uses = ? WHERE Name = ?",[Itemuses, Name])
                    await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " it has been added to the fifth slot in their inventory!```")  
                else:
                    await message.channel.send("```" + str(Name) + " does not have any space the this item!```")
            else:
                await message.channel.send("```" + str(Name) + " was given a "+ str(Item) + " they can use this at anytime!```")          
        
        elif message.content == "!gun" + mess[4:]:
            count = 0
            Name = ""
            
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                     
            list = ["Sadon", "Nora", "Emily", "Ale", "Alice","Leo", "Leslie", "Yakov", "Orson", "Yurusu", "Monika", "Deloris", "Barabal", "Sawyer", "Ansel", "Wuji", "Flare", "Nex", "Valentin", "Maddie", "Delphi", "Suigi", "Takako", "Duff", "Veena", "Jules", "Nerin", "Kiyoshi", "Meldios", "Diya", "Oakley", "Dirk", "Flynn", "Lawrence", "Conway", "Damian", "Wren", "Oliver", "Azmon", "Pisti", "Onida"]
            Name1 = random.choice(list)
            if Name != "":         
                await message.channel.send("```Deloris pulls out his gun and shoots " + str(Name) + " they take 999 damage instantly killing " + str(Name) + "```")
            else:
                await message.channel.send("```" + str(random.choice(list)) + " pulls out their gun and shoots " + str(Name1) + " they take 999 damage instantly killing " + str(Name1) + "```")
        
        elif message.content == "!smooch" + mess[8:]:
            count = 0
            Name = ""
            
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                     
            list = ["Sadon", "Nora", "Emily", "Ale", "Alice","Leo", "Leslie", "Yakov", "Orson", "Yurusu", "Monika", "Deloris", "Barabal", "Sawyer", "Ansel", "Wuji", "Flare", "Nex", "Valentin", "Maddie", "Delphi", "Suigi", "Takako", "Duff", "Veena", "Jules", "Nerin", "Kiyoshi", "Meldios", "Diya", "Oakley", "Dirk", "Flynn", "Lawrence", "Conway", "Damian", "Wren", "Oliver", "Azmon", "Pisti", "Onida"]
            Name1 = random.choice(list)
            await message.channel.send("```" + str(random.choice(list)) + " smooches " + str(Name1) + " how sweet uwu```")
            
        elif message.content == "!vibecheck" + mess[10:]:
            count = 0
            Name = ""
            vibe = 0
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""  
                     
            vibe = random.randint(0,100)
            if vibe == 0:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe)+ " out of a 100 I have never seen worse vibes! *Cocks gun* you got to go.```")
            if vibe > 0 and vibe <= 20:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe)+ " out of a 100 your vibes are horrible!```")
            elif vibe > 20 and vibe <= 40:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 your vibes are not very good...```")
            elif vibe > 40 and vibe <= 60:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 your vibes are alright!```")
            elif vibe > 60 and vibe < 69:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 your vibes are pretty good!!!```")
            elif vibe == 69:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 \nnice```")
            elif vibe > 69 and vibe <= 80:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 your vibes are pretty good!!!```")
            elif vibe > 80 and vibe <= 99:
                await message.channel.send("```" + str(Name) + " I rate your vibe a "+ str(vibe) +" out of a 100 your vibes are great! Keep it up!```")
            elif vibe == 100:
                await message.channel.send("```" + str(Name) + " I rate your vibe a " +str(vibe) +" out of a 100 your vibes are amazing! Best vibes ever!```")
        
        elif message.content == "!hotornot" + mess[9:]:
            count = 0
            Name = ""
            hot = random.randint(1,100)
            
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                     
            if hot >49 and hot < 100:
                await message.channel.send("```" + str(Name) + " is a hottie!```")
            elif hot == 100:
                await message.channel.send("```" + str(Name) + "? MMMMM Sexy~```")
            else:
                await message.channel.send("```" + str(Name) + " eh that's a not!```")
                
        elif message.content == "!AddBattle"+ mess[10:]:
            count = 0
            count1 = 0
            In = ""
            Name = ""
            Ob = ""
            Vic = ""
            Def = ""
            for char in mess: 
                    if char == ' ' and count == 0:
                        count += 1
                    elif char == ',':
                        count1 += 1
                    elif count >= 1 and count1 == 0:
                        Name += char + ""
                    elif count >= 1 and count1 == 1:
                        Ob += char + ""
                    elif count >= 1 and count1 == 2:
                        Vic += char + ""
                    elif count >= 1 and count1 == 3:
                        Def += char + ""
            for row in cursor.execute("SELECT Name FROM Battle WHERE Name = ?",[Name]):
                In = row[0]
            if In == Name:
                await message.channel.send("```Battle " + Name +" is already in the Database!```")
            else:
                cursor.execute('''INSERT INTO Battle(NAME, Objective, Victory, Defeat) 
                            VALUES(?,?,?,?)''', (Name, Ob, Vic, Def))
                await message.channel.send("```Battle " + Name +" has been added use !BattleStart [Name] to start the battle```")
        
        elif message.content == "!BattleStart"+ mess[12:]:
            count = 0
            count1 = 0
            countO = 0
            In = ""
            Name = ""
            Ob = ""
            Vic = ""
            Def = ""
            Owner = ""
            Owner1 = ""
            OwnerT =""
            Temp = ""
            Temp2 = ""
            for char in mess: 
                    if char == ' ':
                        count += 1
                    elif count == 1:
                        Name += char + ""
            countx = 0
            county = 0
            for row in cursor.execute("SELECT Objective FROM Battle WHERE Name = ?",[Name]):
                Ob = row[0]
            for row in cursor.execute("SELECT Victory FROM Battle WHERE Name = ?",[Name]):
                Vic = row[0]
            for row in cursor.execute("SELECT Defeat FROM Battle WHERE Name = ?",[Name]):
                Def = row[0]
            for row in cursor.execute("SELECT Name FROM Battle WHERE Name = ?",[Name]):
                In = row[0]
            for i in cursor.execute("SELECT Name FROM InBattle ORDER BY SPD DESC"):
                Not_VisitedAllies.append(i[0])
                print(i[0])
            
            for i in cursor.execute("SELECT Name FROM Inbattleene ORDER BY SPD DESC"):
                Not_VisitedEnemies.append(i[0])
                print(i[0])
            await message.channel.send("```Objective: " + Ob +"\n\nVictory Condition: " + Vic + "\n\nDefeat Condition: " + Def +"\n\nBattle start!```")
            x = "```Allies Speed:\n"
            for i in Not_VisitedAllies:
                Temp = i
                for row in cursor.execute("SELECT SPD FROM InBattle WHERE NAME = ?", [Temp]):
                    Temp2 = row[0]
                x += Temp + ": " + str(Temp2)+ "\n"
            x += "\nEnemies' Speed:\n"
            for i in Not_VisitedEnemies:
                Temp = i
                for row in cursor.execute("SELECT SPD FROM Inbattleene WHERE NAME = ?", [Temp]):
                    Temp2 = row[0]
                x += Temp + ": " + str(Temp2) + "\n"
            await message.channel.send(x + "```")
            Phase = "Allies Phase"
            character = Not_VisitedAllies[0]
            if len(Not_VisitedAllies) >= 1:
                await message.channel.send("```" + str(Phase) + "\n\nIt's " + str(character) + "'s turn!\n```")
            VisitedAllies.append(Not_VisitedAllies[0])
            Not_VisitedAllies.remove(Not_VisitedAllies[0])
                
        elif message.content == "!Health"+ mess[7:]:
            count = 0
            count1 = 0
            In = ""
            Name = ""
            Healcurr = ""
            for char in mess: 
                    if char == ' ':
                        count += 1
                    elif count == 1:
                        Name += char + ""
            for row in cursor.execute("SELECT HC FROM Character WHERE Name = ?",[Name]):
                Healcurr = row[0]
            await message.channel.send("```" + str(Name) + " has " + str(Healcurr) + " health left!```")
            
        elif message.content == "!Stats" + mess[6:]:
            count = 0
            Name = ""
            Health = ""
            Health1 = ""
            Str = ""
            Mag = ""
            Def = ""
            Res = ""
            Spd = ""
            Skill = ""
            Luck = ""
            Sword = ""
            Lance = ""
            Bow = ""
            Axe = ""
            Brawl = ""
            Reason = ""
            Faith = ""
            for char in mess: 
                if char == ' ':
                    count += 1
                elif count == 1:
                    Name += char + ""
            for row in cursor.execute("SELECT HC FROM Character WHERE Name = ?",[Name]):
                Health = row[0]     
            for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                Health1 = row[0]   
            for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                Str = row[0]
            for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                Mag = row[0]  
            for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                Def = row[0]
            for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                Res = row[0]
            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                Spd = row[0]
            for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                Skill = row[0]
            for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                Luck = row[0]
            for row in cursor.execute("SELECT SWORD FROM Character WHERE Name = ?",[Name]):
                Sword = row[0]  
            for row in cursor.execute("SELECT LANCE FROM Character WHERE Name = ?",[Name]):
                Lance = row[0]
            for row in cursor.execute("SELECT BOW FROM Character WHERE Name = ?",[Name]):
                Bow = row[0]
            for row in cursor.execute("SELECT AXE FROM Character WHERE Name = ?",[Name]):
                Axe = row[0]
            for row in cursor.execute("SELECT BRAWL FROM Character WHERE Name = ?",[Name]):
                Brawl = row[0]    
            for row in cursor.execute("SELECT REASON FROM Character WHERE Name = ?",[Name]):
                Reason = row[0]
            for row in cursor.execute("SELECT FAITH FROM Character WHERE Name = ?",[Name]):
                Faith = row[0]   
                
            await message.channel.send("```" + str(Name) + "'s Stats:\nHealth: " + str(Health) + "/" + str(Health1) + "\nStrength: " + str(Str) +"\nMagic: " + str(Mag) + "\nDefense: " + str(Def) + "\nResistance: " + str(Res) + "\nSpeed: " + str(Spd)+ "\nSkill: " + str(Skill) + "\nLuck: " + str(Luck)+ "\n\n Weapon Grades:\nSword: " + str(Sword) + "\nLance: " + str(Lance) + "\nBow: " + str(Bow) + "\nAxe: " + str(Axe) + "\nBrawl: " + str(Brawl) + "\nReason: " + str(Reason) + "\nFaith: " + str(Faith) +"```")
            
        elif message.content == "!Addtobattle" + mess[12:]:
            count = 0
            Name= ""
            Title = ""
            spd = 0
            for char in mess: 
                if char == ' ':
                    count += 1
                elif count == 0:
                    Title += char + ""
                elif count == 1:
                    Name += char + ""
                    
            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
               spd = row[0]   
                
            if Title == "!Addtobattle":
                cursor.execute('''INSERT INTO InBattle(NAME,SPD) 
                            VALUES(?,?)''', (Name, spd))
                await message.channel.send("```" + Name + " has been added to the Battle/Seminar! Please make sure you are available for the battle! If you aren't available for some reason please use !Removefrombattle [Name] prior to the Battle/Seminar starting. Thank you!```")
            elif Title == "!Addtobattleenemies":
                cursor.execute('''INSERT INTO InBattleene(NAME,SPD) 
                        VALUES(?,?)''', (Name,spd))
                await message.channel.send("```" + Name + " has been added to the Battle/Seminar (for the baddies)! Please make sure you are available for the battle! If you aren't available for some reason please use !Removefrombattle [Name] prior to the Battle/Seminar starting. Thank you!```")
                
        elif message.content == "!Removefrombattle" + mess[17:]:
            count = 0
            Name= ""
            Title = ""
            for char in mess: 
                if char == ' ':
                    count += 1
                elif count == 0:
                    Title += char + ""
                elif count == 1:
                    Name += char + ""
            if Title == "!Removefrombattle":
                cursor.execute("DELETE FROM InBattle WHERE NAME = ?", [Name])
                await message.channel.send("```" + Name + " has been removed from the Battle/Seminar!```")
            elif Title == "!Removefrombattleenemies":
                cursor.execute("DELETE FROM InBattleene WHERE NAME = ?", [Name])
                await message.channel.send("```" + Name + " has been removed from the Battle/Seminar!```")
            
        elif message.content == "!Nextturn":
            Name = ""
            print(Not_VisitedAllies)
            print(Not_VisitedEnemies)
            print(len(Not_VisitedAllies))
            if Phase == "Allies Phase":
                if len(Not_VisitedAllies) == 1:
                    Name = Not_VisitedAllies[0]
                    for x in VisitedAllies:
                        Not_VisitedAllies.insert(0,x)
                        VisitedAllies.remove(VisitedAllies[0])
                    if Name != "":
                        Str = 0
                        Health = 0
                        Def = 0
                        Res = 0
                        Mag = 0
                        Skill = 0
                        Luck = 0
                        Spd = 0
                        STRTurns = 0
                        MAGTurns = 0
                        DEFTurns = 0
                        RESTurns = 0
                        HEALTHTurns = 0
                        SKILLTurns = 0
                        LUCKTurns = 0
                        SPDTurns = 0
                        Name1 = ""

                        for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                            Str = row[0]
                        for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                            Health = row[0]
                        for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                            Def = row[0]
                        for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                            Mag = row[0]
                        for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                            Res = row[0]
                        for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                            Skill = row[0]
                        for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                            Luck = row[0]
                        for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                            Spd = row[0]
                        for row in cursor.execute("SELECT STRTURNS FROM Buffs WHERE Name = ?",[Name]):
                            STRTurns = row[0]
                        for row in cursor.execute("SELECT MAGTURNS FROM Buffs WHERE Name = ?",[Name]):
                            MAGTurns = row[0]
                        for row in cursor.execute("SELECT DEFTURNS FROM Buffs WHERE Name = ?",[Name]):
                            DEFTurns = row[0]
                        for row in cursor.execute("SELECT RESTURNS FROM Buffs WHERE Name = ?",[Name]):
                            RESTurns = row[0]
                        for row in cursor.execute("SELECT HEALTHTURNS FROM Buffs WHERE Name = ?",[Name]):
                            HEALTHTurns = row[0]
                        for row in cursor.execute("SELECT SKILLTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SKILLTurns = row[0]
                        for row in cursor.execute("SELECT LUCKTURNS FROM Buffs WHERE Name = ?",[Name]):
                            LUCKTurns = row[0]
                        for row in cursor.execute("SELECT SPDTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SPDTurns = row[0]
                        STRTurns = STRTurns - 1
                        MAGTurns = MAGTurns - 1
                        DEFTurns = DEFTurns - 1
                        RESTurns = RESTurns - 1
                        HEALTHTurns = HEALTHTurns - 1
                        SKILLTurns = SKILLTurns - 1
                        LUCKTurns = LUCKTurns - 1
                        SPDTurns = SPDTurns - 1
                        print(STRTurns)
                        cursor.execute("UPDATE Buffs SET STRTURNS = ? WHERE Name = ?",[STRTurns, Name])
                        cursor.execute("UPDATE Buffs SET MAGTURNS = ? WHERE Name = ?",[MAGTurns, Name])
                        cursor.execute("UPDATE Buffs SET DEFTURNS = ? WHERE Name = ?",[DEFTurns, Name])
                        cursor.execute("UPDATE Buffs SET RESTURNS = ? WHERE Name = ?",[RESTurns, Name])
                        cursor.execute("UPDATE Buffs SET HEALTHTURNS = ? WHERE Name = ?",[HEALTHTurns, Name])
                        cursor.execute("UPDATE Buffs SET SKILLTURNS = ? WHERE Name = ?",[SKILLTurns, Name])
                        cursor.execute("UPDATE Buffs SET LUCKTURNS = ? WHERE Name = ?",[LUCKTurns, Name])
                        cursor.execute("UPDATE Buffs SET SPDTURNS = ? WHERE Name = ?",[SPDTurns, Name])
                        if STRTurns == 0:
                            Str1 = 0
                            for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                                STR1 = row[0]
                            if Str > 0:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR buff has wore off!```")
                            else:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR debuff has wore off!```")
                                
                        elif MAGTurns == 0:
                            Mag1 = 0
                            for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                                Mag1 = row[0]
                            if Mag > 0:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG buff has wore off!```")
                            else:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG debuff has wore off!```")
                        
                        elif DEFTurns == 0:
                            Def1 = 0
                            for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                                Def1 = row[0]
                            if Def > 0:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF buff has wore off!```")
                            else:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF debuff has wore off!```")
                        
                        elif RESTurns == 0:
                            Res1 = 0
                            for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                                Res1 = row[0]
                            if Res > 0:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES buff has wore off!```")
                            else:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES debuff has wore off!```")
                            
                        elif HEALTHTurns == 0:
                            Health1 = 0
                            for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                                Health1 = row[0]
                            if Health > 0:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH buff has wore off!```")
                            else:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH debuff has wore off!```")
                                
                        elif SKILLTurns == 0:
                            Skill1 = 0
                            for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                                Skill1 = row[0]
                            if Skill > 0:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL buff has wore off!```")
                            else:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL debuff has wore off!```")
                                
                        elif LUCKTurns == 0:
                            Luck1 = 0
                            for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                                Luck1 = row[0]
                            if Luck > 0:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK buff has wore off!```")
                            else:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK debuff has wore off!```")
                        
                        elif SPDTurns == 0:
                            Spd1 = 0
                            Update = "True"
                            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                                Spd1 = row[0]
                            if Spd > 0:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD buff has wore off!```")
                            else:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD debuff has wore off!```")
                            
                        await message.channel.send("```" + Phase + " \n\nIts " + str(Name) + "'s turn!```")
                        print(Update)
                        if Update == "True":
                            Not_VisitedAllies = []
                            x = "```Due to Buffs and Debuffs the Speed list has been updated!\nAllies Speed:\n"
                            for i in cursor.execute("SELECT Name FROM InBattle ORDER BY SPD DESC"):
                                Not_VisitedAllies.append(i[0])
                                print(i[0])
                                print("aaa")
                            print(Not_VisitedAllies)
                            for i in Not_VisitedAllies:
                                Temp = i
                                for row in cursor.execute("SELECT SPD FROM Character WHERE NAME = ?", [Temp]):
                                    Temp2 = row[0]
                                    x += Temp + ": " + str(Temp2)+ "\n"
                            x += "\nEnemies' Speed:\n"
                            for i in Not_VisitedEnemies:
                                Temp = i
                                for row in cursor.execute("SELECT SPD FROM Inbattleene WHERE NAME = ?", [Temp]):
                                    Temp2 = row[0]
                                    x += Temp + ": " + str(Temp2) + "\n"
                                    print(Not_VisitedEnemies)
                            await message.channel.send(x + "```")
                            Update = "False"
                        Phase = "Enemies Phase"
                    
                elif len(Not_VisitedAllies) > 1:
                    Name = Not_VisitedAllies[0]
                    VisitedAllies.append(Not_VisitedAllies[0])
                    Not_VisitedAllies.remove(Not_VisitedAllies[0])
                    
                    if Name != "":
                        Str = 0
                        Health = 0
                        Def = 0
                        Res = 0
                        Mag = 0
                        Skill = 0
                        Luck = 0
                        Spd = 0
                        STRTurns = 0
                        MAGTurns = 0
                        DEFTurns = 0
                        RESTurns = 0
                        HEALTHTurns = 0
                        SKILLTurns = 0
                        LUCKTurns = 0
                        SPDTurns = 0

                        for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                            Str = row[0]
                        for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                            Health = row[0]
                        for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                            Def = row[0]
                        for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                            Mag = row[0]
                        for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                            Res = row[0]
                        for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                            Skill = row[0]
                        for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                            Luck = row[0]
                        for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                            Spd = row[0]
                        for row in cursor.execute("SELECT STRTURNS FROM Buffs WHERE Name = ?",[Name]):
                            STRTurns = row[0]
                        for row in cursor.execute("SELECT MAGTURNS FROM Buffs WHERE Name = ?",[Name]):
                            MAGTurns = row[0]
                        for row in cursor.execute("SELECT DEFTURNS FROM Buffs WHERE Name = ?",[Name]):
                            DEFTurns = row[0]
                        for row in cursor.execute("SELECT RESTURNS FROM Buffs WHERE Name = ?",[Name]):
                            RESTurns = row[0]
                        for row in cursor.execute("SELECT HEALTHTURNS FROM Buffs WHERE Name = ?",[Name]):
                            HEALTHTurns = row[0]
                        for row in cursor.execute("SELECT SKILLTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SKILLTurns = row[0]
                        for row in cursor.execute("SELECT LUCKTURNS FROM Buffs WHERE Name = ?",[Name]):
                            LUCKTurns = row[0]
                        for row in cursor.execute("SELECT SPDTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SPDTurns = row[0]
                        STRTurns = STRTurns - 1
                        MAGTurns = MAGTurns - 1
                        DEFTurns = DEFTurns - 1
                        RESTurns = RESTurns - 1
                        HEALTHTurns = HEALTHTurns - 1
                        SKILLTurns = SKILLTurns - 1
                        LUCKTurns = LUCKTurns - 1
                        SPDTurns = SPDTurns - 1
                        print(STRTurns)
                        cursor.execute("UPDATE Buffs SET STRTURNS = ? WHERE Name = ?",[STRTurns, Name])
                        cursor.execute("UPDATE Buffs SET MAGTURNS = ? WHERE Name = ?",[MAGTurns, Name])
                        cursor.execute("UPDATE Buffs SET DEFTURNS = ? WHERE Name = ?",[DEFTurns, Name])
                        cursor.execute("UPDATE Buffs SET RESTURNS = ? WHERE Name = ?",[RESTurns, Name])
                        cursor.execute("UPDATE Buffs SET HEALTHTURNS = ? WHERE Name = ?",[HEALTHTurns, Name])
                        cursor.execute("UPDATE Buffs SET SKILLTURNS = ? WHERE Name = ?",[SKILLTurns, Name])
                        cursor.execute("UPDATE Buffs SET LUCKTURNS = ? WHERE Name = ?",[LUCKTurns, Name])
                        cursor.execute("UPDATE Buffs SET SPDTURNS = ? WHERE Name = ?",[SPDTurns, Name])
                        if STRTurns == 0:
                            Str1 = 0
                            for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                                STR1 = row[0]
                            if Str > 0:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR buff has wore off!```")
                            else:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR debuff has wore off!```")
                                
                        elif MAGTurns == 0:
                            Mag1 = 0
                            for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                                Mag1 = row[0]
                            if Mag > 0:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG buff has wore off!```")
                            else:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG debuff has wore off!```")
                        
                        elif DEFTurns == 0:
                            Def1 = 0
                            for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                                Def1 = row[0]
                            if Def > 0:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF buff has wore off!```")
                            else:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF debuff has wore off!```")
                        
                        elif RESTurns == 0:
                            Res1 = 0
                            for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                                Res1 = row[0]
                            if Res > 0:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES buff has wore off!```")
                            else:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES debuff has wore off!```")
                            
                        elif HEALTHTurns == 0:
                            Health1 = 0
                            for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                                Health1 = row[0]
                            if Health > 0:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH buff has wore off!```")
                            else:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH debuff has wore off!```")
                                
                        elif SKILLTurns == 0:
                            Skill1 = 0
                            for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                                Skill1 = row[0]
                            if Skill > 0:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL buff has wore off!```")
                            else:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL debuff has wore off!```")
                                
                        elif LUCKTurns == 0:
                            Luck1 = 0
                            for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                                Luck1 = row[0]
                            if Luck > 0:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK buff has wore off!```")
                            else:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK debuff has wore off!```")
                        
                        elif SPDTurns == 0:
                            Spd1 = 0
                            Update = "True"
                            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                                Spd1 = row[0]
                            if Spd > 0:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD buff has wore off!```")
                            else:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD debuff has wore off!```")
                            
                        await message.channel.send("```" + Phase + " \n\nIts " + str(Name) + "'s turn!```")
                    
            elif Phase == "Enemies Phase":
                if len(Not_VisitedEnemies) == 1:
                    Name = Not_VisitedEnemies[0]
                    for x in VisitedEnemies:
                        Not_VisitedEnemies.insert(0,x)
                        VisitedEnemies.remove(VisitedEnemies[0])
                    if Name != "":
                        Str = 0
                        Health = 0
                        Def = 0
                        Res = 0
                        Mag = 0
                        Skill = 0
                        Luck = 0
                        Spd = 0
                        STRTurns = 0
                        MAGTurns = 0
                        DEFTurns = 0
                        RESTurns = 0
                        HEALTHTurns = 0
                        SKILLTurns = 0
                        LUCKTurns = 0
                        SPDTurns = 0

                        for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                            Str = row[0]
                        for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                            Health = row[0]
                        for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                            Def = row[0]
                        for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                            Mag = row[0]
                        for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                            Res = row[0]
                        for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                            Skill = row[0]
                        for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                            Luck = row[0]
                        for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                            Spd = row[0]
                        for row in cursor.execute("SELECT STRTURNS FROM Buffs WHERE Name = ?",[Name]):
                            STRTurns = row[0]
                        for row in cursor.execute("SELECT MAGTURNS FROM Buffs WHERE Name = ?",[Name]):
                            MAGTurns = row[0]
                        for row in cursor.execute("SELECT DEFTURNS FROM Buffs WHERE Name = ?",[Name]):
                            DEFTurns = row[0]
                        for row in cursor.execute("SELECT RESTURNS FROM Buffs WHERE Name = ?",[Name]):
                            RESTurns = row[0]
                        for row in cursor.execute("SELECT HEALTHTURNS FROM Buffs WHERE Name = ?",[Name]):
                            HEALTHTurns = row[0]
                        for row in cursor.execute("SELECT SKILLTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SKILLTurns = row[0]
                        for row in cursor.execute("SELECT LUCKTURNS FROM Buffs WHERE Name = ?",[Name]):
                            LUCKTurns = row[0]
                        for row in cursor.execute("SELECT SPDTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SPDTurns = row[0]
                        STRTurns = STRTurns - 1
                        MAGTurns = MAGTurns - 1
                        DEFTurns = DEFTurns - 1
                        RESTurns = RESTurns - 1
                        HEALTHTurns = HEALTHTurns - 1
                        SKILLTurns = SKILLTurns - 1
                        LUCKTurns = LUCKTurns - 1
                        SPDTurns = SPDTurns - 1
                        print(STRTurns)
                        cursor.execute("UPDATE Buffs SET STRTURNS = ? WHERE Name = ?",[STRTurns, Name])
                        cursor.execute("UPDATE Buffs SET MAGTURNS = ? WHERE Name = ?",[MAGTurns, Name])
                        cursor.execute("UPDATE Buffs SET DEFTURNS = ? WHERE Name = ?",[DEFTurns, Name])
                        cursor.execute("UPDATE Buffs SET RESTURNS = ? WHERE Name = ?",[RESTurns, Name])
                        cursor.execute("UPDATE Buffs SET HEALTHTURNS = ? WHERE Name = ?",[HEALTHTurns, Name])
                        cursor.execute("UPDATE Buffs SET SKILLTURNS = ? WHERE Name = ?",[SKILLTurns, Name])
                        cursor.execute("UPDATE Buffs SET LUCKTURNS = ? WHERE Name = ?",[LUCKTurns, Name])
                        cursor.execute("UPDATE Buffs SET SPDTURNS = ? WHERE Name = ?",[SPDTurns, Name])
                        if STRTurns == 0:
                            Str1 = 0
                            for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                                STR1 = row[0]
                            if Str > 0:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR buff has wore off!```")
                            else:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR debuff has wore off!```")
                                
                        elif MAGTurns == 0:
                            Mag1 = 0
                            for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                                Mag1 = row[0]
                            if Mag > 0:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG buff has wore off!```")
                            else:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG debuff has wore off!```")
                        
                        elif DEFTurns == 0:
                            Def1 = 0
                            for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                                Def1 = row[0]
                            if Def > 0:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF buff has wore off!```")
                            else:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF debuff has wore off!```")
                        
                        elif RESTurns == 0:
                            Res1 = 0
                            for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                                Res1 = row[0]
                            if Res > 0:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES buff has wore off!```")
                            else:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES debuff has wore off!```")
                            
                        elif HEALTHTurns == 0:
                            Health1 = 0
                            for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                                Health1 = row[0]
                            if Health > 0:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH buff has wore off!```")
                            else:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH debuff has wore off!```")
                                
                        elif SKILLTurns == 0:
                            Skill1 = 0
                            for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                                Skill1 = row[0]
                            if Skill > 0:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL buff has wore off!```")
                            else:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL debuff has wore off!```")
                                
                        elif LUCKTurns == 0:
                            Luck1 = 0
                            for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                                Luck1 = row[0]
                            if Luck > 0:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK buff has wore off!```")
                            else:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK debuff has wore off!```")
                        
                        elif SPDTurns == 0:
                            Spd1 = 0
                            Update = "True"
                            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                                Spd1 = row[0]
                            if Spd > 0:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD buff has wore off!```")
                            else:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD debuff has wore off!```")
                            
                        await message.channel.send("```" + Phase + " \n\nIts " + str(Name) + "'s turn!```")
                        print(Update)
                        if Update == "True":
                            Not_VisitedEnemies = []
                            x = "```Due to Buffs and Debuffs the Speed list has been updated!\nAllies Speed:\n"
                            for i in cursor.execute("SELECT Name FROM InBattle ORDER BY SPD DESC"):
                                Temp = i[0]
                                for row in cursor.execute("SELECT SPD FROM Character WHERE NAME = ?", [Temp]):
                                    Temp2 = row[0]
                                    x += Temp + ": " + str(Temp2)+ "\n"
                            x += "\nEnemies' Speed:\n"
                            for i in cursor.execute("SELECT Name FROM Inbattleene ORDER BY SPD DESC"):
                                Not_VisitedEnemies.append(i[0])
                        
                            for i in Not_VisitedEnemies:
                                Temp = i
                        
                                for row in cursor.execute("SELECT SPD FROM Character WHERE NAME = ?", [Temp]):
                                    Temp2 = row[0]
                                    x += Temp + ": " + str(Temp2) + "\n"
                            await message.channel.send(x + "```")
                            Update = "False"
                        Phase = "Allies Phase"
                    
                elif len(Not_VisitedEnemies) > 1:
                    Name = Not_VisitedEnemies[0]
                    VisitedEnemies.append(Not_VisitedEnemies[0])
                    Not_VisitedEnemies.remove(Not_VisitedEnemies[0])
                    if Name != "":
                        Str = 0
                        Health = 0
                        Def = 0
                        Res = 0
                        Mag = 0
                        Skill = 0
                        Luck = 0
                        Spd = 0
                        STRTurns = 0
                        MAGTurns = 0
                        DEFTurns = 0
                        RESTurns = 0
                        HEALTHTurns = 0
                        SKILLTurns = 0
                        LUCKTurns = 0
                        SPDTurns = 0

                        for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                            Str = row[0]
                        for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                            Health = row[0]
                        for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                            Def = row[0]
                        for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                            Mag = row[0]
                        for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                            Res = row[0]
                        for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                            Skill = row[0]
                        for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                            Luck = row[0]
                        for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                            Spd = row[0]
                        for row in cursor.execute("SELECT STRTURNS FROM Buffs WHERE Name = ?",[Name]):
                            STRTurns = row[0]
                        for row in cursor.execute("SELECT MAGTURNS FROM Buffs WHERE Name = ?",[Name]):
                            MAGTurns = row[0]
                        for row in cursor.execute("SELECT DEFTURNS FROM Buffs WHERE Name = ?",[Name]):
                            DEFTurns = row[0]
                        for row in cursor.execute("SELECT RESTURNS FROM Buffs WHERE Name = ?",[Name]):
                            RESTurns = row[0]
                        for row in cursor.execute("SELECT HEALTHTURNS FROM Buffs WHERE Name = ?",[Name]):
                            HEALTHTurns = row[0]
                        for row in cursor.execute("SELECT SKILLTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SKILLTurns = row[0]
                        for row in cursor.execute("SELECT LUCKTURNS FROM Buffs WHERE Name = ?",[Name]):
                            LUCKTurns = row[0]
                        for row in cursor.execute("SELECT SPDTURNS FROM Buffs WHERE Name = ?",[Name]):
                            SPDTurns = row[0]
                        STRTurns = STRTurns - 1
                        MAGTurns = MAGTurns - 1
                        DEFTurns = DEFTurns - 1
                        RESTurns = RESTurns - 1
                        HEALTHTurns = HEALTHTurns - 1
                        SKILLTurns = SKILLTurns - 1
                        LUCKTurns = LUCKTurns - 1
                        SPDTurns = SPDTurns - 1
                        print(STRTurns)
                        cursor.execute("UPDATE Buffs SET STRTURNS = ? WHERE Name = ?",[STRTurns, Name])
                        cursor.execute("UPDATE Buffs SET MAGTURNS = ? WHERE Name = ?",[MAGTurns, Name])
                        cursor.execute("UPDATE Buffs SET DEFTURNS = ? WHERE Name = ?",[DEFTurns, Name])
                        cursor.execute("UPDATE Buffs SET RESTURNS = ? WHERE Name = ?",[RESTurns, Name])
                        cursor.execute("UPDATE Buffs SET HEALTHTURNS = ? WHERE Name = ?",[HEALTHTurns, Name])
                        cursor.execute("UPDATE Buffs SET SKILLTURNS = ? WHERE Name = ?",[SKILLTurns, Name])
                        cursor.execute("UPDATE Buffs SET LUCKTURNS = ? WHERE Name = ?",[LUCKTurns, Name])
                        cursor.execute("UPDATE Buffs SET SPDTURNS = ? WHERE Name = ?",[SPDTurns, Name])
                        if STRTurns == 0:
                            Str1 = 0
                            for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                                Str1 = row[0]
                            if Str > 0:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR buff has wore off!```")
                            else:
                                Str1= Str1 - Str
                                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, Name])
                                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s STR debuff has wore off!```")
                                
                        elif MAGTurns == 0:
                            Mag1 = 0
                            for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                                Mag1 = row[0]
                            if Mag > 0:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG buff has wore off!```")
                            else:
                                Mag1= Mag1 - Mag
                                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, Name])
                                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s MAG debuff has wore off!```")
                        
                        elif DEFTurns == 0:
                            Def1 = 0
                            for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                                Def1 = row[0]
                            if Def > 0:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF buff has wore off!```")
                            else:
                                Def1= Def1 - Def
                                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, Name])
                                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s DEF debuff has wore off!```")
                        
                        elif RESTurns == 0:
                            Res1 = 0
                            for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                                Res1 = row[0]
                            if Res > 0:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES buff has wore off!```")
                            else:
                                Res1= Res1 - Res
                                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, Name])
                                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s RES debuff has wore off!```")
                            
                        elif HEALTHTurns == 0:
                            Health1 = 0
                            for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                                Health1 = row[0]
                            if Health > 0:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH buff has wore off!```")
                            else:
                                Health1= Health1 - Health
                                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, Name])
                                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s HEALTH debuff has wore off!```")
                                
                        elif SKILLTurns == 0:
                            Skill1 = 0
                            for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                                Skill1 = row[0]
                            if Skill > 0:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL buff has wore off!```")
                            else:
                                Skill1= Skill1 - Skill
                                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, Name])
                                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SKILL debuff has wore off!```")
                                
                        elif LUCKTurns == 0:
                            Luck1 = 0
                            for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                                Luck1 = row[0]
                            if Luck > 0:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK buff has wore off!```")
                            else:
                                Luck1= Luck1 - Luck
                                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, Name])
                                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s LUCK debuff has wore off!```")
                        
                        elif SPDTurns == 0:
                            Spd1 = 0
                            Update == "True"
                            for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                                Spd1 = row[0]
                            if Spd > 0:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD buff has wore off!```")
                            else:
                                Spd1= Spd1 - Spd
                                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, Name])
                                for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                                    Name1 = row[0]
                                if Name1 == "":
                                    AAA = "A"
                                else: 
                                    AAA = "B"
                                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, Name])
                                await message.channel.send("```" + str(Name) + "'s SPD debuff has wore off!```")
                            
                        await message.channel.send("```" + Phase + " \n\nIts " + str(Name) + "'s turn!```")
        
        elif message.content == "!EndBattle":
            for x in VisitedEnemies:
                VisitedEnemies.remove(VisitedEnemies[0])
            for x in VisitedAllies:
                VisitedAllies.remove(VisitedAllies[0])
            for x in Not_VisitedAllies:
                Not_VisitedAllies.remove(Not_VisitedAllies[0])
            for x in Not_VisitedEnemies:
                Not_VisitedEnemies.remove(Not_VisitedEnemies[0])
            Phase = "Allies Phase"
            await message.channel.send("```Battle End! \nThe mod team will inform you about rewards and items for participating in the Battle/Seminar! Thank you all for participating!```")
            
        elif message.content == "!Buff" + mess[5:]:    
            count = 0
            Name= ""
            Type = ""
            amount = ""
            Turnx = ""
            currthing = 0
            currthing2 = 0
            AAA = ""
            Name1 = ""
            In = ""
            for char in mess: 
                if char == ' ':
                    count += 1
                elif count == 3:
                    amount += char + ""
                elif count == 1:
                    Name += char + ""
                elif count == 2:
                    Type += char + ""
                elif count == 4:
                    Turnx += char + ""
                    
            for row in cursor.execute("SELECT Name FROM InBattle Where Name = ?", [Name]):
                Name1 = row[0]
            if Name1 == "":
                AAA = "A"
            else: 
                AAA = "B"
                    
            if Type == "Health" or Type == "HP":
                Type == "HEALTH"
            elif Type == "Strength" or Type == "Str":
                Type == "STR"
            elif Type == "Magic" or Type == "Mag":
                Type == "MAG"
            elif Type == "Defense" or Type == "Def":
                Type == "DEF"
            elif Type == "Resistance" or Type == "Res":
                Type == "RES"
            elif Type == "Skill":
                Type == "SKILL"
            elif Type == "Spd" or Type == "Speed":
                Type == "SPD"
            elif Type == "Luck":
                Type == "LUCK"
            print(amount)
            for row in cursor.execute("SELECT Name FROM Buffs WHERE Name = ?", [Name]):
                In = row[0]
            if In == "":    
                cursor.execute('''INSERT INTO Buffs(NAME, STR, MAG, HEALTH, DEF, RES, SKILL, LUCK, STRTURNS, MAGTURNS, DEFTURNS, RESTURNS, HEALTHTURNS, SKILLTURNS, LUCKTURNS, SPD, SPDTURNS) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (Name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0))
            if int(amount) > 0:
                if Type == "STR":
                    for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "MAG":
                    for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "DEF":
                    for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "RES":
                    for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "HEALTH":
                    for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "SKILL":
                    for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "LUCK":
                    for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "SPD":
                    for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                        
                if Type == "STR":
                    for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "MAG":
                    for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "DEF":
                    for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "RES":
                    for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "HEALTH":
                    for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "SKILL":
                    for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "LUCK":
                    for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "SPD":
                    for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                
                currthing = int(currthing) + int(amount)
                currthing2 = int(currthing2) + int(amount)
                Turn = int(Turnx) + 1
                if Type == "HEALTH":
                    cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[currthing , Name])
                elif Type == "STR":
                    cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[currthing , Name])
                elif Type == "MAG":
                    cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[currthing , Name])
                elif Type == "DEF":
                    cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[currthing , Name])
                elif Type == "RES":
                    cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[currthing , Name])
                elif Type == "SKILL":
                    cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[currthing , Name])
                elif Type == "LUCK":
                    cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[currthing , Name])
                elif Type == "SPD":
                    cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[currthing , Name])
                if Type == "STR":
                    cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "MAG":
                    cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "DEF":
                    cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "RES":
                    cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "HEALTH":
                    cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "SKILL":
                    cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "LUCK":
                    cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "SPD":
                    Update = "True"
                    cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[currthing2, Name])
                    if AAA == "B":
                        cursor.execute("UPDATE InBattle SET SPD = ? WHERE Name = ?",[currthing2, Name])
                    elif AAA == "A":
                        cursor.execute("UPDATE Inbattleene SET SPD = ? WHERE Name = ?",[currthing2, Name])
                
                await message.channel.send("```" + str(Name) + "'s " + str(Type) + " has been buffed by " + str(amount) + " for " + str(Turn-1) + " turns! (If turns equal -1 this is a permanent buff!```")
                
                    
            else:
                if Type == "STR":
                    for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "MAG":
                    for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "DEF":
                    for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "RES":
                    for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "HEALTH":
                    for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "SKILL":
                    for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "LUCK":
                    for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                elif Type == "SPD":
                    for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[Name]):
                        currthing = row[0]
                
                if Type == "STR":
                    for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "MAG":
                    for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "DEF":
                    for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "RES":
                    for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "HEALTH":
                    for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "SKILL":
                    for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "LUCK":
                    for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                elif Type == "SPD":
                    for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[Name]):
                        currthing2 = row[0]
                
                currthing = int(currthing) + int(amount)
                currthing2 = int(currthing2) + int(amount)
                
                Turn1 = int(Turnx) + 1
                if Type == "HEALTH":
                    cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[currthing , Name])
                elif Type == "STR":
                    cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[currthing , Name])
                elif Type == "MAG":
                    cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[currthing , Name])
                elif Type == "DEF":
                    cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[currthing , Name])
                elif Type == "RES":
                    cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[currthing , Name])
                elif Type == "SKILL":
                    cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[currthing , Name])
                elif Type == "LUCK":
                    cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[currthing , Name])
                elif Type == "SPD":
                    cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[currthing , Name])
                if Type == "STR":
                    cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "MAG":
                    cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "DEF":
                    cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "RES":
                    cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "HEALTH":
                    cursor.execute("UPDATE Character SET HEALTH = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "SKILL":
                    cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "LUCK":
                    cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[currthing2, Name])
                elif Type == "SPD":
                    Update = "True"
                    cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[currthing2, Name])
                    if AAA == "B":
                        cursor.execute("UPDATE InBattle SET SPD = ? WHERE Name = ?",[currthing2, Name])
                    elif AAA == "A":
                        cursor.execute("UPDATE Inbattleene SET SPD = ? WHERE Name = ?",[currthing2, Name])
                amount1 = abs(int(amount))
                await message.channel.send("```" + str(Name) + "'s " + str(Type) + " has been debuffed by " + str(amount1) + " for " + str(Turn1-1) + " turns! (If turns equal -1 this is a permanent debuff!```")
        
        elif message.content == "!EXP" + mess[4:]:
            count = 0
            EXP = 0
            Name = ""
            amount = ""
            Level = ""
            for char in mess: 
                if char == ' ':
                    count += 1
                elif count == 1:
                    Name += char + ""
                elif count == 2:
                    amount += char + ""
            
            for row in cursor.execute("SELECT EXP FROM Character WHERE Name = ?",[Name]):
                EXP = row[0]
            for row in cursor.execute("SELECT Level FROM Character WHERE Name = ?",[Name]):
                Level = row[0]
            await message.channel.send("```" + str(Name) + " has earned  " + str(amount) + " EXP!```")
            EXP = EXP + int(amount)
            while EXP >= 100:
                if Level < 99:
                    Level = Level + 1
                    EXP = EXP - 100
                    await message.channel.send("```" + str(Name) + " has leveled up! They are now level " + str(Level) + "!```")
            cursor.execute("UPDATE Character SET Level = ? WHERE Name = ?",[Level , Name])
            cursor.execute("UPDATE Character SET EXP = ? WHERE Name = ?",[EXP , Name])
            
        elif message.content == "!Clearbattle" + mess[12:]:
            cursor.execute("DELETE FROM InBattle")
            cursor.execute("DELETE FROM Inbattleene")
            Not_VisitedAllies = []
            Not_VisitedEnemies = []
            VisitedAllies = []
            VisitedEnemies = []
            Str = 0
            Health = 0
            Def = 0
            Res = 0
            Mag = 0
            Skill = 0
            Luck = 0
            Spd = 0
            Name1 = ""
            for x in cursor.execute("SELECT Name FROM Buffs"):
                print(x[0])
                for row in cursor.execute("SELECT STR FROM Buffs WHERE Name = ?",[x[0]]):
                    Str = row[0]
                for row in cursor.execute("SELECT HEALTH FROM Buffs WHERE Name = ?",[x[0]]):
                    Health = row[0]
                for row in cursor.execute("SELECT DEF FROM Buffs WHERE Name = ?",[x[0]]):
                    Def = row[0]
                for row in cursor.execute("SELECT MAG FROM Buffs WHERE Name = ?",[x[0]]):
                    Mag = row[0]
                for row in cursor.execute("SELECT RES FROM Buffs WHERE Name = ?",[x[0]]):
                    Res = row[0]
                for row in cursor.execute("SELECT SKILL FROM Buffs WHERE Name = ?",[x[0]]):
                    Skill = row[0]
                for row in cursor.execute("SELECT LUCK FROM Buffs WHERE Name = ?",[x[0]]):
                    Luck = row[0]
                for row in cursor.execute("SELECT SPD FROM Buffs WHERE Name = ?",[x[0]]):
                    Spd = row[0]
                print(Str)
                print(Mag)
                print(Health)
                print(Def)
                print(Res)
                print(Spd)
                print(Skill)
                print(Luck)
                Str1 = 0
                for row in cursor.execute("SELECT STR FROM Character WHERE Name = ?",[x[0]]):
                    Str1 = row[0]
                Str1= Str1 - Str
                cursor.execute("UPDATE Character SET STR = ? WHERE Name = ?",[Str1, x[0]])
                cursor.execute("UPDATE Buffs SET STR = ? WHERE Name = ?",[0, x[0]])
                                
                Mag1 = 0
                for row in cursor.execute("SELECT MAG FROM Character WHERE Name = ?",[x[0]]):
                    Mag1 = row[0]
                Mag1= Mag1 - Mag
                cursor.execute("UPDATE Character SET MAG = ? WHERE Name = ?",[Mag1, x[0]])
                cursor.execute("UPDATE Buffs SET MAG = ? WHERE Name = ?",[0, x[0]])
                        
                Def1 = 0
                for row in cursor.execute("SELECT DEF FROM Character WHERE Name = ?",[x[0]]):
                    Def1 = row[0]
                Def1= Def1 - Def
                cursor.execute("UPDATE Character SET DEF = ? WHERE Name = ?",[Def1, x[0]])
                cursor.execute("UPDATE Buffs SET DEF = ? WHERE Name = ?",[0, x[0]])
                        
                Res1 = 0
                for row in cursor.execute("SELECT RES FROM Character WHERE Name = ?",[x[0]]):
                    Res1 = row[0]
                Res1= Res1 - Res
                cursor.execute("UPDATE Character SET RES = ? WHERE Name = ?",[Res1, x[0]])
                cursor.execute("UPDATE Buffs SET RES = ? WHERE Name = ?",[0, x[0]])
                            
                Health1 = 0
                for row in cursor.execute("SELECT HT FROM Character WHERE Name = ?",[x[0]]):
                    Health1 = row[0]
                Health1= Health1 - Health
                cursor.execute("UPDATE Character SET HT = ? WHERE Name = ?",[Health1, x[0]])
                cursor.execute("UPDATE Buffs SET HEALTH = ? WHERE Name = ?",[0, x[0]])
                                
                Skill1 = 0
                for row in cursor.execute("SELECT SKILL FROM Character WHERE Name = ?",[x[0]]):
                    Skill1 = row[0]
                Skill1= Skill1 - Skill
                cursor.execute("UPDATE Character SET SKILL = ? WHERE Name = ?",[Skill1, x[0]])
                cursor.execute("UPDATE Buffs SET SKILL = ? WHERE Name = ?",[0, x[0]])
                                
                Luck1 = 0
                for row in cursor.execute("SELECT LUCK FROM Character WHERE Name = ?",[x[0]]):
                    Luck1 = row[0]
                Luck1= Luck1 - Luck
                cursor.execute("UPDATE Character SET LUCK = ? WHERE Name = ?",[Luck1, x[0]])
                cursor.execute("UPDATE Buffs SET LUCK = ? WHERE Name = ?",[0, x[0]])
                        
                Spd1 = 0
                Update = "True"
                for row in cursor.execute("SELECT SPD FROM Character WHERE Name = ?",[x[0]]):
                    Spd1 = row[0]
                Spd1= Spd1 - Spd
                cursor.execute("UPDATE Character SET SPD = ? WHERE Name = ?",[Spd1, x[0]])
                cursor.execute("UPDATE Buffs SET SPD = ? WHERE Name = ?",[0, x[0]])
            await message.channel.send("```The battlefield has settled!```")
        elif message.content == "!Rob" + mess[4:]:
            count = 0
            Name = ""
            moneyc = 0
            monz = ""
            for char in mess: 
                if char == ' ':
                    count = count + 1              
                elif count == 1:
                     Name += char + ""      
                elif count == 2:
                     monz += char + ""
            for row in cursor.execute("SELECT MONEY, Name FROM Chargold WHERE Name = ?",[Name]):
                moneyc = row[0]
            moneyc -= int(monz)
            cursor.execute("UPDATE Chargold SET MONEY = ? WHERE Name = ?",[moneyc, Name])
            await message.channel.send("```" + str(Name) + " has been robbed and lost "+ str(monz) + " gold! \nThey now have " + str(moneyc) + " gold in total!```")
                
        conn.commit()
        cursor.close()
client.run(token)