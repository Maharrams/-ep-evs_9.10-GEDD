## 1. Programmas apraksts

1.Faila nosaukums: 04_summa_lidz_n.py
2.Ievade: ievada veselu pozitīvu skaitli n (teksta formātā, kas tiek nolasīts ar input() un konvertēts uz veselu skaitli).
3.Sagaidāmais rezultāts: Programma izdrukā visu veselo skaitļu summu no 1 līdz n ieskaitot.
4.Algoritma darbība: Programma vispirms veic drošības pārbaudes: pārbauda, vai ievade nav tukša (if not ievade.strip()), vai ievadītais teksts ir pārvēršams veselā skaitlī (try-except ValueError) un vai skaitlis ir lielāks par 0 (if n <= 0). Ja viss ir pareizs, ar for cikla un range(1, n + 1) palīdzību tiek veikta pakāpeniska skaitļu summēšana mainīgajā summa (summa += i), un galā tiek izvadīts rezultāts.

## 2. Izpildes izsekošana

| Solis | Nosacījums | Mainīgie pirms | Veiktā darbība | Mainīgie pēc | Izvade |
|------:|------------|-----------------|----------------|----------------|--------|
| 0     | —          | `ievade = "3"`  | Validācija un `n` konversija | `n = 3`, `summa = 0` | — |
| 1     | `i = 1`    | `n = 3`, `summa = 0`, `i = 1` | `summa += 1` | `summa = 1` | — |
| 2     | `i = 2`    | `n = 3`, `summa = 1`, `i = 2` | `summa += 2` | `summa = 3` | — |
| 3     | `i = 3`    | `n = 3`, `summa = 3`, `i = 3` | `summa += 3` | `summa = 6` | — |
| 4     | Cikls beidzas | `n = 3`, `summa = 6` | `print(...)` | `summa = 6` | Skaitļu summa no 1 līdz 3 ir: 6 |

## 3. Testa piemēri

| Testa veids | Ievade | Sagaidāmais rezultāts | Faktiskais rezultāts | Tests izturēts? |
|-------------|--------|-----------------------|---------------------|-----------------|
| Tipisks | `5` | `Skaitļu summa no 1 līdz 5 ir: 15` | `Skaitļu summa no 1 līdz 5 ir: 15` | Jā |
| Robežgadījums | `1` | `Skaitļu summa no 1 līdz 1 ir: 1` | `Skaitļu summa no 1 līdz 1 ir: 1` | Jā |
| Tukša vai nederīga ievade | `abc` | `Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu.` | `Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu.` | Jā |
| Papildu tests | `0` | `Kļūda: Skaitlim ir jābūt pozitīvam (lielākam par 0).` | `Kļūda: Skaitlim ir jābūt pozitīvam (lielākam par 0).` | Jā |

## 4. Kļūda, pretpiemērs vai uzlabojums

Paskaidrojums: Ja programmā nebūtu iekļauta pārbaude if n <= 0, tad, ievadot skaitli 0 vai negatīvu skaitli, range(1, n + 1) funkcija sāktos no 1 un beigtos pirms 1 vai uzreiz apstātos, atgriežot summu 0, kas maldinātu lietotāju. Savukārt bez try-except bloka programmas darbība negaidīti apstātos ar sistēmas kļūdu (ValueError), ja lietotājs ievadītu burtus. Šīs pārbaudes padara kodu drošu.