import random
import utils


def test_chars():
    chars = utils.get_characters_collection()
    for c in chars:
        print(c.name, c.atk, c.defce, c.pv)

def test_mons():
    mons = utils.get_monsters_collection()
    for m in mons:
        print(m.name, m.atk, m.defce, m.pv)

def choose_squad():
    chars = utils.get_characters_collection()
    squad = []

    while len(squad) < 3:
        print("\nYour squad : ")
        for i, c in enumerate(squad, start=1): #i et c sont me permettent de recup les perso et leur noms je dois finir cette partie avant de passer à la suite 
            print(f"{i} - {c.name} Atk : {c.atk} Def:{c.defce} pv{c.pv}")
            print("\nAvailable characters:")
            for i, c in enumerate(chars, start=1):
                print(f"{i} - {c.name} Atk:{c.atk} Def:{c.defce} Pv:{c.pv}")

        try:
            choice = int(input("choose a character 1~10 : "))
            chosen = chars[choice -1]
            if chosen in squad:
                print("already in your squad bro")

            else:
                squad.append(chosen)#ici en gros on ajoute les perso additionnel avec append
        except(ValueError, IndexError):
            print("Ain't no way boy stop trolling") # on evite les erreurs d'input avec le try except (a re tester parce que je suis pas sur d'avoir capté)
            
        
    return squad

#la version automatique du jeu fonctionne ou presque maintenant je peux faire un mini jeu et proposer des actions

def make_a_move_for_chars(c):
    print(f"\n{c.name}'s turn - Pv: {c.pv}")
    print("1/Attack")
    print("2/Block")
    choice = input("Choose a move: ")
    return choice

def Attack_move(c, monster):
    dmg = max(0, c.atk - monster.defce)
    monster.take_damage(dmg)
    print(f"{c.name} attack and deals {dmg} damage. Pv monster = {monster.pv}")

def Block_move(c, monster):
    dmg = max(0, monster.atk - c.defce)
    c.take_damage(dmg)
    print(f"{c.name} block and reduce damage but still takes {dmg} damage. pv {c.name} = {c.pv}")
    
def fight_wave(squad):
    monsters = utils.get_monsters_collection()
    monster = random.choice(monsters)
    print(f"\nA {monster.name} Appeared, break his kneecaps!!! Atk:{monster.atk} def:{monster.defce} pv:{monster.pv}")
#ici faut faire les combats je vais essayer de faire des tours j'ai pas encore la logique (peut être avec un for ou while)

#Ici version avec les choix (a tester):
    for c in squad:
        if c.pv <= 0 or monster.pv <= 0:
            continue # def de Continue : L'instruction continue en Python permet de sauter le reste du code dans l'itération actuelle d'une boucle et de passer directement à l'itération suivante.
        
        move = make_a_move_for_chars(c)

        if move == "1":
            Attack_move(c, monster)
        elif move == "2":
            Block_move(c, monster)
        else:
            print("my brother/sister in christ you only got two move to choose from, you just skip your turn...")

    if monster.pv <= 0:
        print("Monster is slain, gg")
        return True
    
    living_chars = [c for c in squad if c.pv > 0]
    
    if not living_chars:
        return False
    
    target = random.choice(living_chars)
    dmg = max(0, monster.atk - target.defce)
    target.take_damage(dmg)
    print(f"{monster.name} attack {target.name} and deals {dmg} damage. pv {target.name} = {target.pv}")

    if all(c.pv <= 0 for c in squad):
        return False
    
    return True

#La version sans choix
    for c in squad:
        if c.pv > 0 and monster.pv > 0:
            dmg = max(0, c.atk - monster.defce)
            monster.take_damage(dmg)
            print(f"{c.name} inflict {dmg} damage. Pv monster = {monster.pv}")

    if monster.pv <= 0:
            print("A monster has been sacri... slain.. good job")
            return True # ça c'est en cas de victoire contre un mob
        
    #attaque du mob
    living_chars = [c for c in squad if c.pv > 0]
    if not living_chars:
        return False
        
    target = random.choice(living_chars)
    dmg = max(0, monster.atk - target.defce)
    target.take_damage(dmg)
    print(f"{monster.name} attack {target.name} and deals {dmg} damage. Pv {target.name} = {target.pv}")

    # un check pour voir si l'equipe est ko

    if all(c.pv <= 0 for c in squad):
        return False
        
    return True
        
def start_game():
    username = input("Name of the playa : ")
    squad = choose_squad()

    wave = 0
    alive = True
    while alive:
        alive = fight_wave(squad)
        if alive:
            wave += 1
            print(f"wave {wave} cleared!")
        else:
            print("it can bleed... it can dieeee.... you must get good")

        
    utils.save_score(username, wave)
    print(f"game over,  wave survived : {wave}")

def show_leaderboard():
    score = utils.get_top_score()
    print("\n Leaderboard ")
    for i, s in enumerate(score, start=1):
        print(f"{i}. {s['username']} - {s['waves']} waves")