def aprekinat_summu():
    """
    Programma aprēķina visu veselo skaitļu summu no 1 līdz n,
    izmantojot for ciklu un pašu uzrakstītu summēšanas algoritmu.
    """
    ievade = input("Lūdzu, ievadi veselu pozitīvu skaitli n: ")

    # Pārbaudām, vai ievade nav tukša
    if not ievade.strip():
        print("Kļūda: Ievade nedrīkst būt tukša.")
        return

    try:
        n = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu.")
        return

    # Pārbaudām, vai skaitlis ir pozitīvs
    if n <= 0:
        print("Kļūda: Skaitlim ir jābūt pozitīvam (lielākam par 0).")
        return

    # Aprēķinām summu ar for ciklu
    summa = 0
    for i in range(1, n + 1):
        summa += i

    print(f"Skaitļu summa no 1 līdz {n} ir: {summa}")

if __name__ == "__main__":
    aprekinat_summu()