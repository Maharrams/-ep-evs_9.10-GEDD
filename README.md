# Programmēšanas un algoritmu ĢEDD

**Datums:** 09.10.2026.  
**Programmēšana I:** Gitea repozitorijs, versiju vēsture un Python pamatkonstrukcijas  
**Algoritmu pamati:** vienkāršu algoritmu īstenošana Python programmās, izsekošana un testēšana

## Sasniedzamie rezultāti

### Programmēšana I

Es izveidoju Gitea repozitoriju, pievienoju README un Python failus, saglabāju darbu loģiskos `commit` posmos un nosūtu jaunāko versiju uz serveri. Programmās izmantoju `if`, `for` un `while`.

### Algoritmu pamati

Es uzrakstu Python programmu, kas īsteno vienkāršu algoritmu, izsekoju tās mainīgo vērtības un pārbaudu programmu ar tipisku, robežas un nederīgu ievadi.

# AI sarunašana 

1. uzdevums — Vecuma grupa
Izveido programmu, kas:

pieprasa lietotāja vecumu;
ar if, elif un else nosaka grupu;
izvada vienu no rezultātiem: bērns, pusaudzis, pieaugušais vai seniors.
Izvēlies un kodā skaidri norādi vecuma robežas.

Fails: 01_vecuma_grupa.py
Ieteiktais commit: Pievienots vecuma grupas uzdevums ar if

Pārbaudes: vecumi tieši pirms un pēc katras robežas, 0, negatīvs skaitlis un tukša ievade.

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

    2. uzdevums — Reizināšanas tabula
Izveido programmu, kas pieprasa vienu veselu skaitli un ar for ciklu izvada tā reizināšanas tabulu no 1 līdz 10.

Piemērs, ja ievadīts 4:

4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
Fails: 02_reizinasanas_tabula.py
Ieteiktais commit: Pievienota reizināšanas tabula ar for

Pārbaudes: pozitīvs skaitlis, 0, 1, negatīvs skaitlis un teksts skaitļa vietā.

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

    3. uzdevums — Paroles pārbaude
Izveido programmu, kurā pareizā parole ir saglabāta mainīgajā. Lietotājam ir ne vairāk kā trīs mēģinājumi.

Programmai:

jāizmanto while cikls;
pēc pareizas paroles jāizvada Piekļuve atļauta;
pēc trim nepareiziem mēģinājumiem jāizvada Piekļuve bloķēta;
pēc kļūdaina mēģinājuma jāparāda, cik mēģinājumu vēl atlicis.
Fails: 03_paroles_parbaude.py
Ieteiktais commit: Pievienota paroles pārbaude ar while

Pārbaudes: pareiza parole pirmajā mēģinājumā, pareiza trešajā, trīs nepareizas paroles un tukša parole.

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

    4. uzdevums — Summa no 1 līdz n
Izveido programmu, kas:

pieprasa veselu pozitīvu skaitli n;
ar for vai while aprēķina visu skaitļu summu no 1 līdz n, ieskaitot n;
parāda gala summu;
paskaidro kļūdu, ja ievadīts 0, negatīvs skaitlis vai nederīga vērtība.
Nelieto gatavu summēšanas funkciju. Mērķis ir pašam uzrakstīt summēšanas algoritmu.

Piemērs: ja n = 5, rezultāts ir 15.
Fails: 04_summa_lidz_n.py
Ieteiktais commit: Pievienots summēšanas algoritms

Pārbaudes: 1, 5, 0, negatīvs skaitlis un tukša ievade.

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

    5.uzdevums — Mazākais un lielākais skaitlis
Izveido programmu, kas pieprasa, cik skaitļus lietotājs ievadīs. Pēc tam programma ievada skaitļus pa vienam un pati atrod mazāko un lielāko vērtību.

Prasības:

izmanto ciklu;
salīdzini katru jauno skaitli ar pašreizējo mazāko un lielāko;
nelieto min() un max();
korekti apstrādā gadījumu, ja skaitļu skaits ir 0 vai negatīvs.
Fails: 05_min_un_max.py
Ieteiktais commit: Pievienots minimuma un maksimuma meklēšanas algoritms

Pārbaudes: viens skaitlis, visi vienādi, tikai negatīvi skaitļi, jaukta secība un skaitļu skaits 0.

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

    6. uzdevums — Lineārā meklēšana
Izmanto doto sarakstu:

skaitli = [4, 7, 2, 9, 7, 1]
Programma pieprasa meklējamo skaitli un ar ciklu pārbauda saraksta elementus pēc kārtas.

Programmai jāizvada:

pirmais indekss, kurā skaitlis atrasts;
paziņojums Nav atrasts, ja skaitļa sarakstā nav.
Papildu līmenis: izvada visus indeksus, kuros vērtība atrasta.

