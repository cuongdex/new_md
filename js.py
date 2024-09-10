import os
import json
from PIL import Image

# Đường dẫn tới thư mục chứa ảnh
image_dir = './images'
output_json = './captions.json'

# Thay đổi các thông tin này theo dữ liệu của bạn
info = {
    "description": "Dataset description",
    "version": "1.0",
    "year": 2024
}

licenses = [
    {
        "id": 1,
        "name": "License name",
        "url": "http://license.url"
    }
]

categories = [
    {
        "id": 1,
        "name": "category_name",
        "supercategory": "supercategory_name"
    }
]

images = []
annotations = []

image_id = 1
annotation_id = 1

# Ví dụ mô tả ảnh
descriptions = {
    "000000000001.jpg": "A description of the image 000000000001.jpg",
    # Thêm mô tả cho các ảnh khác nếu cần
}

for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_dir, filename)
        with Image.open(image_path) as img:
            width, height = img.size

        images.append({
            "id": image_id,
            "file_name": filename,
            "height": height,
            "width": width,
            "description": descriptions.get(filename, "mo ta")  # Thêm mô tả nếu có
        })

        # Thêm thông tin annotation (cần thay đổi tùy thuộc vào dữ liệu thực tế của bạn)
        annotations.append({
            "id": annotation_id,
            "image_id": image_id,
            "category_id": 1,  # Cần thay đổi theo danh sách categories của bạn
            "bbox": [50, 50, 100, 150],  # Cần thay đổi tọa độ thực tế
            "area": 15000,  # Tính diện tích nếu cần
            "iscrowd": 0,
            "caption": descriptions.get(filename, "mo ta")  # Thêm mô tả nếu có
        })
        annotation_id += 1
        image_id += 1

# Tạo cấu trúc JSON cuối cùng
dataset = {
    "info": info,
    "licenses": licenses,
    "images": images,
    "annotations": annotations,
    "categories": categories
}

# Ghi dữ liệu JSON ra file
with open(output_json, 'w') as f:
    json.dump(dataset, f, indent=4)

print(f"JSON file created: {output_json}")
