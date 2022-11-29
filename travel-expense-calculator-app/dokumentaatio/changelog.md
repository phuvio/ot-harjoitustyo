# ChangeLog

## Viikko 3

- Lisätty Matkat-näkymä
- Lisätty TravelRepository-luokka, joka vastaa matkojen tallennuksesta sqlite-tietokantaan
- Lisätty TravelService-luokka, joka vastaa matkoihin liittyvän sovelluslogiikan koodista
- Käyttäjä näkee listan kaikista matkoista
- Käyttäjä voi lisätä uuden matkan (matka kovakoodattu, koska lisäys sivu puuttuu vielä)
- Testit jäivät kiinni luokkien riippuvuuksista aiheutuneeseen virheeseen, jota en löytänyt

## Viikko 4

- Muokattu tietokanta skeemaa
- Lisätty Payment-entiteetti
- Lisätty Participant-entiteetti
- Lisätty User-entiteetti
- Lisätty Kirjaudu sisään -näkymä
- Lisätty UserRepository-luokka, joka vastaa käyttäjän tallennuksesta sqlite-tietokantaan
- Lisätty UserService-luokka, joka vastaa käyttäjään liittyvästä sovelluslogiikan koodista
- Lisätty Luo uusi käyttäjä -näkymä
- Lisätty uuden käyttäjän luomiseen liittyvät virheilmoitukset
- Lisätty sisäänkirjautumiseen liittyvät virheilmoitukset
- Ohjelmassa voi luoda uuden käyttäjän, joka kirjautuu automaattisesti sisään
- Käyttäjä voi kirjautua sisään jo aikaisemmin luodulla käyttäjätunnuksella
- Käyttäjä voi luoda uuden matkan (matka on kovakoodattu, koska matkan lisäys -sivu puuttuu vielä)