Fails: 06_lineara_meklesana.py
Ieteiktais commit: Pievienots lineārās meklēšanas algoritms

Pārbaudes: pirmais elements, pēdējais elements, vērtība atkārtojas, vērtības nav un nederīga ievade.

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

    izskaidro kas ir šis kods; vecums = int(ievade), if __name__ == "__main__":

Šeit ir vienkāršs un skaidrs skaidrojums abiem šiem bieži izmantotajiem Python koda fragmentiem:

1. vecums = int(ievade)
Šī rinda veic divas svarīgas lietas: pārveido datu tipu un saglabā to mainīgajā.

ievade: Šis parasti ir mainīgais, kurā saglabāts tas, ko lietotājs ievadīja, izmantojot input() funkciju. Svarīgi atcerēties, ka Python visu no tastatūras ievadīto uztver kā tekstu (virkni jeb str), pat ja lietotājs ievadīja ciparus, piemēram, "15".

int(...): Šī iebūvētā funkcija konvertē (pārveido) tekstu par veselu skaitli (angļu valodā integer). Piemēram, tā pārvērš tekstu "15" par īstu skaitli 15.

vecums =: Iegūto skaitli tā saglabā jaunā mainīgajā ar nosaukumu vecums.

Kāpēc tas ir vajadzīgs? Lai ar ievadīto vērtību varētu veikt matemātiskas darbības vai salīdzinājumus (piemēram, pārbaudīt, vai vecums >= 18). Ja mēs mēģinātu salīdzināt tekstu "15" ar skaitli 18, Python izmestu kļūdu.

2. if __name__ == "__main__":
Šis ir ļoti izplatīts Python nosacījums, ko bieži dēvē par "galveno ieejas punktu" (main entry point). Tas pasaka programmai: izpildi šo kodu tikai tad, ja šis fails tiek palaists tieši.

Kā tas strādā? Python, palaižot jebkuru failu, tam automātiski piešķir īpašu sistēmas mainīgo __name__.

Ja tu palaid šo failu tieši (piemēram, terminālī izpildot komandu python 07_skaitlu_analizators.py), Python šī mainīgā vērtību iestata kā "__main__".

Ja šo failu vēlāk importē kā moduli kādā citā Python programmā, __name__ būs faila nosaukums, nevis "__main__".

Kāpēc to izmanto? Tas ļauj tev droši rakstīt kodu, kas automātiski palaižas, kad tu testē savu skriptu, bet neļauj šim kodam nejauši izpildīties, ja kāds cits fails tavu kodu vienkārši importē.

Vai tev ir vēl kādi jautājumi par to, kā strādā konkrētas Python rindas vai konstrukcijas?

izskaidro kas ir if, else un elif

if, elif un else ir nosacījumu operatori (zarošanās konstrukcijas), ko programmēšanā izmanto, lai programma varētu pieņemt lēmumus.

Tie ļauj datoram izvēlēties, kuru koda daļu izpildīt atkarībā no tā, vai kāds nosacījums ir patiess (True) vai nepatiess (False).

1. if (Ja)
Šis ir pats pirmais solis. if pārbauda vienu noteiktu nosacījumu.

Ja nosacījums ir patiess, tiek izpildīts kods, kas atrodas zem if.

Ja nosacījums ir nepatiess, šis kods tiek izlaists.

2. elif (Citā gadījumā, ja... / else if)
Šo izmanto tad, ja tev ir vairāki iespējamie varianti. elif tiek pārbaudīts tikai tad, ja iepriekšējais if (vai cits elif) izrādījās nepatiess. Programmā var būt vairāki elif bloki pēc kārtas.

3. else (Pretējā gadījumā)
Šis ir "drošības tīkls". else nenorāda nekādu konkrētu nosacījumu — tas nostrādā automātiski tad, ja neviens no iepriekšējiem if vai elif nosacījumiem nebija patiess.

Praktisks piemērs
Iedomājies programmu, kas pasaka, kādā vecuma grupā tu esi:

Python
vecums = 15

if vecums < 13:
    print("Tu esi bērns.")
elif vecums < 18:
    print("Tu esi pusaudzis.")
else:
    print("Tu esi pieaugušais.")
Kā tas strādā šajā piemērā:

Programma pārbauda pirmos vārtus: if vecums < 13 (vai 15 ir mazāks par 13?). Tā kā nē, šis tiek izlaists.

Programma pāriet pie nākamajiem vārtiem: elif vecums < 18 (vai 15 ir mazāks par 18?). Tā kā jā, programma izpilda šo rindu un izdrukā: "Tu esi pusaudzis.".

