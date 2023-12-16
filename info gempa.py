# Import kelas Gempa dari file Gempa.py
from Gempa import Gempa

# Buat 5 object gempa
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Panggil fungsi dampak() pada masing-masing object gempa
gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()
