Sistem de online banking

Proiectul va presupune implementarea unui sistem de online banking disponibil atat in varianta web, cat si mobile. Sistemul va fi securizat prin multi-factor authentication, astfel incat, pentru a-si accesa contul, dupa introducerea numelui de utilizator si a parolei, clientul va primi un token prin e-mail pentru a-si certifica identitatea. Informatiile despre utilizatori vor fi pastrate intr-o baza de date centralizata.
Sistemul va permite utilizatorului sa vizualizeze soldul contului sau, cat si sa descarce un document ce contine extrasul de cont, sa realizeze transferuri bancare, sa-si administreze conturile si sa deschida noi conturi, cat sa isi si gestioneze cardurile atasate conturilor. De asemenea, atat aplicatia web, cat si cea mobile vor trimite notificari via e-mail utilizatorilor in perioada apropiata expirarii cardurilor detinute de acestia. Aplicatia mobile va permite utilizatorilor sa apeleze call center-ul bancii direct si va dispune si de o caseta in care utilizatorul poate trimite e-mail reprezentantilor bancii. Vom incerca, de asemenea, implementarea unei functionalitati de plata catre comercianti via NFC.


Utilizare

1. sudo source internet_banking/virtualenv/bin/activate
2. python3 run.py
3. Ca sa iesiti din virtualenv: deactivate 


Daca nu folositi virtualenv: 
    pip3 install -r requirements.txt