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
   U->>+S: login("Petteri", "salasana")
   S->>+R: find_by_username("Petteri")
   R->>-S: user
   S->>-U: user
   U->>U: show_travel_view()

```

Sisäänkirjautuminen-painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan `UserService` metodia `login` antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää `UserRepository`:n avulla onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasanat. Jos salasanat täsmäävät, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi `ShowTravelView`, eli sovelluksen varsinaisen päänäkymän ja listaa näkymään kirjautuneen käyttäjän tallennetut matkat.

#### Uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus, joka ei ole jo käytössä sekä salasana, jonka jälkeen klikataan Luo uusi käyttäjä -painiketta etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor K as Käyttäjä
  participant UI
  participant S as UserService
  participant R as UserRepository
  participant matti
  K->>UI: click "Luo uusi käyttäjä" button
  UI->>+S: create_user("matti", "matti123")
  S->>+R: find_by_username("matti")
  R-->>-S: None
  S->>+R: create(matti)
  R->>matti: User("matti", "matti123")
  R-->> -S: user
  S-->>-UI: user
  UI->>UI: show_travel_view()
```

[Tapahtumakäsittelijä](https://github.com/phuvio/ot-harjoitustyo/blob/main/travel-expense-calculator-app/src/ui/ui.py#L65) kutsuu sovelluslogiikan metodia [create_user](https://github.com/phuvio/ot-harjoitustyo/blob/main/travel-expense-calculator-app/src/services/user_service.py#L28) antaen parametriksi luotavan käyttäjän tiedot. Sovelluslogiikka selvittää `UserRepository`:n avulla onko käyttäjätunnus olemassa. Jos ei, eli uuden käyttäjän luominen on mahdollista, luo sovelluslogiikka `User`-olion ja tallettaa sen kutsumalla `UserRepository`:n metodia `create`. Tästä seurauksena on se, että käyttöliittymä vaihtaa näkymäksi `ShowTravelView`:n. Luotu käyttäjä kirjataan automaattisesti sisään.

#### Uuden matkan luominen

Kun sisäänkirjautunut käyttäjä luo uuden matkan, niin sovelluksen kontrolli etenee seuraavasti:

```mermaid
 sequenceDiagram
   Actor K as Käyttäjä
   participant U as UI
   participant T as Travel <br> Service
   participant TR as Travel <br> Repository
   participant P as Participant <br> Service
   participant PR as Participant <br> Repository
   participant J as Jaana
   participant M as Retki
   K->>U: click "Lisää uusi matka" button
   U->>U: show_create_travel_view()
   K->>U: click "Luo uusi matkustaja"
   U->>U: show_create_participant_view()
   K->>U: click "Luo uusi matkustaja"
   U->>+P: get_participants_by_guide("Petteri")
   P->>+PR: find_by_guide("Petteri")
   PR->>-P: list(Participants)
   P->>-U: list(Participants)
   U->>+P: create_participant("Jaana", "*", "Petteri")
   P->>+PR: create(participant)
   PR->>J: Participant("Jaana", "*","Petteri")
   PR->>-P: participant
   P->>-U: participant
   U->>U: show_create_travel_view()
   K->>U: click "Lisää uusi matka"
   U->>+T: create_travel("Retki", "Petteri")
   T->>+TR: create(travel)
   TR->>M: Travel("Retki","Petteri")
   TR->>-T: travel
   T->>-U: travel
   U->>+P: create_participant("Jaana", "Retki", "Petteri")
   P->>+PR: create(participant)
   PR->>J: Participant("Jaana","Retki","Petteri")
   PR->>-P: participant
   P->>-U: participant
   U->>U: show_travel_view()

```

`Lisää uusi matka` -painikkeen painamiseen reagoiva tapahtumankäsittelijä vaihtaa näkymäksi `CreateTravelView`. Näkymässä kirjautunut käyttäjä voi antaa uudelle matkalle nimen sekä valita matkan matkustajat. Aluksi matkustajaluettelossa on vain sisäänkirjautunut käyttäjä. 

Uusia matkustajia voi lisätä matkustajaluetteloon Luo uusi matkustaja -painiketta painamalla. Painikkeen painamiseen reagoiva tapahtumakäsittelijä vaihtaa näkymäksi `CreateParticipantView`. `CreateParticipantView`-näkymässä painamalla `Luo uusi matkustaja` -painiketta sen tapahtumakäsittelijä kutsuu sovelluslogiikan `ParticipantService` metodia `get_participants_by_guide`, joka etsii sisäänkirjautuneen käyttäjän tallentamat matkustajat. Metodi kutsuu `ParticipantRepository`:n metodia `find_by_guide`, joka palauttaa luettelon sisäänkirjautuneen käyttäjän tallentamista matkustajista `Participant`-olioina. Sovelluslogiikka tarkastaa onko luettelossa annettu matkustajan nimi. Mikäli ei ole, niin painikkeen tapahtumakäsittelijä kutsuu `ParticipantService`:n metodia `create_participant`. Parametreiksi annetaan matkustajan nimi, matkan nimeksi \*-merkki sekä sisäänkirjautuneen käyttäjän `username`. Metodi kutsuu `ParticipantRepository`:n metodia `create`, jolle annetaan parametriksi `Participant`-olio. Molemmat metodit palauttavat tallennetun `Participant`-olion. Lopuksi sovelluslogiikka vaihtaa näkymäksi takaisin `CreateTravelView`:n, eli uuden matkan luominen -näkymän. 

Käyttäjä voi tallentaa uuden matkan `Lisää uusi matka` -painiketta painamalla. Painikkeen painamiseen reagoiva tapahtumakäsittelijä kutsuu sovelluslogiikan `TravelService` metodia `create_travel`, jonka parametreina ovat matkan nimi ja sisäänkirjautuneen käyttäjän `username`. Sovelluslogiikka yrittää tallentaa matkaa kutsumalla `TravelRepository`:n metodia `create`, jonka parametriksi annetaan sovelluslogiikan luoma `Travel`-olio. Mikäli tallennus onnistuu, niin sen jälkeen sovelluslogiikka tallentaa jokaisen matkustajaluettelosta valitun matkustajat tietokantaan matkan nimen ja sisäänkirjautuneen käyttäjän nimellä kutsumalla `ParticipantService`:n metodia `create_participant`. Lopuksi sovelluslogiikka vaihtaa näkymäski päänäkymän `ShowTravelView`.