Pārējais kods (tostarp else) tiek pilnībā izlaists, jo viens atbilstošs variants jau tika atrasts.

izskaidro šis, print(f"\nSkaitļa {skaitlis} reizināšanas tabula:")

    for i in range(1, 11):

        rezultats = skaitlis * i

        print(f"{skaitlis} x {i} = {rezultats}")

Šis kods ir vienkārša un eleganta programma, kas izveido un izdrukā konkrēta skaitļa reizināšanas tabulu (no 1 līdz 10).

Sadalīsim šo kodu pa rindiņām, lai saprastu, kas tieši tur notiek:

1. Virsraksta izdruka
Python
print(f"\nSkaitļa {skaitlis} reizināšanas tabula:")
\n: Šis simbols nozīmē "jauna linderinda" (newline). Tas pirms teksta ievieto vienu tukšu rindu, lai skats terminālī būtu pārskatāmāks.

f"..." (f-string): Šī ir ļoti ērta Python funkcija (formatētā virkne). Tā ļauj ievietot mainīgā vērtību tieši tekstā, ierakstot mainīgā nosaukumu iekavās {skaitlis}. Piemēram, ja skaitlis ir 5, rezultāts būs: Skaitļa 5 reizināšanas tabula:.

2. Cikls no 1 līdz 10
Python
for i in range(1, 11):
range(1, 11): Šī funkcija ģenerē skaitļu secību no 1 līdz 10 ieskaitot (atceries, ka Python range beigu robeža ir ekskluzīva, tāpēc jāraksta 11, lai iekļautu arī skaitli 10).

for i in ...: Cikls izies cauri šim blokam 10 reizes. Katrā reizē mainīgais i mainīs savu vērtību: pirmajā reizē i = 1, otrajā i = 2, un tā līdz 10.

3. Reizināšanas aprēķins
Python
rezultats = skaitlis * i
Šeit katrā cikla solī tiek reizināts lietotāja ievadītais pamatskaitlis (skaitlis) ar pašreizējo cikla skaitli (i).

Iegūtais rezultāts tiek saglabāts mainīgajā rezultats.

4. Soli pa solim drukāšana
Python
print(f"{skaitlis} x {i} = {rezultats}")
Arī šeit tiek izmantota f-string virkne, lai skaisti parādītu pilnu reizināšanas izteiksmi.

Piemēram, ja skaitlis ir 5 un i ir 3, uz ekrāna parādīsies: 5 x 3 = 15.

Kopsavilkums
Ja tu palaistu šo kodu un mainīgais skaitlis būtu 4, uz ekrāna izskrietu šāds rezultāts:

Plaintext
Skaitļa 4 reizināšanas tabula:
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
Vai tev ir skaidrs, kā strādā f-string (f"...") vai cikli, vai vēlies vēl kādu piemēru?

try:

        n = int(ievade)

    except ValueError:

        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu.")

        return 

Šis ir ļoti svarīgs un noderīgs koda fragments, ko izmanto kļūdu apstrādei (error handling) Python programmā. Tas neļauj programmai "uzkārties" vai sabojāties, ja lietotājs ievada nepareizus datus.

Sadalīsim šo kodu pa daļām:

1. try: (Mēģināt)
Nozīme: Programma mēģina izpildīt kodu, kas atrodas zem šī bloka. Šajā gadījumā tā mēģina izdarīt šo: n = int(ievade) (pārvērst lietotāja ievadīto tekstu par veselu skaitli).

Ja viss ir kārtībā un lietotājs ievadīja, piemēram, skaitli 5, programma mierīgi turpina darbu tālāk un ignorē except daļu.

2. except ValueError: (Izņēmums / Kļūdas ķeršana)
Nozīme: Šis bloks "noķer" konkrētu kļūdu — ValueError (vērtības kļūda).

Tas nostrādā tad, ja lietotājs ievade vietā ierakstīja kaut ko citu, ko nav iespējams pārvērst par skaitli (piemēram, burtus "abc" vai vārdu "sveiki"). Bez šī koda programma vienkārši apstātos ar sarkanu kļūdas paziņojumu.

3. Kļūdas ziņojums un return
print(...): Parāda lietotājam saprotamu un draudzīgu paziņojumu latviešu valodā, kas paskaidro, kas nogāja greizi.

return: Pārtrauc funkcijas darbību. Tā pasaka programmai: "Tā kā dati nav pareizi, mēs tālāk neturpinām, un šo funkciju beidzam."

Kopsavilkums
Šo konstrukciju izmanto, lai padarītu programmu drošu un lietotājam draudzīgu (user-friendly). Tā vietā, lai programma avarētu, tā laipni pasaka lietotājam: "Klau, tu ievadīji burtus, lūdzu, pamēģini vēlreiz!"

