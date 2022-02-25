from men import Man
from women.Woman import Woman

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
        instance = Man.Man(None, None, None, None)
        while picked != 6:
            print("   # ******************************************** #")
            print("   # 1. Add a man ")
            print("   # 2. Edit by matricule ")
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
        instance = Woman(None, None, None, None)
        while picked != 6:
            print("   # ******************************************** #")
            print("   # 1. Add a women ")
            print("   # 2. Edit by cin ")
            print("   # 3. Delete by cin ")
            print("   # 4. Display by cin ")
            print("   # 5. Display all ")
            print("   # 6. Back <- ")
            print("   # ___________________________________________ #")
            picked = int(input("  ==> : "))
            # -----------------------------------------------------------------------------------------
            if picked == 1:
                print(" ------ Add Operation ------- ")
                result = instance.saisir()
                instance.save(Women, result)
                print(" ------ End Operation ------- ")

            if picked == 2:
                print(" ------ Edit Operation ------- ")
                cin = input(" Entrez le cin de la personne : ")
                instance.edit(Women, cin)
                print(" ------ End Operation ------- ")

            if picked == 3:
                print(" ------ Delete Operation ------- ")
                cin = input(" Entrez le cin de la personne : ")
                instance.delete(Women, cin)
                print(" ------ End Operation ------- ")

            if picked == 4:
                print(" ------ Display by Cin ------- ")
                cin = input(" Entrez le cin de la personne : ")
                instance.display_by(Women, cin)
                print(" ------ End Operation ------- ")

            if picked == 5:
                print(" ------ Display All ------- ")
                instance.display_all(Women)
                print(" ------ End Operation ------- ")
