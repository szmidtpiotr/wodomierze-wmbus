# 1. Części

## Lista

| Część | Uwagi |
|---|---|
| **Seeed XIAO ESP32-S3** | Musi być ESP32 (komponent radiowy nie działa na ESP8266, D1 mini ani NodeMCU). |
| **Moduł CC1101 na 868 MHz** | **Uważaj na wersję:** w sklepach są też moduły 433 MHz, które nie odbiorą licznika. Sprawdź opis „868 MHz" lub „868/915 MHz". |
| **Antena 868 MHz** | Do CC1101: spirala lub kawałek drutu ok. 8,6 cm (ćwierć fali). Bez anteny zasięg jest bardzo słaby. |
| **Antenka WiFi u.FL** | **XIAO ESP32-S3 nie ma anteny na płytce.** Bez antenki u.FL płytka nie widzi sieci WiFi, nawet jeśli router stoi kilka metrów dalej. |
| Przewody 7 szt., kabel USB-C, zasilacz USB | Zasilanie wystarczy z dowolnej ładowarki USB. |

Cen nie podaję, bo nie mam ich sprawdzonych.

## Licznik wody

Odbiornik słyszy tylko liczniki, które nadają radiowo. Autor używa nakładek **Apator AT-WMBUS-16-2** na licznikach Apator i Maddalena (sterownik `apator162`, tryb T1, bez szyfrowania). Sprawdzone tylko na tych.

Jeśli Twój licznik nie ma nakładki, **same kupno odbiornika nic nie da**. Przed zakupem nakładki upewnij się u producenta lub sprzedawcy, że pasuje do Twojego modelu, a u wodociągów, czy wolno ją założyć (licznik bywa plombowany).

## Gdzie postawić odbiornik

Zasięg nie zależy prosto od odległości, tylko od ścian i rur po drodze. U autora licznik bliżej, ale za grubą ścianą, nie dochodził wcale, a dalszy dochodził dobrze. Zacznij od ustawienia płytki możliwie blisko licznika i sprawdź RSSI ([rozdział 6](06-problemy.md)).

Dalej: [2. Instalacja](02-instalacja.md)
