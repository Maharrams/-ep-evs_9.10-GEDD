def noteikt_vecuma_grupu():
    """
    Programma nosaka lietotāja vecuma grupu pamatojoties uz ievadīto vecumu.
    Vecuma robežas:
    - Bērns: no 0 līdz 12 gadiem (ieskaitot)
    - Pusaudzis: no 13 līdz 17 gadiem (ieskaitot)
    - Pieaugušais: no 18 līdz 64 gadiem (ieskaitot)
    - Seniors: 65 gadi un vecāki
    """
    ievade = input("Lūdzu, ievadi savu vecumu: ")

    # Pārbaudām, vai ievade nav tukša
    if not ievade.strip():
        print("Kļūda: Ievade nedrīkst būt tukša.")
        return

    try:
        vecums = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli.")
        return

    # Pārbaudām negatīvus skaitļus
    if vecums < 0:
        print("Kļūda: Vecums nevar būt negatīvs skaitlis.")
    elif vecums <= 12:
        print("Bērns")
    elif vecums <= 17:
        print("Pusaudzis")
    elif vecums <= 64:
        print("Pieaugušais")
    else:
        print("Seniors")

if __name__ == "__main__":
    noteikt_vecuma_grupu()