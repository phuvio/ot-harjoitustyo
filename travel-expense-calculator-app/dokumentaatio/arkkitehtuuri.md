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
   U->>U: show_travel_view

```

Sisäänkirjautuminen-painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu sovelluslogiikan TUserService metodia login antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää UserRepository:n avulla onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasanat. Jos salasanat täsmäävät, kirjautuminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi ShowTravelView, eli sovelluksen varsinaisen päänäkymän ja listaa näkymään kirjautuneen käyttäjän tallennetut matkat.

#### Uuden käyttäjän luominen

Kun uuden käyttäjän luomisnäkymässä on syötetty käyttäjätunnus, joka ei ole jo käytössä sekä salasana, jonka jälkeen klikataan Luo uusi käyttäjä -painiketta etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
  actor K as Käyttäjä
  participant UI
  participant S as UserService
  participant R UserRepository
  participant matti
  K->>UI: click "Luo uusi käyttäjä" button
  UI->>+S: create_user("matti", "matti123")
  S->>+R: find_by_username("matti")
  R-->>-S: None
  S->>matti: User("matti", "matti123")
  S->>+R: create(matti)
  R-->> -S: user
  S-->>-UI: user
  UI->>UI: show_travel_view()
```

[Tapahtumakäsittelijä](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/ui/create_user_view.py#L18) kutsuu sovelluslogiikan metodia [create_user](https://github.com/ohjelmistotekniikka-hy/python-todo-app/blob/master/src/services/todo_service.py#L130) antaen parametriksi luotavan käyttäjän tiedot. Sovelluslogiikka selvittää `UserRepository`:n avulla onko käyttäjätunnus olemassa. Jos ei, eli uuden käyttäjän luominen on mahdollista, luo sovelluslogiikka `User`-olion ja tallettaa sen kutsumalla `UserRepository`:n metodia `create`. Tästä seurauksena on se, että käyttöliittymä vaihtaa näkymäksi `ShowTravelView`:n. Luotu käyttäjä kirjataan automaattisesti sisään.

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
   U->>+P: create_participant("Jaana", "", user.username)
   P->>+PR: create(participant)
   PR->>-P: participant
   P->>-U: participant
   U->>U: show_create_travel_view
   K->>U: click "Lisää uusi matka"
   U->>+T: create_travel("Retki", user.username)
   T->>+TR: create(travel)
   TR->>-T: travel
   T->>-U: travel
   U->>+P: create_participant("Jaana", "Retki", user.username)
   P->>+PR: create(participant)
   PR->>-P: participant
   P->>-U: participant
   U->>U: show_travel_view

```

Lisää uusi matka -painikkeen painamiseen reagoiva tapahtumankäsittelijä vaihtaa näkymäksi CreateTravelView. Näkymässä kirjautunut käyttäjä voi antaa uudelle matkalle nimen sekä valita matkan matkustajat. Aluksi matkustajaluettelossa on vain sisäänkirjautunut käyttäjä. Uusia matkustajia voi lisätä matkustajaluetteloon Luo uusi matkustaja -painiketta painamalla. Painikkeen painamiseen reagoiva tapahtumakäsittelijä vaihtaa näkymäksi CreateParticipantView. CreateParticipantView-näkymässä painamalla Luo uusi matkustaja -painiketta sen tapahtumakäsittelijä kutsuu sovelluslogiikan ParticipantService metodia create_participant. Parametriksi annetaan matkustajan nimi. Sovelluslogiikka selvittää ParticipantRepository:n avulla onko nimi jo tallennettu sisäänkirjautuneen käyttäjän nimellä. Jos ei ole, niin uuden matkustajan tallentaminen onnistuu. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi takaisin CreateTravelView:n, eli uuden matkan luominen -näkymän. Käyttäjä voi tallentaa uuden matkan Lisää uusi matka -painiketta painamalla. Painikkeen painamiseen reagoiva tapahtumakäsittelijä kutsuu sovelluslogiikan TravelService metodia create_travel, jonka parametreina ovat matkan nimi ja matkustajaluettelosta valitut matkustajat. Sovelluslogiikka selvittää TravelRepository:n avulla onko matkan nimi jo tallennettu sisäänkirjautuneen käyttäjän nimellä. Jos ei ole, niin uuden matkan tallentaminen onnistuu. Samalla jokainen valittu matkustaja tallennettaan tietokantaan matkan nimen ja sisäänkirjautuneen käyttäjän nimellä. Lopuksi käyttöliittymä vaihtaa näkymäski päänäkymän ShowTravelView.
