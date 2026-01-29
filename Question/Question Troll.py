questions_logique = [
    {
        "id": 1,
        "question": "Si tu as 5 barres de chocolat dans un bol et que t’en prends 3. Combien il t’en reste ?",
        "reponse": "5",
        "explication": "Le bol est à toi, donc même si tu en prends 3 dans ta main, tu possèdes toujours les 5 barres."
    },
    {
        "id": 2,
        "question": "Si tu entres dans un restaurant et qu’il y a 3 personnes de 30 ans et 6 personnes de 40 ans. Combien y’en a-t-il au total ?",
        "reponse": "10",
        "explication": "Il y a les 9 clients plus toi qui viens d'entrer."
    },
    {
        "id": 3,
        "question": "Certains mois ont 31 jours, d'autres en ont 30. Combien de mois en ont 28 ?",
        "reponse": "12",
        "explication": "Tous les mois de l'année ont au moins 28 jours."
    },
    {
        "id": 4,
        "question": "À combien est égale la multiplication de tous les chiffres du numéro de téléphone ?",
        "reponse": "0",
        "explication": "N'importe quel nombre multiplié par 0 (présent dans tous les numéros) est égal à 0."
    },
    {
        "id": 5,
        "question": "Qu’est-ce qu’on met dans un toaster ?",
        "reponse": "pain",
        "explication": "On ne met pas de toasts (ce sont des pains déjà grillés) mais du pain."
        
    },
    {
        "id": 6,
        "question": "Si un avion s'écrase sur la frontière entre la France et la Belgique, où enterre-t-on les rescapés ?",
        "reponse": "nulle part",
        "explication": "On n'enterre pas les rescapés, ils sont vivants !"
    },
    {
        "id": 7,
        "question": "Avant que le Mont Everest ne soit découvert, quel était le plus haut sommet du monde ?",
        "reponse": "Everest",
        "explication": "Il était déjà le plus haut, même si personne ne l'avait encore découvert."
    },
    {
        "id": 8,
        "question": "Une femme a deux fils qui sont nés le même jour, à la même heure, du même mois et de la même année, mais ce ne sont pas des jumeaux. Comment est-ce possible ?",
        "reponse": "triplés",
        "explication": "Ils font partie d'une naissance de triplés (ou plus), il y a donc un troisième enfant."
    },
    {
        "id": 9,
        "question": "Si tu participes à une course et que tu doubles le dernier, à quelle position es-tu ?",
        "reponse": "impossible",
        "explication": "Tu ne peux pas doubler le dernier, car si tu es derrière lui, c'est toi qui es dernier !"
    },
    {
        "id": 10,
        "question": "Combien est égale la moitié de deux plus deux ?",
        "reponse": "3",
        "explication": "La moitié de deux est un, plus deux fait trois."
    },
    {
       
        "id": 11,
        "question": "Qu'est-ce qui monte et qui descend, mais qui reste toujours à la même place ?",
        "reponse": "escalier",
        "explication": "Un escalier ne bouge pas physiquement, mais on l'utilise pour monter et descendre."
    },
    {
        "id": 12,
        "question": "Si tu as un seau rempli à moitié d'eau et que tu y ajoutes un autre seau rempli à moitié d'eau, combien de seaux d'eau as-tu maintenant ?",
        "reponse": "2",
        "explication": "Tu as toujours deux seaux, chacun rempli à moitié."
    },
    {
        "id": 13,
        "question": "Combien y'a t-il d'heure dans une semaine ?",
        "réponse": "168" ,
    },
    {  "id": 14,
        "question" : "Je pense à un nombre, devine le ?",   
        "réponse": "12",
    },
    {
     "id": 15,
     "question" : "Combien il y a de lettre dans ce mot : ooooooooooooooooooooooooooooooooooooo",
     "réponse" : "37",
     "explication" : "Il faut savoir compter ! "
     },
    
]

import time

def lancer_quiz(liste_questions):
    score = 0
    print("--- BIENVENUE AU QUIZ DE LOGIQUE ---")
    
    for q in liste_questions:
        print(f"\nQuestion : {q['question']}")
        reponse_user = input("Ta réponse : ").lower().strip()
        
        if q['reponse'].lower() in reponse_user:
            print("✅ Bravo ! C'est logique.")
            score += 1
        else:
            print(f"❌ Dommage ! La réponse était : {q['reponse']}")
        
        print(f"L'astuce : {q['explication']}")
        time.sleep(1)

    print(f"\n--- Score final : {score}/{len(liste_questions)} ---")

lancer_quiz(questions_logique)
