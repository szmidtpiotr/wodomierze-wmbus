# 4. Panel Energia

Home Assistant: **Ustawienia → Pulpity → Energia → Zużycie wody**.

## Jeden licznik

Dodaj encję **Wodomierz - stan** jako źródło wody. Gotowe.

## Dwa liczniki (główny i podlicznik)

**Pułapka:** HA **sumuje** wszystkie pozycje z „Zużycie wody". Jeśli wpiszesz tam oba liczniki, woda z podlicznika (np. z ogrodu) policzy się dwa razy, bo przepływa też przez główny.

Poprawnie:

1. Jako źródło wody wpisz tylko licznik **główny** (całość).
2. Podlicznik dodaj w sekcji **Pojedyncze urządzenia wodne**. Tam HA odejmuje go od całości zamiast dodawać.

Encja „Wodomierz dom - stan" nie jest do panelu Energia potrzebna, bo HA sam wylicza resztę. Zostaje jako zwykły odczyt.

Sprawdzone u autora we wrześniu 2026. Nazwy sekcji w interfejsie mogą się różnić między wersjami HA.

Dalej: [5. Łowienie ID](05-lowienie-id.md)
