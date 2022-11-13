import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_paatteen_saldo_ja_myydyt_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # käteisostos
    def test_syo_edullisesti_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)

    def test_syo_edullisesti_lisaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_lisaa_rahaa_kassaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_syo_maukkaasti_lisaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_liian_vahan_rahaa_ei_muuta_tilannetta(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_liian_vahan_rahaa_ei_muuta_tilannetta(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # korttiostot
    def test_syo_edullisesti_vahentaa_rahaa_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        assert self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) == True

    def test_syo_edullisesti_kortilla_lisaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_vahentaa_rahaa_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        assert self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) == True

    def test_syo_maukkaasti_kortilla_lisaa_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_liian_vahan_rahaa_kortilla_ei_muuta_tilannetta(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(str(maksukortti), "Kortilla on rahaa 0.10 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)
        assert self.kassapaate.syo_edullisesti_kortilla(maksukortti) == False

    def test_syo_maukkaasti_liian_vahan_rahaa_kortilla_ei_muuta_tilannetta(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(str(maksukortti), "Kortilla on rahaa 0.10 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        assert self.kassapaate.syo_maukkaasti_kortilla(maksukortti) == False

    # rahan lataus kortille
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassan_rahamaara_kasavaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)

    def test_negatiivista_arvoa_ei_voi_ladata_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)