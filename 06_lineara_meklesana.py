def linearā_meklēšana():
    """
    Programma veic lineāro meklēšanu dotajā sarakstā un atrod
    gan pirmo indeksu, gan visus indeksus, kuros vērtība atrasta.
    """
    skaitli = [4, 7, 2, 9, 7, 1]
    
    ievade = input("Ievadi meklējamo skaitli: ")

    # Pārbaudām, vai ievade nav tukša
    if not ievade.strip():
        print("Kļūda: Ievade nedrīkst būt tukša.")
        return

    try:
        meklejamo = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli.")
        return

    pirmais_indekss = -1
    visi_indeksi = []

    # Ar ciklu un enumerate pārbaudām saraksta elementus pēc kārtas
    for indekss, vertiba in enumerate(skaitli):
        if vertiba == meklejamo:
            if pirmais_indekss == -1:
                pirmais_indekss = indekss
            visi_indeksi.append(indekss)

    # Izvadam rezultātus atbilstoši prasībām
    if pirmais_indekss != -1:
        print(f"Pirmais indekss, kurā skaitlis atrasts: {pirmais_indekss}")
        print(f"Visi indeksi (papildu līmenis): {visi_indeksi}")
    else:
        print("Nav atrasts")

if __name__ == "__main__":
    linearā_meklēšana()