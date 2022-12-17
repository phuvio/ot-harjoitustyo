# Vaatimusmäärittely

# Sovelluksen tarkoitus

Ryhmässä on mukava matkustaa. Välillä tulee kuitenkin kiistaa siitä, kuka on maksanut mitäkin laskuja ja kuinka paljon. **Travel Expense Calculator** -sovellukseen voi syöttää kaikki matkan aikana syntyneet kulut sekä tiedon siitä kuka on maksaja ja keille maksu kohdistuu. Sovellus pitää kirjaa maksuista ja laskee automaattisesti kaikkien matkalaisten maksamien laskujen saldon sekä plus-miinus-tilaston jokaiselle matkalaiselle. Sovellukseen voi tallentaa useita matkoja.

## Käyttäjät

Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä. Jokainen käyttäjä näkee vain omat tallentamansa matkat, matkustajat ja maksut. Kirjautunut käyttäjä toimii *matkanjohtajana*, joka voi lisätä uusia matkoja, matkustajia ja maksuja.

## Käyttöliittymäluonnos

Sovellus koostuu yhdeksästä eri näkymästä.

![Käyttöliittymäluonnos](https://github.com/phuvio/ot-harjoitustyo/blob/main/travel-expense-calculator-app/dokumentaatio/kuvat/k%C3%A4ytt%C3%B6liittym%C3%A4luonnos.png)

Sovellus aukeaa *kirjautumisnäkymään*, josta on mahdollista siirytä *uuden käyttäjän luomisnäkymään* tai onnistuneen kirjautumisen yhteydessä *matkat-näkymään*. *Matkat-näkymässä* voi siirtyä *uuden matkan luomisnäkymään* tai valita jonkun luettelossa olevista matkoista. *Uuden matkan luomisnäkymässä* voi luoda uuden matkan ja valita sille osallistujat sekä matkanjohtajan tai siirtyä *luo uusi matkustaja -näkymään*. *Luo uusi matkustaja -näkymässä* voi luoda uuden matkustajan. *Matkat-näkymästä* voi siirtyä *maksut-näkymään* valitsemalla jonkun *matkat-näkymässä* näkyvistä matkoista. *Maksut-näkymässä* näkyvät matkan maksut ja kuka maksun on maksanut. Matkalle voi lisätä uusia maksuja *luo uusi maksu -näkymässä*. *Luo uusi maksu -näkymässä* luodaan uusi maksu ja syötetään maksun tiedot. *Maksut-näkymästä* voi valita yksittäisen maksun, jolloin *maksun tiedot -näkymässä* näkyvät laskun kaikki tiedot. Lisäksi *maksut-näkymästä* pääsee myös *yhteenveto-näkymän*, jossa on yhteenveto jokaisen matkalaisen suorittamista maksuista, laskelma jokaiselle matkalaiselle kohdistuneista ostoksista sekä jokaisen matkalaisen plus-miinus-tilasto.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen - tehty
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä - tehty
- Käyttäjä voi kirjautua järjestelmään - tehty
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjaudu sisään -näkymässä - tehty

### *Matkat-näkymä*
 
- Käyttäjä näkee luettelon sovellukseen luoduista matkoista - tehty
- Käyttäjä voi luoda uuden matkan *lisää matka -näkymässä* - tehty
- Käyttäjä voi valita luettelosta matkan, jolloin hän pääsee valitun matkan *maksut-näkymään* - tehty

### *Lisää matka -näkymä*
- Käyttäjä voi luoda uuden matkan - tehty
  - Matkalle pitää antaa nimi, jonka täytyy olla uniikki - tehty
  - Matkalle valitaan osallistujat, joita kirjautunut käyttäjä voi luoda - tehty

### *Luo uusi matkustaja -näkymä*
- Kirjautunut käyttäjä voi luoda uuden matkustajan - tehty
  - Matkustajalle pitää antaa nimi, jonka täytyy olla uniikki - tehty

### *Maksut-näkymä*

- Käyttäjä näkee matkalle tallennetut maksut - tehty
  - Jokaisen maksun kohdalla näkyvät - tehty
    - Maksun nimi
    - Maksun summa
    - Maksajan nimi
- Käyttäjä voi hän lisätä uuden maksun matkalle siirtymällä *luo uusi maksu -näkymään* - tehty
- Valitsemalla maksun, siirtyy *maksun tiedot -näkymään*, jossa näkyvät kyseisen maksun tiedot - tehty
- Käyttäjä voi siirtyä *yhteenveto-näkymään*, jossa on matkan maksujen yhteenveto - tehty

### *Uusi lasku -näkymä*

- Käyttäjä kirjaa - tehty
  - Uuden maksun nimen, jonka pitää olla uniikki - tehty
  - Maksun summan - tehty
  - Maksun maksajan - tehty
  - Miten maksu jakautuu matkan osallistujien kesken - tehty
  - Maksun päivämäärän - tehty
  - Maksun lisätiedot - tehty

### *Maksun tiedot -näkymä*

- Näyttää valitun maksun tiedot  - tehty

### *Yhteenveto-näkymä*

- *Yhteenveto-näkymässä* on laskelma, jossa näkyvät - tehty
  - Jokaisen matkalaisen maksamien laskujen summa - tehty
  - Jokaiseen matkalaiseen kohdistuvien ostosten summa - tehty
  - Jokaisen matkalaisen plus-miinus-tilasto, jossa näkyy onko matkalainen maksanut enemmän tai vähemmän kuin oman osuutensa - tehty

## Jatkokehitysideoita

Ohjelmaan on mahdollista lisätä seuraavia toiminnallisuuksia:

- Lisätä yhteenveto-näkymään laskelma miten matkan päätyttyä maksut tasataan 
- Kieliversiot
- Matkan tietojen muokkaaminen
- Matkan poistaminen
- Maksun tietojen muokkaaminen
- Maksun poistaminen
- Matkustajan poistaminen
- Yhteenvedon lähettäminen annettuun sähköpostiin
- Pääkäyttäjäroolin lisääminen
  - Pääkäyttäjä voi poistaa käyttäjiä
