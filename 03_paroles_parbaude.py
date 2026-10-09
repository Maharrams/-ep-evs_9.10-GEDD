def paroles_parbaude():
    """
    Programma pārbauda lietotāja paroli ar maksimāli 3 mēģinājumiem,
    izmantojot while ciklu.
    """
    PAREIZA_PAROLE = "banan3000robokop"
    atlikusie_meginajumi = 3

    while atlikusie_meginajumi > 0:
        ievade = input("Ievadi paroli: ")

        if ievade == PAREIZA_PAROLE:
            print("Piekļuve atļauta")
            return
        else:
            atlikusie_meginajumi -= 1
            if atlikusie_meginajumi > 0:
                print(f"Nepareiza parole! Atlikušie mēģinājumi: {atlikusie_meginajumi}")
            else:
                print("Piekļuve bloķēta")

if __name__ == "__main__":
    paroles_parbaude()