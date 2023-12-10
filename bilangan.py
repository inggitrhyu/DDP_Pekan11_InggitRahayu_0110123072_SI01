def tambah(bil1, bil2):
    hasil = (bil1, bil2)
    print('hasil penjumlahan', bil1, "+", bil2, "=", hasil)

def kurang(bil1, bil2):
    hasil = (bil1, bil2)
    print('hasil pengurangan', bil1, "+", bil2, "=", hasil)

def kali(bil1, bil2):
    hasil = (bil1, bil2)
    print('hasil perkalian', bil1, "+", bil2, "=", hasil)

def bagi(bil1, bil2):
    hasil = (bil1, bil2)
    print('hasil pembagian', bil1, "+", bil2, "=", hasil)

def pangkat(bil1, bil2):
    import math
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)


def akar_kuadrat(bil):
    import math
    hasil = math.sqrt(bil)
    print("Akar kuadrat dari", bil, "=", hasil)

def logaritma(bil, base):
    import math
    hasil = math.log(bil, base)
    print("Logaritma dari", bil, "dengan basis", base, "=", hasil)

def sin_bil(bil):
    import math
    hasil = math.sin(math.radians(bil))
    print("Sinus dari", bil, "derajat =", hasil)

def cos_bil(bil):
    import math
    hasil = math.cos(math.radians(bil))
    print("Kosinus dari", bil, "derajat =", hasil)

def tan_bil(bil):
    import math
    hasil = math.tan(math.radians(bil))
    print("Tangen dari", bil, "derajat =", hasil)

    
