# Travel Expense Calculator App

## Sovelluksen tarkoitus

Ryhmässä on mukava matkustaa. Välillä tulee kuitenkin kiistaa siitä, kuka on maksanut mitäkin laskuja ja kuinka paljon. Travel Expense Calculator -sovellukseen voi syöttää kaikki matkan aikana syntyneet kulut sekä tiedon siitä kuka on maksaja ja keille maksu kohdistuu. Sovellus pitää kirjaa maksuista ja laskee automaattisesti kaikkien matkalaisten maksamien laskujen saldon sekä laskee plus-miinus-tilaston jokaiselle matkalaiselle. Sovellukseen voi tallentaa useita matkoja ja niihin liittyviä maksuja.

Sovellus on tehty Helsingin yliopiston Tietojenkäsittelytieteen kurssin Ohjelmistotekniikka harjoitustyönä.

# Huomio Python-versiosta

Sovelluksen toiminta on testattu Python-versiolla 3.8. 

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

- [ChangeLog](./dokumentaatio/changelog.md)


# Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
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

Testit eivät tällä hetkellä mene läpi.

