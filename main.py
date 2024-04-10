import json

if __name__ == "__main__":
    from my_classes import Person, Experiment

    repetition = True

    while repetition == True:

        #Erstellen des Supervisors mit der Klasse Person
        print("Geben Sie die benötigten Daten des Supervisors ein: ")
        supervisor1 = Person(input("Vorname: "), input("Nachname: "), input("Geschlecht (male / female): "), int(input("Alter: ")))
        
        #Erstellen des Subjects mit der Klasse Person
        print("Geben Sie die benötigten Daten des Subjects ein: ")
        subject1 = Person(input("Vorname: "), input("Nachname: "), input("Geschlecht (male / female): "), int(input("Alter: ")))

        #Erstellen des Experiments:
        experiment_01 = Experiment(input("Name des Experiments: "), input("Datum: "), supervisor1.__dict__, subject1.__dict__)

        #Abfrage was gespeichert werden soll
        print("Welche der eingegeben Daten wollen Sie in einer json-Datei speichern? (Supervisor / Subject / Experiment / Exit)")
        while True:
            decision = input("Geben Sie ihre Auswahl, wie oben genannt ein: ")
            if decision == "Supervisor":
                supervisor1.save()
            elif decision == "Subject":
                subject1.save()
            elif decision == "Experiment":
                experiment_01.save()
            elif decision == "Exit":
                break
            else:
                print("Falsche Eingabe, versuchen Sie erneut!!")
                continue

        #Soll das Programm neu gestartet werden damit weitere Daten eingegeben werden können?
        
        while True:
            decision = input("Wollen Sie weitere Daten eingeben? (Ja / Nein): ")
            if decision == "Ja":
                repetition = True
                break
            elif decision == "Nein":
                repetition = False
                print("Until next Time!")
                break
            else:
                print("Falsche Eingabe, versuchen Sie erneut!!")
                continue