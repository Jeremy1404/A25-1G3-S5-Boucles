def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    # TODO : Créer 3 listes

    # TODO : Pour 3 ordinateur
        # TODO : Demander temp, poussière, humidité
        # TODO : Mettres les 3 valeurs dans leurs listes

    try:
        temp = int(input("Entrer le température : "))
        poussiere = input("Entrer le niveau de poussière : ")
        humidite = float(input("Entrer le niveau d'humidité : "))

    except ValueError:
        print("Votre réponse doit être un chiffre !")
    except NameError:
        print("Veuillez entrer une réponse")


    # TODO : Pour les 3 ordi
        # TODO : Utilliser la fonction et afficher le resultat
    print(environnement_optimal(temp, poussiere, humidite))
