# 3. Konfiguracja

Ustawienia są na górze pliku `firmware/wodomierze.yaml`, w bloku `substitutions`.

| Pole | Znaczenie | Domyślnie |
|---|---|---|
| `name` | nazwa urządzenia w sieci i w HA | `wodomierze` |
| `friendly_name` | nazwa wyświetlana | `Wodomierze` |
| `meter_id` | ID radiowe nakładki, 8 cyfr szesnastkowych z `0x` na początku | `0x12345678` (**przykład, zmień**) |
| `meter_offset` | poprawka stanu w m³ | `0.0` |
| `garden_id`, `garden_offset` | to samo dla drugiego licznika (tylko plik na dwa liczniki) | przykład |

## ID licznika

ID to numer **nakładki radiowej**, a nie numer wybity na korpusie licznika. Jak go znaleźć: [rozdział 5](05-lowienie-id.md).

## Offset: dlaczego i jak go wyliczyć

Nakładka ma własny punkt zerowy, ustawiany przy montażu, więc jej liczba nie musi zgadzać się z tarczą. Przyrosty są poprawne, rozjechany jest tylko punkt startowy.

1. Zostaw `meter_offset: "0.0"` i wgraj firmware. Encja „Wodomierz - stan" pokaże wartość z radia.
2. W jednej chwili zapisz wartość z encji (z dokładnością do litrów) i odczytaj tarczę licznika.
3. Offset = **tarcza − radio**. Przykład: tarcza 14,177, radio 37,626 → offset `-23.449`.
4. Wpisz offset, wgraj firmware po WiFi.

**Czytanie tarczy:** czerwone wskazówki to ułamki m³. Czytaj łańcuchem od najmniejszej wskazówki w górę: każda wskazówka musi pasować do ułamka tej mniejszej od niej. Czytanie „na oko" potrafi dać błąd o całe 0,9 m³ przy wskazówce stojącej tuż przy zerze.

**Uwaga:** po zmianie offsetu na działającym systemie statystyki w HA zrobią skok. Można go skorygować usługą `recorder/adjust_sum_statistics` (przez WebSocket API) albo zaakceptować i ustawić offset zaraz na początku, zanim zbierze się historia.

**Po wymianie nakładki lub korpusu licznika** punkt zerowy się zmienia, więc offset trzeba wyliczyć od nowa.

## Drugi licznik i „dom = główny − podlicznik"

Plik `wodomierze-dwa-liczniki.yaml` ma encję **Wodomierz dom - stan** = główny − podlicznik. Zatrzask w jej kodzie jest potrzebny, bo liczniki nadają niezależnie, co kilkanaście minut. Bez niego chwilowy spadek różnicy HA uznałby za wyzerowanie licznika i doliczył fałszywy skok.

## Czego nie robić

- Nie wystawiaj strony WWW płytki do internetu.
- Nie wyłączaj szyfrowania API ani `web_server: auth`.
- Nie wpisuj haseł do plików poza `secrets.yaml`.

Dalej: [4. Panel Energia](04-panel-energia.md)
