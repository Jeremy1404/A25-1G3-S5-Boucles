import pytest # importer le module pytest pour faire nos tests unitaire
from ExDebug1 import environnement_optimal # importer la fonction de notre autre fichier

# test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    #Arrange : préparer les variables d'entrer et les résultats attendus
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #Act : appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert : vérifier le resultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal_2():
    #Arrange : préparer les variables d'entrer et les résultats attendus
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act : appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert : vérifier le resultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal_3():
    #Arrange : préparer les variables d'entrer et les résultats attendus
    temperature = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    #Act : appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert : vérifier le resultat
    assert resultat_attendu == resultat_obtenu

# test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal_4():
    #Arrange : préparer les variables d'entrer et les résultats attendus
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    #Act : appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert : vérifier le resultat
    assert resultat_attendu == resultat_obtenu