# Aprēķinām summu ar for ciklu

    summa = 0

    for i in range(1, n + 1):

        summa += i



    print(f"Skaitļu summa no 1 līdz {n} ir: {summa}")

Šis kods aprēķina visu veselo skaitļu summu no 1 līdz izvēlētajam skaitlim n, izmantojot for ciklu. Tas ir klasisks veids, kā saskaitīt kopā veselu skaitļu virkni.

Sadalīsim šo kodu pa daļām, lai redzētu, kā tas strādā soli pa solim:

1. Mainīgā sagatavošana
Python
summa = 0
Pirms sākam skaitīt, mēs izveidojam mainīgo summa un piešķiram tam vērtību 0.

Šajā mainīgajā mēs soli pa solim uzkrāsim kopējo summu. Ja mēs to nepiešķirtu, programma nezinātu, no kura punkta sākt skaitīšanu.

2. Cikls caur skaitļiem
Python
for i in range(1, n + 1):
range(1, n + 1): Šeit tiek izveidota virkne no 1 līdz n. Tā kā Python beigu robeža ir ekskluzīva, mēs rakstīsim n + 1, lai iekļautu arī pašu skaitli n.

for i in ...: Cikls izies cauri visiem šiem skaitļiem pa vienam. Pirmajā reizē i = 1, otrajā reizē i = 2, un tā tālāk, līdz tas sasniedz n.

3. Summas uzkrāšana
Python
summa += i
Šis ir saīsinājums pierakstam summa = summa + i.

Katrā cikla solī tas pieskaita pašreizējo skaitli i pie jau esošās summas.

Piemērs, ja n = 3:

Sākumā: summa = 0

solis (i = 1): summa kļūst par 0 + 1 = 1

solis (i = 2): summa kļūst par 1 + 2 = 3

solis (i = 3): summa kļūst par 3 + 3 = 6

4. Rezultāta izdruka
Python
print(f"Skaitļu summa no 1 līdz {n} ir: {summa}")
Kad cikls ir beidzies un visi skaitļi ir saskaitīti, programma izmanto f-string, lai smuki parādītu gala rezultātu uz ekrāna.

Vai zināji?
Matemātikā šo pašu summu (no 1 līdz n) var aprēķināt uzreiz ar vienu vienkāršu formulas rindiņu bez cikla:

summa = n * (n + 1) // 2 (tā sauktā Gausa formula). Taču for cikls ir lielisks veids, kā programmēšanā mācīties saprast, kā dati tiek apstrādāti soli pa solim!

skaitlis = float(ievade_skaitlis), print(f"\nRezultāts:") print(f"Mazākais skaitlis: {mazakais:g}")

    print(f"Lielākais skaitlis: {lielakais:g}")

Šis koda fragments parāda, kā pārvērst ievadīto tekstu par daļskaitli un kā skaisti noformatēt gala rezultātus, izmantojot īpašu formatējuma burtu :g.

Sadalīsim to trīs daļās:

1. skaitlis = float(ievade_skaitlis)
ievade_skaitlis: Tā ir mainīgā virkne, kurā saglabāts tas, ko lietotājs ievadīja (piemēram, teksts "5.5").

float(...): Šī funkcija pārveido tekstu par daļskaitli (angļu valodā floating-point number). Atšķirībā no int() (kas strādā tikai ar veseliem skaitļiem, piemēram, 5), float saprot arī decimāldaļas ar punktu, piemēram, 5.5 vai -3.14.

skaitlis =: Iegūtais skaitlis tiek saglabāts mainīgajā skaitlis, lai ar to varētu veikt matemātiskas darbības.

2. print(f"\nRezultāts:")
Šis ir vienkāršs paziņojums, kas izdrukā uz ekrāna virsrakstu Rezultāts:.

Simbols \n pirms vārda izveido vienu tukšu rindu pirms teksta, lai terminālis izskatītos glītāks un pārskatāmāks.

3. print(f"Mazākais skaitlis: {mazakais:g}") un {lielakais:g}
Šeit galvenā uzmanība jāpievērš simbolam :g iekavās aiz mainīgā nosaukuma:

Kas ir :g? Python f-string virknēs :g (no angļu valodas general format) ir formatējuma rīks, kas palīdz skaitļiem izskatīties smukāk un dabiskāk:

Tas automātiski notīra liekās nulles aiz komata. Piemēram, ja skaitlis ir 5.0, tas ekrānā parādīs vienkārši 5, bet, ja tas ir 5.5, tas parādīs 5.5.

Tas arī pasargā garus decimāldaļskaitļus no pārliekas garuma (ja cipars aiz komata ir ļoti garš).

Kopumā šīs rindiņas parāda lietotājam agrāk aprēķināto minimālo un maksimālo skaitli tīrā un viegli lasāmā veidā!

