# Generator śpiewników

Program, dzięki któremu możemy w łatwy i szybki sposób wygenerować śpiewnik w formacie docx.

Uwaga, program jest jedynie częścią projektu [śpiewnika online](https://spiewnik.mmakos.pl).
Nie generuje on śpiewników autonomicznie, lecz konwertuje nasz utworzony online śpiewnik *.smm* do formatu *.docx*.

Docelowo ze strony będzie można od razu pobierać pliki docx (konwersja będzie robiona już "na stronie"), ale obecnie
nie stać mnie na takie rozwiązanie (wymaga to opłacenia serwera z możliwością hostowania aplikacji napisanych w Python).

## Zainstaluj generator (Windows)

1. Pobierz [najnowszy instalator z github](https://github.com/mmakos/songbook2docx/releases).
2. Zainstaluj.

*Uwaga, prawdopodobnie uruchomią się jakieś antywirusy i inne — jest to standardowe zachowanie dla niecertyfikowanych aplikacji z nieznanych źródeł*.

Jeśli korzystasz z innego systemu, patrz niżej.

## Wygeneruj swój śpiewnik

Na stronie [śpiewnika online](https://spiewnik.mmakos.pl):
1. Utwórz spotkanie w menu **Spotkanie** lub dołącz do istniejącego, podając nazwę spotkania.
2. Otwórz piosenkę, którą chcesz dodać do śpiewnika.
3. Pod tekstem piosenki możesz zaznaczyć interesujące Cię opcje dla danej piosenki:
   * Transpozycja
   * Sposób wyświetlania akordów — *Uwaga, niektóre opcje mogą być dostępne tylko na stronie lub tylko online (przy każdej opcji jest informacja).*
   * Możesz zmienić ustawienia globalne (wtedy każda otwierana piosenka będzie miała zaznaczone odpowiednie parametry (oprócz tonacji)).
4. Po zaznaczeniu wybranych opcji kliknij gwiazdkę po prawej stronie nad tekstem.
5. Dodaj kolejne piosenki.
6. Po prawej stronie wyświetla się lista wybranych piosenek — możesz zmienić kolejność, przeciągając wybrane piosenki na inne miejsca.
7. W menu **Spotkanie** wybierz opcję **Zapisz spotkanie**.

## Przekonwertuj śpiewnik do DOCX

W tym momencie powinien zostać pobrany plik w formacie **SMM** — jest to twój śpiewnik, ale na razie zawiera dane (tekst, akordy, wybrane opcje) w moim formacie.
Aby utworzyć z tego plik *.docx*, należy:
1. Otwórz pobrany plik *.smm* za pomocą programu *Songbook2docx* (generator śpiewników):
   1. Kliknij dwukrotnie na plik (jeśli zainstalowałeś generator instalatorem, powinien domyślnie otworzyć się w tym programie)
   2. lub przeciągnij plik na ikonę programu
   3. lub uruchom program i wybierz odpowiedni plik.
2. Poczekaj, aż program stworzy śpiewnik w formacie *.docx*
3. Wybierz miejsce, gdzie ma być zapisany wyjściowy plik.
4. Po zapisaniu śpiewnik powinien się automatycznie otworzyć w programie word (lub innym programie skojarzonym z plikami *.docx*).

## Jak uruchomić program na innym systemie niż windows?

Ponieważ nawet nie posiadam urządzenia Apple, nie jestem w stanie zbudować projektu do dystrybucji na tym systemie.
Dlatego ta sekcja będzie wymagała nieco więcej wysiłku i wiedzy.

### Zainstaluj Python 3.9+
Do pobrania z https://www.python.org/downloads/

Przy instalacji zaznacz opcję *Dodaj Python do zmiennej PATH*.

### Pobierz i zainstaluj bibliotekę songbook2docx

1. Pobierz bibliotekę z [github](https://github.com/mmakos/songbook2docx/archive/refs/heads/master.zip).
   * Opcja **Code**->**Download ZIP**, wypakuj pliki
   * lub `git clone https://github.com/mmakos/songbook2docx.git`.
2. Przejdź do katalogu z pobranymi plikami (powinien być tam plik *main.py*, folder *songbook2docx* itd.)
3. Uruchom polecenie `pip install .` (jeśli jest błąd, to znaczy, że niepoprawnie zainstalowałeś Pythona).
4. Uruchom konwerter przy pomocy polecenia `python main.py`
5. Dalej powinno być tak samo, jak na windows.

## Plik konfiguracyjny
Jeżeli chcesz zmienić styl tekstu lub akordów, musisz to zrobić, zanim wygenerujesz śpiewnik — inaczej się rozjedzie.

W tym celu należy zmodyfikować plik *conf.ini* w katalogu, gdzie zainstalowałeś program.
Możliwe ustawienia są opisane w tym pliku.
