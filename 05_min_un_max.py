def atrast_min_max():
    """
    Programma pieprasa skaitļu daudzumu, ļauj ievadīt skaitļus pa vienam 
    un atrod mazāko un lielāko vērtību, izmantojot algoritmiskos salīdzinājumus.
    """
    ievade_skaits = input("Cik skaitļus tu vēlies ievadīt? ")

    # Pārbaudām, vai ievade nav tukša
    if not ievade_skaits.strip():
        print("Kļūda: Ievade nedrīkst būt tukša.")
        return

    try:
        n = int(ievade_skaits)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli.")
        return

    # Pārbaudām, vai skaitļu skaits ir pozitīvs
    if n <= 0:
        print("Kļūda: Skaitļu skaitam ir jābūt pozitīvam (lielākam par 0).")
        return

    mazakais = None
    lielakais = None

    # Cikls skaitļu ievadei un salīdzināšanai
    for i in range(1, n + 1):
        ievade_skaitlis = input(f"Ievadi {i}. skaitli: ")
        
        if not ievade_skaitlis.strip():
            print("Kļūda: Skaitļa ievade nedrīkst būt tukša.")
            return

        try:
            skaitlis = float(ievade_skaitlis)
        except ValueError:
            print("Kļūda: Lūdzu, ievadi derīgu skaitli.")
            return

        # Pirmajā iterācijā saglabājam pirmo skaitli kā pagaidu min un max
        if mazakais is None or lielakais is None:
            mazakais = skaitlis
            lielakais = skaitlis
        else:
            # Salīdzinām katru nākamo skaitli ar esošo mazāko un lielāko
            if skaitlis < mazakais:
                mazakais = skaitlis
            if skaitlis > lielakais:
                lielakais = skaitlis

    print(f"\nRezultāts:")
    print(f"Mazākais skaitlis: {mazakais:g}")
    print(f"Lielākais skaitlis: {lielakais:g}")

if __name__ == "__main__":
    atrast_min_max()