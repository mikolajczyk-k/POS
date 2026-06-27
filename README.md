Projekt zaliczeniowy z przedmiotu Projektowanie Oprogramowania Systemów. Semestr letni 2026. Wybrany temat: 5. Tester mikroprocesorów.

Ta sekcja dotyczy oprogramowania testera, realizującego procedurę testową.

Projekt został stworzony dla programowawnia mikrokontrolera STM32G431C6T6.

Aby załadować projekt w środowisku STM32CubeIde wystaczy uruchomić plik .ioc zmienić ścieżkę workspace do ścieżki w której został pobrany folder.

Oprogramowanie zostało stworzono za narzędzia STMicroelectronics STM32cubeIde 1.15. Aktualna struktura projektu wygląda następująca:

- plik .ioc jest plikiem konfiguracyjnym projektu w STM32CubeIDE
- plik .mxproject jest plikiem konfiguracyjnym projektu w STM32CubeMX
- folder /Drivers/CMSIS zawiera pliki driverów niskopoziomowych do rdzenia ARM
- folder /Drivers/STM32G4xx_HAL_Driver zawiera pliki warstwy abstrakcji sprzętowej
- folder /Core/Scr zawiera pliki źródłowe opgragramowania projektu
- folder /Core/Inc zawiera pliki nagłówkowe opgragramowania projektu
