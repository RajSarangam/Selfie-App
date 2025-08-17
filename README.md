# Selfie-App
Image &amp; Video effects with OpenCV — Instagram-style filters, blemish removal, and green screen compositing built from scratch.

# 🎨 Fundamentals of Computer Vision — Image & Video Effects  

**Image & video effects with OpenCV — Instagram-style filters, blemish removal, and green screen compositing built from scratch.**

---

## 📌 Executive Summary  
This project showcases **three computer vision applications** built from scratch using **OpenCV & NumPy**:  
1. **Instagram Filters** – Pencil Sketch & Cartoon effects via edge detection, smoothing, and color quantization.  
2. **Blemish Removal** – Interactive skin retouching using patch matching, seamless cloning, and inpainting.  
3. **Chroma Keying** – Green screen matting with adjustable tolerance, softness, and spill removal for realistic background replacement.  

🔑 Demonstrates practical CV skills in **image processing, patch-based editing, and video compositing**.  

---

## 📂 Project Parts  

### **Part 1 — Instagram Filters**  
Recreate two classic Instagram-style filters:  
- **Pencil Sketch**: Converts an image into a grayscale sketch by detecting edges and blending with inverted blurred images.  
- **Cartoon Effect**: Simplifies colors with bilateral filtering & quantization, then overlays bold outlines for a comic-book look.  

🔑 **Concepts**: edge detection, smoothing, quantization, blending.  

---

### **Part 2 — Blemish Removal**  
An interactive tool for skin retouching:  
- User clicks on a blemish → tool finds the best nearby patch (similar texture & lighting).  
- The patch is blended seamlessly over the blemish using Poisson blending or inpainting.  

🔑 **Concepts**: patch matching, SSD/Laplacian scoring, seamless cloning, inpainting.  

---

### **Part 3 — Chroma Keying (Green Screen Matting)**  
Replace a solid green (or blue) background with an arbitrary image/video.  
- User samples a patch of the background color.  
- Adjustable sliders for **tolerance**, **softness**, and **color spill removal** refine the mask.  
- Output is a composite of the subject and new background.  

🔑 **Concepts**: color space modeling, alpha matte generation, feathering, compositing.  

---

## 🚀 Highlights  
- Built entirely with **OpenCV + NumPy**  
- Real-time interactive UI with **HighGUI** controls  
- Extensible: you can plug in new filters, patch-based effects, or background matting techniques  

---

## ▶️ Usage  

Each part is self-contained.  

```bash
# Part 1 - Instagram Filters
python part1-instagram-filters/pencil_sketch.py --image examples/input.jpg --output output_sketch.jpg
python part1-instagram-filters/cartoon_filter.py --image examples/input.jpg --output output_cartoon.jpg

# Part 2 - Blemish Removal
python part2-blemish-removal/blemish_removal.py --image examples/face.jpg

# Part 3 - Chroma Keying
python part3-chroma-keying/chroma_key.py --video examples/greenscreen.mp4 --bg-img examples/bg.jpg --out output.mp4