pirmais_indekss = -1

    visi_indeksi = [], # Ar ciklu un enumerate pārbaudām saraksta elementus pēc kārtas

    for indekss, vertiba in enumerate(skaitli):

        if vertiba == meklejamo:

            if pirmais_indekss == -1:

                pirmais_indekss = indekss

            visi_indeksi.append(indekss), if pirmais_indekss != -1: 

Šis koda fragments ir ļoti noderīgs algoritms, lai atrastu konkrētas vērtības atrašanās vietas (indeksus) sarakstā. Tas atrod gan pašu pirmo reizi, kur šis skaitlis parādās, gan visas pārējās reizes, ja skaitlis sarakstā atkārtojas vairākas reizes.

Sadalīsim šo kodu pa daļām:

1. Mainīgo sagatavošana
Python
pirmais_indekss = -1
visi_indeksi = []
pirmais_indekss = -1: Mēs izveidojam mainīgo un iestatām to uz -1. Programmēšanā -1 bieži izmanto kā signālu jeb karodziņu, kas nozīmē: "Mēs vēl neesam atraduši šo skaitli." (Tā kā saraksta indeksi vienmēr sākas no 0, -1 nevar būt reāls indekss, tāpēc tas ir drošs rādītājs).

visi_indeksi = []: Mēs izveidojam tukšu sarakstu, kurā vēlāk uzkrāsim visus indeksus, kur atradīsim meklēto skaitli.

2. Cikls un enumerate funkcija
Python
for indekss, vertiba in enumerate(skaitli):
enumerate(skaitli): Šī ir lieliska Python funkcija. Kad tu ej cauri sarakstam skaitli, enumerate tev uzreiz pasaka divas lietas vienlaikus: pozīciju (indeksu) un pašu vērtību tajā pozīcijā.

indekss saglabā skaitļa vietu sarakstā (0, 1, 2 utt.), bet vertiba saglabā tur esošo skaitli.

3. Pārbaude un meklēšana
Python
    if vertiba == meklejamo:
        if pirmais_indekss == -1:
            pirmais_indekss = indekss
        visi_indeksi.append(indekss)
if vertiba == meklejamo:: Pārbauda, vai pašreizējais elements sakrīt ar to skaitli, ko mēs meklējam (meklejamo).

if pirmais_indekss == -1:: Ja skaitlis sakrīt un mēs vēl neesam atraduši pirmo indeksu (tas joprojām ir -1), mēs saglabājam šo indeksu kā pirmais_indekss. Tā kā tas notiek pašā pirmajā sakritības reizē, tas vairs nemainīsies turpmākajos soļos.

visi_indeksi.append(indekss): Neatkarīgi no tā, vai tā ir pirmā vai piektā reize, kad skaitlis atrasts, mēs pievienojam šo indeksu mūsu sarakstam visi_indeksi, izmantojot .append() metodi.

4. Pēdējā rinda: if pirmais_indekss != -1:
Tā rinda, kas tev ir pierakstīta beigās, parasti tiek izmantota uzreiz pēc cikla, lai pārbaudītu rezultātu:

!= -1 nozīmē "ja tas nav vienāds ar -1" (tas ir – ja mēs vispār atradām šo skaitli sarakstā).

Pēc šīs pārbaudes programma parasti izdrukā lietotājam: "Atrasts pirmajā pozīcijā ar indeksu X" vai izada visu sarakstu ar indeksiem. Ja skaitlis vispār netika atrasts, pirmais_indekss paliek -1, un programma var paziņot, ka šāda skaitļa sarakstā nav.

skaitlis = float(input(f"Ievadiet {i+1}. skaitli: "))

                skaitli.append(skaitlis)

                break

            except ValueError:

                print("Nederīga vērtība. Lūdzu, ievadiet skaitli atkārtoti!"), # Pāra un nepāra skaitļi parasti attiecas uz veseliem skaitļiem

    para = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 == 0)

    nepara = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 != 0),

Šis koda fragments apvieno divas svarīgas programmas daļas: drošu skaitļa saņemšanu un pievienošanu sarakstam (iekš while cikla) un pāra/nepāra skaitļu skaitīšanu (izmantojot generatoru izteiksmes).

Sadalīsim to pa daļām:

1. Datu ievade un saglabāšana sarakstā
Python
skaitlis = float(input(f"Ievadiet {i+1}. skaitli: "))
skaitli.append(skaitlis)
break
float(input(...)): Programma prasa lietotājam ievadīt nākamo skaitli (piemēram, pirmajā reizē i=0, tāpēc rādīsies 1. skaitli) un uzreiz to pārvērš par daļskaitli (float).

