def izveidot_reizinasanas_tabulu():
    """
    Programma pieprasa veselu skaitli un ar for ciklu 
    izvada tā reizināšanas tabulu no 1 līdz 10.
    """
    ievade = input("Lūdzu, ievadi veselu skaitli: ")

    # Pārbaudām, vai ievade nav tukša
    if not ievade.strip():
        print("Kļūda: Ievade nedrīkst būt tukša.")
        return

    try:
        skaitlis = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu.")
        return

    print(f"\nSkaitļa {skaitlis} reizināšanas tabula:")
    for i in range(1, 11):
        rezultats = skaitlis * i
        print(f"{skaitlis} x {i} = {rezultats}")

if __name__ == "__main__":
    izveidot_reizinasanas_tabulu()