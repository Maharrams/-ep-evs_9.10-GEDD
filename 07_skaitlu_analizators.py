def skaitlu_analizators():
    print("--- Skaitļu analizators ---")
    
    # 1. Pajautā, cik skaitļus lietotājs ievadīs
    try:
        n = int(input("Cik skaitļus jūs vēlaties ievadīt? "))
    except ValueError:
        print("Kļūda: Lūdzu, ievadiet veselu skaitli!")
        return

    # Pārbaude, ja skaitļu skaits ir 0 vai negatīvs
    if n <= 0:
        print("Skaitļu skaitam jābūt lielākam par 0.")
        return

    skaitli = []
    
    # 2. Cikls katra skaitļa pieprasīšanai
    for i in range(n):
        while True:
            try:
                skaitlis = float(input(f"Ievadiet {i+1}. skaitli: "))
                skaitli.append(skaitlis)
                break
            except ValueError:
                print("Nederīga vērtība. Lūdzu, ievadiet skaitli atkārtoti!")

    # 3. Datu apstrāde un statistika
    summa = sum(skaitli)
    pozitivi = sum(1 for x in skaitli if x > 0)
    negativi = sum(1 for x in skaitli if x < 0)
    nulles = sum(1 for x in skaitli if x == 0)
    
    # Pāra un nepāra skaitļi parasti attiecas uz veseliem skaitļiem
    para = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 == 0)
    nepara = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 != 0)
    
    vid_aritmetiskais = summa / n

    # 4. Rezultātu izvade
    print("\n" + "="*30)
    print("ANALĪZES REZULTĀTI:")
    print("="*30)
    print(f"Ievadīto skaitļu summa: {summa}")
    print(f"Pozitīvo skaitļu skaits: {pozitivi}")
    print(f"Negatīvo skaitļu skaits: {negativi}")
    print(f"Nulļu skaits: {nulles}")
    print(f"Pāra skaitļu skaits (veseliem skaitļiem): {para}")
    print(f"Nepāra skaitļu skaits (veseliem skaitļiem): {nepara}")
    print(f"Vidējais aritmētiskais: {vid_aritmetiskais}")
    print("="*30)

if __name__ == "__main__":
    skaitlu_analizators()