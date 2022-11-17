# Tehtävä 1: Monopoli

```mermaid
 classDiagram
      Peli "1"--"2" Noppa
      Peli "1"--"1" Lauta
      Lauta "1"--"40" Ruutu
      Ruutu "1"--"0..8" Pelinappula
      Pelinappula "1"--"1" Pelaaja
      Pelaaja "2..8"--"1" Peli
      class Peli{
      }
      class Lauta{
      }
      class Ruutu{
      seuraava ruutu
      }
      class Pelaaja{
      }
      class Pelinappula{
      }
      class Noppa{
      }
```

# Tehtävä 2: Monopoli

```mermaid
 classDiagram
      Peli "1"--"2" Noppa
      Peli "1"--"1" Lauta
      Lauta "1"--"40" Ruutu
      Ruutu "1"--"0..8" Pelinappula
      Pelinappula "1"--"1" Pelaaja
      Pelaaja "2..8"--"1" Peli
      Pelaaja "1"--"*" Raha
      Sattuma_ja_yhteismaa -- Kortti
      Normaalit_kadut "1"--"0..4" Talo
      Normaalit_kadut "1"--"0..1" Hotelli
      Pelaaja "1"--"*" Normaalit_kadut
      class Peli{
      }
      class Lauta{
      }
      class Ruutu{
      seuraava ruutu
      toiminto
      }
      class Raha{
      }
      class Pelaaja{
      }
      class Pelinappula{
      }
      class Noppa{
      }
      class Aloitus{
      sijainti
      }
      class Vankila{
      sijainti
      }
      class Sattuma_ja_yhteismaa{
      }
      class Kortti{
      toiminto
      }
      class Asemat_ja_laitokset{
      }
      class Normaalit_kadut{
      nimi
      }
      class Hotelli{
      }
      class Talo{
      }
```
