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
   U->>+S: login("nimi", "salasana")
   S->>+R: find_by_username("nimi")
   R->>-S: user
   S->>-U: user
   U->>U: show_travel_view

```

#### Uuden matkan luominen

Kun sisäänkirjautunut käyttäjä luo uuden matkan, niin sovelluksen kontrolli etenee seuraavasti:

```mermaid
 sequenceDiagram
   Actor K as Käyttäjä
   participant U as UI
   participant T as TravelService
   participant TR as TravelRepository
   participant P as ParticipantService
   participant PR as ParticipantRepository
   K->>U: click "Lisää uusi matka" button
   U->>U: show_create_travel_view
   K->>U: click "Luo uusi matkustaja"
   U->>U: show_create_participant_view
   U->>+P: create_participant("nimi", "", user.username)
   P->>+PR: create(participant)
   PR->>-P: participant
   P->>-U: participant
   U->>U: show_create_travel_view
   K->>U: click "Lisää uusi matka"
   U->>T: create_travel("matkan nimi", user.username)
   T->>TR: create(travel)
   TR->>T: travel
   T->>U: travel
   U->>U: show_travel_view

```
