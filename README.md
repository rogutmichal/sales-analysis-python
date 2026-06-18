#  Analiza danych sprzedażowych (Python + Pandas + Matplotlib)

##  Opis projektu

Ten projekt to kompletny pipeline analizy danych sprzedażowych stworzony w Pythonie. Obejmuje on wczytanie danych, ich czyszczenie, preprocessing, obliczanie kluczowych wskaźników biznesowych (KPI), agregacje oraz wizualizacje.

Celem projektu jest szybka analiza wyników sprzedaży oraz identyfikacja najważniejszych trendów w danych.

---

##  Technologie

- Python 3
- Pandas – analiza i przetwarzanie danych
- Matplotlib – wizualizacja danych

---

##  Proces analizy danych

### 1. Wczytanie danych
- Import danych z pliku CSV
- Walidacja wymaganych kolumn
- Czyszczenie tekstu (usuwanie zbędnych spacji)

### 2. Przetwarzanie danych (preprocessing)
- Konwersja dat do formatu datetime
- Konwersja wartości numerycznych (Price, Quantity)
- Usuwanie błędnych i pustych danych
- Usuwanie duplikatów
- Tworzenie nowych kolumn:
  - Revenue (przychód)
  - Month
  - DayOfWeek
  - Year

### 3. Analiza KPI
Projekt oblicza kluczowe wskaźniki biznesowe:

- liczba zamówień
- całkowity przychód
- średnia wartość zamówienia
- liczba unikalnych produktów
- liczba miast

### 4. Agregacja danych
Dane są grupowane według:

- miast
- produktów
- menedżerów
- typu zakupu
- metody płatności

### 5. Wizualizacja danych
Projekt generuje wykresy:

-  przychód według miasta
  <img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/266549a0-6374-412a-a5d7-de9e87175ec2" />

-  przychód według produktu
-  trend sprzedaży w czasie
-  przychody według metody kupna
-  przychody według metody płatności
