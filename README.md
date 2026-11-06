# Wodomierze wM-Bus w Home Assistancie

Odbiornik radiowy na płytce ESP32, który odczytuje stan wodomierza przez radio (wM-Bus, 868 MHz) i wysyła go do Home Assistanta. Nie musisz nic wpinać w rurę ani zdejmować plomb z licznika, jeśli licznik ma już nakładkę radiową Apator AT-WMBUS-16-2.

**Po co:** zużycie wody widać w Home Assistancie na bieżąco, w panelu Energia, bez chodzenia do piwnicy i przepisywania liczb z tarczy.

![Jak to działa](docs/img/jak-to-dziala.png)

## Co potrafi

- Odczyt stanu licznika w m³ z dokładnością do litra i siły sygnału radiowego (RSSI).
- Poprawka stanu (offset), żeby wartość w HA zgadzała się z tarczą licznika.
- Dwa liczniki naraz (główny + podlicznik, np. ogród) i wyliczenie zużycia samego budynku.
- Podgląd cudzych ramek radiowych, żeby znaleźć numer (ID) własnego licznika.
- Szyfrowane API, strona WWW plytki za loginem, awaryjna sieć WiFi.

## Rozdziały

| Plik | Treść |
|---|---|
| [01-czesci.md](docs/01-czesci.md) | co kupić i na co uważać |
| [02-instalacja.md](docs/02-instalacja.md) | lutowanie, wgranie firmware, dodanie do HA |
| [03-konfiguracja.md](docs/03-konfiguracja.md) | ID licznika, offset, drugi licznik |
| [04-panel-energia.md](docs/04-panel-energia.md) | woda w panelu Energia i pułapka z podwójnym liczeniem |
| [05-lowienie-id.md](docs/05-lowienie-id.md) | jak znaleźć ID własnego licznika |
| [06-problemy.md](docs/06-problemy.md) | objaw → przyczyna → rozwiązanie |
| [07-jak-to-dziala.md](docs/07-jak-to-dziala.md) | budowa i decyzje projektowe |

## Najkrótsza droga

Orientacyjnie 1–2 godziny, jeśli masz już części i ESPHome: [części](docs/01-czesci.md) → [instalacja](docs/02-instalacja.md) → [ID i offset](docs/03-konfiguracja.md).

## Struktura repo

```
firmware/   wodomierze.yaml (1 licznik), wodomierze-dwa-liczniki.yaml, secrets.yaml.example
docs/       instrukcje, docs/wiring.yml (źródło schematu), docs/img/ (obrazki)
tools/      wmbus_ids.py (zestawienie ID z logu)
```

## Stan projektu

- **Sprawdzone:** firmware z `wodomierze-dwa-liczniki.yaml` kompiluje się (ESPHome 2026.10.2). Plik `wodomierze.yaml` przeszedł walidację konfiguracji, ale nie był kompilowany. Wersja produkcyjna autora działa od września 2026 na dwóch licznikach Apator.
- **Nie sprawdzone:** zgodność z innymi licznikami niż Apator (inne sterowniki wymagają zmiany `type` i `drivers`) oraz z licznikami z szyfrowaniem.
- Licencja: MIT. Firmware korzysta z cudzego komponentu [SzczepanLeon/esphome-components](https://github.com/SzczepanLeon/esphome-components), który ma własną licencję.