skaitli.append(skaitlis): Šī metode (.append) pievieno iegūto skaitli iepriekš izveidotajam sarakstam ar nosaukumu skaitli.

break: Pārtrauc iekšējo bezgalīgo ciklu (while True), jo ievade bija veiksmīga un pareiza, un tagad var pāriet pie nākamā skaitļa vai tālākiem aprēķiniem.

2. Kļūdu ķeršana (ja ievadīts teksts)
Python
except ValueError:
    print("Nederīga vērtība. Lūdzu, ievadiet skaitli atkārtoti!")
Ja lietotājs ievadīja burtus vai citus simbolus, kurus nevar pārvērst par skaitli, izlec ValueError kļūda, programma izdrukā brīdinājumu un liek lietotājam mēģināt vēlreiz (jo cikls turpinās).

3. Pāra un nepāra skaitļu noteikšana
Python
para = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 == 0)
nepara = sum(1 for x in skaitli if x.is_integer() and int(x) % 2 != 0)
Tā kā sarakstā var būt arī daļskaitļi (piemēram, 5.5), šis kods gudri atlasa tikai tos skaitļus, kas patiesībā ir veseli, un saskaita tos:

x.is_integer(): Pārbauda, vai konkrētais skaitlis sarakstā ir vesels skaitlis (piemēram, 5.0 ir vesels, bet 5.5 nav).

int(x) % 2 == 0: Pārvērš skaitli par veselu skaitli un ar dalīšanas atlikuma zīmi (%) pārbauda, vai tas dalās ar 2 bez atlikuma (pāra skaitlis). Ja atlikums ir 0, tad tas ir pāra skaitlis.

int(x) % 2 != 0: Pārbauda, vai dalīšanas atlikums, dalot ar 2, nav nulle (tātad atlikumā paliek 1). Tas nozīmē, ka tas ir nepāra skaitlis.

sum(1 for x in skaitli ...): Šis saskaita visus elementus sarakstā, kuri atbilst šim nosacījumam, un atgriež kopējo skaitu mainīgajos para un nepara.

## Šodienas darba secība

1. stunda — repozitorija izveide un darba plūsmas demonstrācija.  
2. stunda — README un failu struktūras sagatavošana.  
3.–5. stunda — programmēšanas uzdevumi un regulāri `commit`.  
6. stunda — Programmēšanas ĢEDD iesniegums.  
7. stunda — algoritmiskie programmēšanas uzdevumi Python valodā.  
8. stunda — izvēlētās programmas pabeigšana, testi, izsekošana un Algoritmu pamatu ĢEDD iesniegums.

## Repozitorija struktūra

```text
README.md
TESTI.md
01_vecuma_grupa.py
02_reizinasanas_tabula.py
03_paroles_parbaude.py
04_summa_lidz_n.py
05_min_un_max.py
06_lineara_meklesana.py
07_skaitlu_analizators.py
08_mini_bankomats.py
09_burbulkartosana.py
```

## Darba noteikumi

- Veic uzdevumus pēc kārtas, kamēr tie atbilst tavam līmenim.
- Katru uzdevumu saglabā atsevišķā `.py` failā.
- Pēc katra pabeigta darba posma izveido atsevišķu `commit` un veic `push`.
- Tev nav jāpabeidz visi deviņi uzdevumi. Pirmie trīs pārbauda Python pamatprasmes. 4.–9. uzdevums palīdz noteikt, cik patstāvīgi proti veidot algoritmu.
- Algoritmu ĢEDD jābūt redzamam gan Python kodā, gan failā `TESTI.md`.
- Ja tests atklāj kļūdu, pieraksti faktisko rezultātu un izlabo programmu. Atrasta un izskaidrota kļūda nav neveiksme.

## Git darba plūsma

Pēc katra pabeigta posma:

```bash
git status
git add .
git commit -m "Īss un konkrēts paveiktā apraksts"
git push
```

## 1. uzdevums — Vecuma grupa

Izveido programmu, kas:

1. pieprasa lietotāja vecumu;
2. ar `if`, `elif` un `else` nosaka grupu;
3. izvada vienu no rezultātiem: `bērns`, `pusaudzis`, `pieaugušais` vai `seniors`.

Izvēlies un kodā skaidri norādi vecuma robežas.

**Fails:** `01_vecuma_grupa.py`  
**Ieteiktais commit:** `Pievienots vecuma grupas uzdevums ar if`

**Pārbaudes:** vecumi tieši pirms un pēc katras robežas, `0`, negatīvs skaitlis un tukša ievade.

## 2. uzdevums — Reizināšanas tabula

Izveido programmu, kas pieprasa vienu veselu skaitli un ar `for` ciklu izvada tā reizināšanas tabulu no 1 līdz 10.

