# 7. Jak to działa

## Budowa

- `wmbus_radio` obsługuje CC1101 i odbiera ramki na 868,95 MHz.
- `wmbus_common` z jednym sterownikiem `apator162`. Wszystkie sterowniki nie mieszczą się sensownie we flashu, więc ładujemy tylko potrzebny.
- `wmbus_meter` dekoduje telegramy konkretnego ID i podaje `total_m3`, `rssi_dbm` i `timestamp`.
- Poprawka offsetu to filtr `offset` na encji.

Komponenty pochodzą z [SzczepanLeon/esphome-components](https://github.com/SzczepanLeon/esphome-components) (v5, esp-idf, tylko ESP32). Konfiguracja wskazuje gałąź `main`, więc po zmianach w tamtym repo build może zachować się inaczej niż u autora. Wersja sprawdzona: kompilacja 2026-11-06.

## Decyzje

| Decyzja | Powód |
|---|---|
| Płytka ESP32 po WiFi zamiast stick USB (np. nanoCUL) | Żadnego przekazywania portu USB do maszyny z HA, płytka stoi tam, gdzie jest zasięg. |
| `logger: level: INFO` | CC1101 sypie szum 1–2 pakiety na sekundę. Na DEBUG log zalewa połączenie z HA. |
| `api: max_connections: 10` | Domyślne 5 gniazd potrafi się wyczerpać i encje stają. |
| `web_server: ota: false` + login | Domyślny formularz wgrania firmware na stronie płytki nie sprawdza hasła OTA. |
| Zatrzask w „dom = główny − podlicznik" | Patrz [rozdział 3](03-konfiguracja.md). |
| Offset w configu, nie w HA | Wartość w HA zgadza się z tarczą od razu, bez dodatkowych przeliczeń. |

## Znane pułapki

- Klucz szyfrowania z samych zer to wartość nakładek Apator AT-WMBUS-16-2 u autora, nie sekret. Nakładka z innym kluczem wymaga wpisania go w `key`.
- Zmiana offsetu daje skok w statystykach HA ([rozdział 3](03-konfiguracja.md)).
- Podgląd ramek (`on_frame`) loguje także cudze liczniki w okolicy. To tylko lokalny log w płytce.
