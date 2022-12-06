# Arkkitehtuurikuvaus

### Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/arkkitehtuuri-pakkaus.png)

Pakkaus ui sisältää käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus entities sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tietokohteita.

### Tietokantaskeema

Ohjelman tietokantaskeema on seuraava:

![Tietokanta skeema](./kuvat/database-schema.png)

### Päätoiminnallisuudet

Ohjelman päätoiminnallisuudet sekvenssikaavioina:


#### Käyttäjän kirjautuminen sisään

Kun kirjautumisnäkymän syötekenttiin kirjoitetetataan käyttäjätunnus ja salasana, jonka jälkeen klikataan painiketta Sisäänkirjautuminen, etenee sovelluksen kontrolli seuraavasti:

```mermaid
 sequenceDiagram
   Actor K as Käyttäjä
   participant U as UI
   participant S as UserService
   participant R as UserRepository
   K->>U: click "Sisäänkirjautuminen" button
   U->>S: login("nimi", "salasana")
   S->>R: find_by_username("nimi")
   R->>S: user
   S->>U: user
   U->>U: show_travel_view

```
