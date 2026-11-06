# 5. Łowienie ID własnego licznika

Telegram radiowy ma jawny nagłówek (producent, ID, wersja, typ) nawet gdy treść jest szyfrowana, więc ID da się odczytać z eteru.

1. Wgraj firmware z przykładowym `meter_id`. Wpis `on_frame` w configu loguje każdą ramkę z poprawną sumą kontrolną, także cudzą.
2. Zapisz logi na 15–20 minut (liczniki nadają co kilkanaście minut): `esphome logs firmware/wodomierze.yaml > ramki.log`, potem przerwij Ctrl+C.
3. Uruchom: `python3 -I tools/wmbus_ids.py ramki.log`.
4. Tabela pokazuje producenta, ID, wersję, typ i siłę sygnału. Szukaj producenta `APA` (Apator) i typu „woda". Najsilniejszy sygnał jest najczęściej Twoim licznikiem (założenie, nie gwarancja), a cudze liczniki z okolicy też się pojawią.
5. Wpisz ID jako `0x` + 8 cyfr (np. `0x12345678`) do `meter_id`.

Jeśli widzisz kilka liczników Apator, a nie wiesz który Twój: zakręć krótko wodę i sprawdź, czyj licznik przestaje rosnąć, albo porównaj z ID na nakładce (naklejka). Numer na korpusie licznika to **nie** ID radiowe.

Dalej: [6. Problemy](06-problemy.md)
