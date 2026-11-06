# 6. Problemy

## Wgrywanie

| Objaw | Przyczyna i rozwiązanie |
|---|---|
| Błąd o braku `secrets.yaml` | Skopiuj `secrets.yaml.example` jako `secrets.yaml` i uzupełnij. |
| Błąd otwarcia portu na końcu wgrania, a wcześniej „Hash of data verified" | XIAO ponownie się zgłasza po USB. Wgranie się udało. |

## Sieć

| Objaw | Przyczyna i rozwiązanie |
|---|---|
| `No networks found` | Brak antenki u.FL (XIAO nie ma anteny na płytce). |
| Encje `unavailable`, a płytka odpowiada na ping | Wyczerpany limit połączeń API. Ustawiono `max_connections: 10`. Jeśli wróci: restart HA Core. |
| W logu `BAD_INDICATOR errno=11` | Ktoś łączy się jawnym tekstem z zaszyfrowanym API, np. dodatek ESPHome z zapamiętaną starą konfiguracją. Zrestartuj dodatek ESPHome. |

## Radio

| Objaw | Przyczyna i rozwiązanie |
|---|---|
| Brak odczytów, w logu tylko szum | Zła wersja modułu (433 MHz zamiast 868), brak anteny albo za duża odległość. Postaw płytkę bliżej. |
| `CC1101: RX timeout after 0 bytes (need 3)` | To nie awaria, tylko szum odebrany jako nośna. Ignoruj. |
| Wartość się nie zgadza z tarczą | Brak lub zły offset, [rozdział 3](03-konfiguracja.md). |
| Odczyt zniknął po wymianie nakładki lub licznika | Inne ID i inny punkt zerowy. Złów ID od nowa i wylicz offset. |

## Jak sprawdzić zasięg

Encja **Wodomierz - RSSI**. Im bliżej zera, tym lepiej (−57 jest lepsze niż −90). U autora dwa liczniki z jednego miejsca miały −57 i −58 dBm i odczyty szły stabilnie. Granicy, poniżej której odbiór się urywa, nie zmierzyłem.

Dalej: [7. Jak to działa](07-jak-to-dziala.md)
