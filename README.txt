Program do pobierania danych od użytkownika w formie instalatora. 

URUCHOMIENIE
Żeby uruchomić program należy (po uprzednim zainstalowaniu PyQt5) wywołać z terminala komendę
>>>python3 main.py

OPIS
Pliki:
Widoki:
firstPageView.ui / firstPageView.py
...
fifthPageView.ui / fifthPageView.py

main.py - plik scalający widoki i tworzący instancje
kody_sqlite.csv - plik zawierający kody pocztowe miast i nazwy miast
sq_db.db - baza danych zawierająca dane z pliku csv
user_data.txt - plik tekstowy, do którego eksportowane są dane z wypełnionego formularza

Instalator składa się z 5 okien. Do wykonania UI użyty został PyQt5, GUI wykoanane w QtDesigner. 
Program jest zbudowany w oparciu o moduł PyQt QWizard, który ułatwia obslugę poruszania się po kolejnych stronach, 
oraz ułatwia korzystanie z modułów wymuszających wypełnienie pola, obliczanie kolejej strony, lub rozpatrywanie ich jako strony niezależne.
Kolejne strony zbudowane zostały w oparciu o QWizardPage.
plikiem scalających widoki jest plik main.py
Każda strona Wizard'a jest osobną instancją klasy QWizardPage

Dla ułatwienia interakcji z programem wprowadzone zostały takie właściwości jak:
	WYBÓR KODÓW POCZTOWYCH Z BAZY DANYCH
	wypełniając kod pocztowy miasta, użytkownik może wybrać kod z listy dzięki zastowaniyu funkcji Completer
	 
	AUTOUZUPEŁNIANIE POLA MIASTO
	Kod wybrany z listy następnie jest podawany do zapytania sql, które filtruje inną kolumnę bazy danych 'sq_db.db' i znajduje odpowiadające kodowi miasto.
	Następnie nazwa miasta jest automatycznie przekazana do pola formularza 'miasto'.

	ZABEZPIECZENIE PRZED NIEKOMPLETNOŚCIĄ FORMULARZA
	Formularz nie uaktywni przycisku 'Next' dla użytkownika, jesli ten nie wypełnił wymaganych pól.

	PRZESŁANIE DANYCH DO PLIKU USER_DATA.TXT
	Dane zatwierdzone przyciskiem Finish są exportowane do pliku txt.
