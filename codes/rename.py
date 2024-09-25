import os

def rename_files(folder_path, start_number, end_number):
    if not os.path.exists(folder_path):
        print("Klasör bulunamadı.")
        return

    file_list = os.listdir(folder_path)
    
    for i, filename in enumerate(file_list, start=start_number):
        if i > end_number:
            break
        
        file_extension = os.path.splitext(filename)[1]
        new_filename = f"{i:01d}{file_extension}"  # Örneğin: 001.jpg, 002.png vb.
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"{filename} --> {new_filename}")

folder_path = r"pathadresi" # İlgili klasörün yolunu buraya girin
start_number =  1  # Başlangıç sayısı
end_number =  20  # Bitiş sayısı (bu sayıya kadar olan dosyalar yeniden adlandırılacak)

rename_files(folder_path, start_number, end_number)
