import random

# ----------------------------
# Données du jeu
# ----------------------------

joueur_pv = 100
ia_pv = 100
degats = 15

# ----------------------------
# Fonction IA
# ----------------------------

def ia_repond(difficulte="normal"):
    if difficulte == "facile":
        chance = 0.4
    elif difficulte == "difficile":
        chance = 0.8
    else:
        chance = 0.6
        return random.random() < chance

# ----------------------------
# Boucle principale du jeu
# ----------------------------

print("⚔️ Bienvenue dans le jeu de combat par questions ! ⚔️")

while joueur_pv > 0 and ia_pv > 0:
question = random.choice(questions)


import random

class SimpleFightingAI:
    def decide_action(self, player_action, distance):
        """
        player_action: 'attack', 'defend', 'idle'
        distance: 'close', 'far'
        """

        if player_action == "attack":
            return random.choice(["defend", "backward"])

        if player_action == "defend":
            return "attack"

        if distance == "far":
            return "forward"

        return random.choice(["attack", "defend"])

# ----------------------------
# Fin du jeu
# ----------------------------

if joueur_pv <= 0:
print("\n💀 Tu as perdu le combat...")
else:
print("\n🏆 Victoire ! Tu as battu l'IA !")