questions_logique = [
    {
        "id": 1,
        "question": "Si tu as 5 barres de chocolat dans un bol et que t’en prends 3. Combien il t’en reste ?",
        "choix": ["2", "3", "5", "0"],
        "reponse": "5",
        "explication": "Le bol est à toi, donc même si tu en prends 3 dans ta main, tu possèdes toujours les 5 barres.",
    },
    {
        "id": 2,
        "question": "Si tu entres dans un restaurant et qu’il y a 3 personnes de 30 ans et 6 personnes de 40 ans. Combien y’en a-t-il au total ?",
        "choix": ["9", "10", "6", "12"],
        "reponse": "10",
        "explication": "Il y a les 9 clients plus toi qui viens d'entrer.",
    },
    {
        "id": 3,
        "question": "Certains mois ont 31 jours, d'autres en ont 30. Combien de mois en ont 28 ?",
        "choix": ["1", "12", "6", "0"],
        "reponse": "12",
        "explication": "Tous les mois de l'année ont au moins 28 jours.",
    },
    {
        "id": 4,
        "question": "À combien est égale la multiplication de tous les chiffres du numéro de téléphone ?",
        "choix": ["0", "1", "Impossible à savoir", "10"],
        "reponse": "0",
        "explication": "N'importe quel nombre multiplié par 0 est égal à 0.",
    },
    {
        "id": 5,
        "question": "Qu’est-ce qu’on met dans un toaster ?",
        "choix": ["Pain", "Toast", "Biscotte", "Rien"],
        "reponse": "pain",
        "explication": "On met du pain, pas des toasts.",
    },
    {
        "id": 6,
        "question": "Si un avion s'écrase sur la frontière entre la France et la Belgique, où enterre-t-on les rescapés ?",
        "choix": ["France", "Belgique", "Les deux", "Nulle part"],
        "reponse": "nulle part",
        "explication": "On n'enterre pas les rescapés.",
    },
    {
        "id": 7,
        "question": "Avant que le Mont Everest ne soit découvert, quel était le plus haut sommet du monde ?",
        "choix": ["K2", "Mont Blanc", "Everest", "Aucun"],
        "reponse": "everest",
        "explication": "Il était déjà le plus haut.",
    },
    {
        "id": 8,
        "question": "Une femme a deux fils nés le même jour, même heure, même année, mais ce ne sont pas des jumeaux. Comment est-ce possible ?",
        "choix": ["Adoption", "Triplés", "Faux jumeaux", "Erreur"],
        "reponse": "triplés",
        "explication": "Ils font partie de triplés.",
    },
    {
        "id": 9,
        "question": "Si tu participes à une course et que tu doubles le dernier, à quelle position es-tu ?",
        "choix": ["Dernier", "Avant-dernier", "Premier", "Impossible"],
        "reponse": "impossible",
        "explication": "Tu ne peux pas doubler le dernier.",
    },
    {
        "id": 10,
        "question": "Combien est égale la moitié de deux plus deux ?",
        "choix": ["2", "3", "4", "1"],
        "reponse": "3",
        "explication": "La moitié de deux est un, plus deux fait trois.",
    },
]


def lancer_quiz(liste_questions):
    score = 0
    print("--- BIENVENUE AU QUIZ DE LOGIQUE (QCM) ---")

    for q in liste_questions:
        print(f"\nQuestion : {q['question']}")

        # Affichage des choix
        for i, choix in enumerate(q["choix"], start=1):
            print(f"{i}. {choix}")

        # Lecture de la réponse utilisateur
        choix_user = input("Ton choix (1-4) : ").strip()

        # Vérification que l'utilisateur tape bien un chiffre entre 1 et 4
        if choix_user.isdigit() and 1 <= int(choix_user) <= 4:
            reponse_user = q["choix"][int(choix_user) - 1].lower()
        else:
            reponse_user = ""

        # Vérification de la bonne réponse
        if reponse_user == q["reponse"].lower():
            print("✅ Bravo !")
            score += 1
        else:
            print(f"❌ Mauvaise réponse ! La bonne était : {q['reponse']}")

        print(f"Astuce : {q['explication']}")

    print(f"\n--- Score final : {score}/{len(liste_questions)} ---")
