from men import Man

choice = 0
Men = []
Women = []

while choice != 3:
    print("   # ******************************************** #")
    print("   #  1. Man ")
    print("   #  2. Woman ")
    print("   #  3. Exit |<- ")
    print("   # ____________________________________________ #")
    choice = int(input("  ==> : "))

    if choice == 1:
        picked = 0
        instance = Man.Man()
        while picked != 6:
            print("   # ******************************************** #")
            print("   # 1. Add a man ")
            print("   # 2. Edit a man ")
            print("   # 3. Delete by matricule ")
            print("   # 4. Display by matricule ")
            print("   # 5. Display all ")
            print("   # 6. Back <- ")
            print("   # ___________________________________________ #")
            picked = int(input("  ==> : "))
            # -----------------------------------------------------------------------------------------
            if picked == 1:
                print(" ------ Add Operation ------- ")
                result = instance.saisir()
                instance.save(Men, result)
                print(" ------ End Operation ------- ")

            if picked == 2:
                print(" ------ Edit Operation ------- ")
                matricule = input(" Entrez le matricule de la personne : ")
                instance.edit(Men, matricule)
                print(" ------ End Operation ------- ")

            if picked == 3:
                print(" ------ Delete Operation ------- ")
                matricule = input(" Entrez le matricule de la personne : ")
                instance.delete(Men, matricule)
                print(" ------ End Operation ------- ")

            if picked == 4:
                print(" ------ Display by Matricule ------- ")
                matricule = input(" Entrez le matricule de la personne : ")
                instance.display_by(Men, matricule)
                print(" ------ End Operation ------- ")

            if picked == 5:
                print(" ------ Display All ------- ")
                instance.display_all(Men)
                print(" ------ End Operation ------- ")
# ------------------------------------------------------------------------------------------------------------------
    elif choice == 2:
        picked = 0
        while picked != 6:
            print("   # ******************************************** #")
            print("   # 1. Add a woman ")
            print("   # 2. Edit a woman ")
            print("   # 3. Delete a woman ")
            print("   # 4. Display by first name ")
            print("   # 5. Display all ")
            print("   # 6. Back <- ")
            print("   # ___________________________________________ #")
            picked = int(input("  ==> : "))
            # -----------------------------------------------------------------------------------------
            if picked == 1:
                print(" Add a man was picked ")
