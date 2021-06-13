Python 3.7 albo wyżej.
Przed uruchomieniem projektu:
Windows:
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

Linux/ MacOS:
```
python3 -m venv env
source venv/bin/activate  LUB  source env/bin/activate
pip3 install -r requirements.txt
```

Żeby uruchomić projekt na localhost:
```
python manage.py runserver
```
a następnie wejść w url http://localhost:8000


Katalog zawierający implementację rozwiązania to nomad. Znajduje się w nim zarówno implementacja mechanizmów randomizacji, tagowania oraz klasa pełniąca funkcję middleware.

Przykład podpięcia middleware do ustawień Django znajduje się w katalogu mysite -> settings.py

Aby zobaczyć, jak działa strona z włączoną randomizacją, należy uruchomić projekt na localhost.
Aby zobaczyć, jak działa strona bez randomizacji, należy zakomentować linię w settings.py odpowiedzialną za podłączenie NomadMiddleware a następnie uruchomić projekt na localhost.

Randomizacja polega na podłożeniu zmiennych ciągów znakowych jako atrybuty 'id' oraz 'name' tagów HTML. Efekt randomizacji można zobaczyć poprzez wyświetlenie źródła strony internetowej
