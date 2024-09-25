from PIL import Image
import os

def resize_images(input_folder, output_folder):
    # Eğer çıkış klasörü yoksa oluştur
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Giriş klasöründeki tüm dosyaları al
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Sadece resim dosyalarını işle
        if os.path.isfile(input_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Resmi aç
                img = Image.open(input_path)

                # Resmi 640x480 boyutuna resize et
                img = img.resize((640, 480))

                # Resmi kaydet
                img.save(output_path)
            except Exception as e:
                print(f"Hata: {e}")
        else:
            print(f"{file_name} resim dosyası değil, işlenmeyecek.")

if __name__ == "__main__":
    input_folder = "ınputpath"
    output_folder = "outputpath"

    resize_images(input_folder, output_folder)
