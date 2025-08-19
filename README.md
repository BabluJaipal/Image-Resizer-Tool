# 🖼️ Image Resizer Tool

A simple Python tool to **resize and convert images** in **batch mode** (entire folder) or **single image mode**.  
Built using **Python** and **Pillow (PIL fork)**.  

---

## 🚀 Features
- ✅ Resize **all images in a folder** at once (batch mode).  
- ✅ Resize a **single image manually** (single image mode).  
- ✅ Choose custom **width** and **height**.  
- ✅ Save in different formats: `JPEG`, `PNG`, `WEBP`, etc.  
- ✅ Automatically creates an output folder for resized images.  
- ✅ Uses **LANCZOS resampling** for high-quality resizing.  

---

## 📦 Requirements
- Python 3.x  
- Pillow (Python Imaging Library)  

Install Pillow with:
#pip install pillow

Image-Resizer-Tool/
│── image_resizer.py   # Main script
│── input_images/      # Put your original images here (for batch mode)
│── output_images/     # Resized images will be saved here (batch mode)
│── output_single/     # Resized single image will be saved here
│── README.md          # Documentation


Run the script:

python image_resizer.py


You will see a menu:

Choose Mode:
1. Resize all images in a folder
2. Resize a single image
Enter choice (1/2):

🔹 Example 1: Resize all images in a folder

Put all your images inside input_images/.

Run the script and choose 1.

Enter width, height, and format.

Resized images will be saved in output_images/.

🔹 Example 2: Resize a single image

Run the script and choose 2.

Enter full path of the image (e.g., C:/Users/Name/Desktop/photo.jpg).

Enter width, height, and format.

Resized image will be saved in output_single/.


📌 Notes

If output folders (output_images / output_single) do not exist, they will be created automatically.

Supported formats: JPEG, PNG, WEBP, BMP, TIFF.

The script currently stretches images to fit width & height.
(Optional improvement: keep aspect ratio to avoid stretching).

🤝 Contributing
Feel free to fork this project, open issues, or submit PRs for improvements (like adding GUI, drag-and-drop support, or maintaining aspect ratio).