Piemērs, ja ievadīts `4`:

```text
4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
```

**Fails:** `02_reizinasanas_tabula.py`  
**Ieteiktais commit:** `Pievienota reizināšanas tabula ar for`

**Pārbaudes:** pozitīvs skaitlis, `0`, `1`, negatīvs skaitlis un teksts skaitļa vietā.

## 3. uzdevums — Paroles pārbaude

Izveido programmu, kurā pareizā parole ir saglabāta mainīgajā. Lietotājam ir ne vairāk kā trīs mēģinājumi.

Programmai:

- jāizmanto `while` cikls;
- pēc pareizas paroles jāizvada `Piekļuve atļauta`;
- pēc trim nepareiziem mēģinājumiem jāizvada `Piekļuve bloķēta`;
- pēc kļūdaina mēģinājuma jāparāda, cik mēģinājumu vēl atlicis.

**Fails:** `03_paroles_parbaude.py`  
**Ieteiktais commit:** `Pievienota paroles pārbaude ar while`

**Pārbaudes:** pareiza parole pirmajā mēģinājumā, pareiza trešajā, trīs nepareizas paroles un tukša parole.

# Algoritmiskie programmēšanas uzdevumi

Šajos uzdevumos algoritms jāīsteno Python kodā. Sāc ar 4. uzdevumu un turpini, kamēr pietiek laika.

## 4. uzdevums — Summa no 1 līdz n

Izveido programmu, kas:

1. pieprasa veselu pozitīvu skaitli `n`;
2. ar `for` vai `while` aprēķina visu skaitļu summu no `1` līdz `n`, ieskaitot `n`;
3. parāda gala summu;
4. paskaidro kļūdu, ja ievadīts `0`, negatīvs skaitlis vai nederīga vērtība.

Nelieto gatavu summēšanas funkciju. Mērķis ir pašam uzrakstīt summēšanas algoritmu.

**Piemērs:** ja `n = 5`, rezultāts ir `15`.  
**Fails:** `04_summa_lidz_n.py`  
**Ieteiktais commit:** `Pievienots summēšanas algoritms`

**Pārbaudes:** `1`, `5`, `0`, negatīvs skaitlis un tukša ievade.

## 5. uzdevums — Mazākais un lielākais skaitlis

Izveido programmu, kas pieprasa, cik skaitļus lietotājs ievadīs. Pēc tam programma ievada skaitļus pa vienam un pati atrod mazāko un lielāko vērtību.

Prasības:

- izmanto ciklu;
- salīdzini katru jauno skaitli ar pašreizējo mazāko un lielāko;
- nelieto `min()` un `max()`;
- korekti apstrādā gadījumu, ja skaitļu skaits ir `0` vai negatīvs.

**Fails:** `05_min_un_max.py`  
**Ieteiktais commit:** `Pievienots minimuma un maksimuma meklēšanas algoritms`

**Pārbaudes:** viens skaitlis, visi vienādi, tikai negatīvi skaitļi, jaukta secība un skaitļu skaits `0`.

## 6. uzdevums — Lineārā meklēšana

Izmanto doto sarakstu:

```python
skaitli = [4, 7, 2, 9, 7, 1]
```

Programma pieprasa meklējamo skaitli un ar ciklu pārbauda saraksta elementus pēc kārtas.

Programmai jāizvada:

- pirmais indekss, kurā skaitlis atrasts;
- paziņojums `Nav atrasts`, ja skaitļa sarakstā nav.

Papildu līmenis: izvada visus indeksus, kuros vērtība atrasta.

**Fails:** `06_lineara_meklesana.py`  
**Ieteiktais commit:** `Pievienots lineārās meklēšanas algoritms`

**Pārbaudes:** pirmais elements, pēdējais elements, vērtība atkārtojas, vērtības nav un nederīga ievade.

## 7. uzdevums — Skaitļu analizators

Izveido programmu, kas sākumā pajautā, cik skaitļus lietotājs ievadīs. Pēc tam programma ar ciklu pieprasa katru skaitli un beigās parāda:

- ievadīto skaitļu summu;
- pozitīvo, negatīvo un nulles vērtību skaitu;
- pāra un nepāra skaitļu skaitu;
- vidējo aritmētisko.

**Fails:** `07_skaitlu_analizators.py`  
**Ieteiktais commit:** `Pievienots skaitļu analizators`

**Pārbaudes:** viens skaitlis, tikai nulles, pozitīvi un negatīvi skaitļi, kā arī skaitļu skaits `0`.

## 8. uzdevums — Mini bankomāts

Izveido programmu ar sākuma atlikumu `100`. Programma atkārtoti rāda izvēlni:

```text
1 — apskatīt atlikumu
2 — iemaksāt naudu
3 — izņemt naudu
4 — beigt darbu
```

