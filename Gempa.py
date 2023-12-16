class Gempa:
    """
    Kelas untuk menyimpan informasi gempa

    Atribut:
        lokasi: lokasi gempa
        skala: skala gempa

    Fungsi:
        dampak(): mencetak dampak gempa
    """

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif 2 <= self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif 4 <= self.skala <= 6:
            print("Dampak gempa bangunan roboh")
        else:
            print("Dampak gempa bangunan roboh dan berpotensi tsunami")

