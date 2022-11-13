# Vaatimusmäärittely

# Scoelluksen tarkoitus

Ryhmässä on mukava matkustaa. Välillä tulee kuitenkin kiistaa siitä, kuka on maksanut mitäkin laskuja ja kuinka paljon. Travel Expense Calculato -sovellukseen voi syöttää kaikki matkan aikana syntyneet kulut sekä tiedon siitä kuka on maksaja ja keille maksu kohdistuu. Sovellus pitää kirjaa maksuista ja laskee automaattisesti kaikkien matkalaisten maksamien laskujen saldon sekä plus-miinus-tilaston jokaiselle matkalaiselle. Sovellukseen voi tallentaa useita matkoja.

## Käyttäjät

Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä. Kaikilla käyttäjillä on kirjautuessa sama rooli. Mutta jokaisella matkalla voi olla vain yksi matkanjohtaja, jolla on oikeus kirjata kuitteja ja laskuja sovellukseen.

## Käyttöliittymäluonnos

Sovellus koostuu seitsemästä eri näkymästä.

Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista siirytä uuden käyttäjän luomisnäkymään tai onnistuneen kirjautumisen yhteydessä matkaluetteloon. Matkaluettelosta voi siirtyä uuden matkan luomisnäkymään, jossa voi luoda uuden matkan ja valita sille osallistujat sekä matkanjohtajan, tai valita jonkun luettelossa olevista matkoista. Tällöin siirrytään valitun matkan näkymään, jossa näkyvät matkan maksut ja kuka maksun on maksanut. Matkanjohtaja voi lisätä uusia maksuja luetteloon. Uusien maksujen näkymässä luodaan uusi maksu, syötetään maksulle summa, päivämäärä ja maksajat sekä valitaan kenelle maksu kohdistuu. Matka-näkymästä voi jokainen käyttäjä valita myös yhteenveto-näkymän, jossa on yhteenveto jokaisen matkalaisen suorittamista maksuista, laskelma jokaiselle matkalaiselle kohdistuneista maksuista sekä jokaisen matkalaisen plus-miinus-tilasto.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjaudu sisään -näkymässä

### Kirjautumisen jälkeen
 
- Käyttäjä näkee luettelon sovellukseen luoduista matkoista
- Käyttäjä voi luoda uuden matkan lisää matka -näkymässä
- Käyttäjä voi valita luettelosta matkan, jolloin hän pääsee valitun matkan matkan laskut -näkymään

### Lisää matka -näkymä
- Käyttäjä voi luoda uuden matkan
  - Matkalle pitää antaa nimi, jonka täytyy olla uniikki
  - Matkalle valitaan osallistujat, jotka voivat olla sovellukseen käyttäjätunnuksen luoneita käyttäjiä
  - Matkalle valitaan matkanjohtaja, jolla on oikeus lisätä uusia maksuja matkalle

### Matka-näkymä

- Käyttäjä näkee matkalle tallennetut maksut
  - Jokaisen maksun kohdalla näkyvät
    - Maksun nimi
    - Maksun summa
    - Maksajan/ien nimi
    - Maksun päivämäärä
- Jos käyttäjä on matkan matkanjohtaja, voi hän lisätä uuden maksun matkalle
- Jokainen käyttäjä voi siirtyä yhteenveto-näkymään, jossa on matkan maksujen yhteenveto

### Uusi lasku -näkymä

- Matkanjohtaja kirjaa 
  - Uuden maksun nimen, jonka pitää olla uniikki
  - Maksun summan
  - Maksun maksajan
  - Miten maksu jakautuu matkan osallistujien kesken
  - Maksun päivämäärän 

### Yhteenveto-näkymä

- Yhteenveto-näkymässä on laskelma, jossa näkyvät
  - Jokaisen matkalaisetn maksamien laskujen summa
  - Jokaiseen matkalaiseen kohdistuvien laskujen summa
  - Jokaisen matkalaisen plus-miinus-tilasto, jossa näkyy onko matkalainen maksanut enemmän tai vähemmän kuin oman osuutensa

## Jatkokehitysideoita

Perusversion jälkeen on mahdollista lisätä, mikäli aikaa jää, seuraavia toiminnallisuuksia:

- Lisätä yhteenveto-näkymään laskelma miten matkan päätyttyä maksut tasataan 
- Kieliversiot
- Yhteenvedon lähettäminen pdf-tiedostona annettuun sähköpostiin
- Pääkäyttäjäroolin lisääminen
  - Pääkäyttäjä voi poistaa matkoja ja henkilöitä
