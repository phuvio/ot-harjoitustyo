# ChangeLog

## Viikko 3

- Lisätty Matkat-näkymä
- Lisätty TravelRepository-luokka, joka vastaa matkojen tallennuksesta sqlite-tietokantaan
- Lisätty TravelService-luokka, joka vastaa matkoihin liittyvän sovelluslogiikan koodista
- Käyttäjä näkee listan kaikista matkoista
- Käyttäjä voi lisätä uuden matkan (matka kovakoodattu, koska lisäys sivu puuttuu vielä)
- Testit jäivät kiinni luokkien riippuvuuksista aiheutuneeseen virheeseen, jota en löytänyt

## Viikko 4

- Muokattu tietokantaskeemaa
- Lisätty Payment-entiteetti
- Lisätty Participant-entiteetti
- Lisätty User-entiteetti
- Lisätty Kirjaudu sisään -näkymä
- Lisätty UserRepository-luokka, joka vastaa käyttäjän tallennuksesta sqlite-tietokantaan
- Lisätty UserService-luokka, joka vastaa käyttäjään liittyvästä sovelluslogiikan koodista
- Lisätty Luo uusi käyttäjä -näkymä
- Lisätty uuden käyttäjän luomiseen liittyvät virheilmoitukset
- Lisätty sisäänkirjautumiseen liittyvät virheilmoitukset
- Tehty testit luokille TravelRepository, TravelService, UserRepository ja UserService
- Ohjelmassa voi luoda uuden käyttäjän, joka kirjautuu automaattisesti sisään
- Käyttäjä voi kirjautua sisään jo aikaisemmin luodulla käyttäjätunnuksella
- Käyttäjä voi luoda uuden matkan (matka on kovakoodattu, koska matkan lisäys -sivu puuttuu vielä)

## Viikko 5

- Lisätty ParticipantRepository-luokka, joka vastaa matkustajan tallennuksesta sqlite-tietokantaan
- Lisätty ParticipantService-luokka, joka vastaa matkustajaan liittyvästä sovelluslogiikan koodista
- Lisätty Luo uusi matka -näkymä
- Lisätty Luo uusi matkustaja -näkymä
- Lisätty uuden matkan luomiseen liittyvät virheilmoitukset
- Lisätty uuden matkustajan luomiseen liittyvät virheilmoitukset
- Lisätty PaymentRepository-luokka, joka vastaa maksun tallennuksesta sqlite-tietokantaan
- Lisätty PaymentService-luokka, joka vastaa maksuun liittyvästä sovelluslogiikan koodista
- Lisätty Maksut-näkymä
- Tehty testit luokille ParticipantRepository, ParticipantService, PaymentRepository ja PaymentService
- Käyttäjä voi luoda uuden matkan
- Käyttäjä voi luoda uuden matkustajan
- Käyttäjä voi valita luodun matkan Matka-näkymässä, jolloin näkymäksi muuttuu Maksut-näkymä

## Viikko 6

- Lisätty Luo uusi maksu -näkymä
- Lisätty Yksittäinen maksu -näkymä
- Lisätty Yhteenveto-näkymä
- Lisätty uuden maksun luomiseen liittyvät virheilmoitukset
- Lisätty DateEntry-kirjasto
- Laajennettu testejä vastaamaan uutta koodia
- Käyttäjä voi luoda uuden maksun
- Käyttäjä näkee yksittäisen maksun tiedot
- Käyttäjä näkee matkan maksujen yhteenvedon

## Viikko 7

- Ohjelman viimeistely
- Käyttöohje
- Testausdokumentti
- Dokumentaation viimeistely
