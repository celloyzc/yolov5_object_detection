import os
import shutil

def eslestir_ve_kaydet(foto_klasor, txt_klasor, hedef_klasor):
    foto_listesi = os.listdir(foto_klasor)
    txt_listesi = os.listdir(txt_klasor)

    for foto_ad in foto_listesi:
        foto_ad_uzantısız = os.path.splitext(foto_ad)[0]

        for txt_ad in txt_listesi:
            txt_ad_uzantısız = os.path.splitext(txt_ad)[0]

            if foto_ad_uzantısız == txt_ad_uzantısız:
                foto_yolu = os.path.join(foto_klasor, foto_ad)
                txt_yolu = os.path.join(txt_klasor, txt_ad)

                # Eşleşen dosyaları hedef klasöre taşıyalım
                hedef_foto_yolu = os.path.join(hedef_klasor, foto_ad)
                hedef_txt_yolu = os.path.join(hedef_klasor, txt_ad)

                shutil.copy(foto_yolu, hedef_foto_yolu)
                shutil.copy(txt_yolu, hedef_txt_yolu)

                break  # İlk eşleşmeyi bulduğumuzda diğer txt dosyalarını kontrol etmeye gerek yok


if __name__ == "__main__":
    foto_klasor = r"D:\datset\bee\train\image"
    txt_klasor = r"D:\datset\bee\train\label"
    hedef_klasor = r"D:\datset\bee\train\hedef"

    # Hedef klasörü oluştur
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)

    eslestir_ve_kaydet(foto_klasor, txt_klasor, hedef_klasor)
