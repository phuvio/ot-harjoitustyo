# Travel Expense Calculator App

## Sovelluksen tarkoitus

Ryhmässä on mukava matkustaa. Välillä tulee kuitenkin kiistaa siitä, kuka on maksanut mitäkin laskuja ja kuinka paljon. Travel Expense Calculator -sovellukseen voi syöttää kaikki matkan aikana syntyneet kulut sekä tiedon siitä kuka on maksaja ja keille maksu kohdistuu. Sovellus pitää kirjaa maksuista ja laskee automaattisesti kaikkien matkalaisten maksamien laskujen saldon sekä laskee plus-miinus-tilaston jokaiselle matkalaiselle. Sovellukseen voi tallentaa useita matkoja ja niihin liittyviä maksuja.

Sovellus on tehty Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

# Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.8. 

## Dokumentaatio

- [Käyttöohje](./travel-expense-calculator-app/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](./travel-expense-calculator-app/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](./travel-expense-calculator-app/dokumentaatio/tuntikirjanpito.md)

- [ChangeLog](./travel-expense-calculator-app/dokumentaatio/changelog.md)

- [Arkkitehtuurikuvaus](./travel-expense-calculator-app/dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](./travel-expense-calculator-app/dokumentaatio/testaus.md)

- [Release](https://github.com/phuvio/ot-harjoitustyo/releases/tag/v1.0.0)


# Asennus

1. Siirry kansioon: */travel-expense-calculator-app*

2. Asenna riippuvuudet komennolla:

```bash
poetry install
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

# Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu *htmlcov*-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./travel-expense-calculator-app/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Autopep

Koodin formatointi automaattisesti PEP 8-tyyliohjeiden mukaisesti onnistuu komennolla:

```bash
poetry run invoke format
```