Prasības:

- izvēlne atkārtojas ar `while`, līdz lietotājs izvēlas 4;
- darbības izvēlas ar `if` un `elif`;
- nedrīkst izņemt vairāk naudas, nekā ir kontā;
- nedrīkst iemaksāt vai izņemt nulli vai negatīvu summu;
- pēc katras darbības parādi saprotamu paziņojumu.

**Fails:** `08_mini_bankomats.py`  
**Ieteiktais commit:** `Pievienots mini bankomāts ar izvēlni`

**Pārbaudes:** izņemt visu atlikumu, izņemt par vienu vairāk, ievadīt `0`, negatīvu summu un neesošu izvēlnes numuru.

## 9. uzdevums — Burbuļkārtošana

Šis ir padziļinātais uzdevums. Sakārto sarakstu augošā secībā, salīdzinot blakus esošus elementus un samainot tos vietām.

```python
skaitli = [5, 2, 8, 1, 4]
```

Prasības:

- izmanto divus ciklus;
- salīdzini blakus esošos elementus;
- izveido maiņu ar pagaidu mainīgo vai Python vērtību maiņu;
- pēc katra ārējā cikla izvada saraksta pašreizējo stāvokli;
- nelieto `sort()` vai `sorted()`.

**Fails:** `09_burbulkartosana.py`  
**Ieteiktais commit:** `Pievienots burbuļkārtošanas algoritms`

**Pārbaudes:** jau sakārtots saraksts, dilstoša secība, vienādas vērtības, viens elements un tukšs saraksts.

# Algoritmu pamatu ĢEDD

Izvēlies vienu no 4.–9. uzdevuma. ĢEDD pierādījumiem jābūt divos failos:

1. darbojošs vai pamatoti iesākts `.py` fails ar algoritmu;
2. `TESTI.md` ar izsekošanu un testiem.

## 1. Programmas apraksts

Norādi faila nosaukumu, ievadi, sagaidāmo rezultātu un īsi paskaidro algoritma darbības.

## 2. Izpildes izsekošana

Izvēlies vienu konkrētu ievadi un pieraksti mainīgo vērtības pa soļiem.

```markdown
| Solis | Nosacījums | Mainīgie pirms | Veiktā darbība | Mainīgie pēc | Izvade |
|------:|------------|-----------------|----------------|----------------|--------|
| 0     | —          |                 | Sākums         |                |        |
| 1     |            |                 |                |                |        |
| 2     |            |                 |                |                |        |
```

## 3. Testa piemēri

Izveido vismaz četrus atšķirīgus testus.

```markdown
| Testa veids | Ievade | Sagaidāmais rezultāts | Faktiskais rezultāts | Tests izturēts? |
|-------------|--------|-----------------------|---------------------|-----------------|
| Tipisks     |        |                       |                     |                 |
| Robežgadījums |      |                       |                     |                 |
| Tukša vai nederīga ievade | |                 |                     |                 |
| Papildu tests |      |                       |                     |                 |
```

## 4. Kļūda, pretpiemērs vai uzlabojums

Ja tests atklāj kļūdu, pieraksti ievadi, sagaidāmo rezultātu, faktisko rezultātu, kļūdas cēloni un labojumu.

Ja programma visus testus iztur, izvēlies agrāku kļūdainu `commit` vai paskaidro, kura ievade radītu kļūdu bez vienas no tavām pārbaudēm.

**Ieteiktais commit:** `Pievienots algoritms un tā testi`

## Programmēšanas ĢEDD iesniegšanas pārbaude

- [ ] repozitorijs atveras Gitea;
- [ ] repozitorijā ir README un sāktie `.py` faili;
- [ ] programmās redzams `if`, `for` un `while` lietojums;
- [ ] programmas ir palaistas un pārbaudītas;
- [ ] versiju vēsturē ir vismaz trīs jēgpilni `commit`;
- [ ] jaunākā versija nosūtīta ar `push`;
- [ ] repozitorija saite iesniegta skolotājam.

## Algoritmu pamatu ĢEDD iesniegšanas pārbaude

- [ ] repozitorijā ir vismaz viens 4.–9. uzdevuma `.py` fails;
- [ ] algoritms darbojas vai ir skaidri norādīta atrastā kļūda;
- [ ] kodā izmantots cikls, nosacījums un mainīgo vērtību atjaunināšana;
- [ ] failā `TESTI.md` redzama izpildes izsekošana;
- [ ] izveidoti vismaz četri atšķirīgi testi;
- [ ] ir tipiska, robežas un tukša vai nederīga ievade;
- [ ] izmaiņas saglabātas ar `commit` un `push`;
- [ ] aizpildīts pašvērtējums.
