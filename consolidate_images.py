import os
import shutil

def consolidate_images(root_dir):
    categories = ['Anime', 'Cartoon']

    for category in categories:
        category_path = os.path.join(root_dir, category)
        target_dir = os.path.join(root_dir, category)

        file_count = 1

        for subfolder in os.listdir(category_path):
            subfolder_path = os.path.join(category_path, subfolder)

            if os.path.isdir(subfolder_path):
                for file_name in os.listdir(subfolder_path):
                    if file_name.endswith('.png'):
                        new_file_name = f"{file_count}.png"
                        new_file_path = os.path.join(target_dir, new_file_name)

                        shutil.move(os.path.join(subfolder_path, file_name), new_file_path)

                        file_count += 1

                shutil.rmtree(subfolder_path)

    print("Consolidation completed!")

root_data_dir = 'data'

consolidate_images(root_data_dir)
