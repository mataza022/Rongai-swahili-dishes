import os
import shutil

downloads = os.path.expanduser("~/Downloads")
project_dir = os.getcwd()

# Find recent images in Downloads
images = [f for f in os.listdir(downloads) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
images.sort(key=lambda x: os.path.getmtime(os.path.join(downloads, x)), reverse=True)

print("\n--- Here are your most recent images in Downloads ---")
for i, img in enumerate(images[:25]):
    print(f"[{i+1}] {img}")

targets = {
    "achari.jpg": "Image 1 (Yellow snack in cups)",
    "smocha.jpg": "Image 2 (Chapati wrap)",
    "smokies.jpg": "Image 3 (Sausage)",
    "mbaazi.jpg": "Image 4 (Pigeon peas)",
    "beans.jpg": "Image 5 (Bean stew)",
    "chapati.jpg": "Image 6 (Chapatis)",
    "sugarcanejuice.jpg": "Image 7 (Sugarcane juice)",
    "ukwajujuice.jpg": "Image 8 (Tamarind juice)",
    "pineapplejuice.jpg": "Image 9 (Pineapple juice)",
    "chipsmasala.jpg": "Image 10 (Chips masala)",
    "ugalibeef.jpg": "Image 11 (Ugali & beef)",
    "whitericebeef.jpg": "Image 12 (White rice & beef)"
}

print("\n--- Let's map them to your website ---")
for target, desc in targets.items():
    while True:
        try:
            choice = input(f"\n{desc}\nType the number from the list above: ")
            idx = int(choice) - 1
            if 0 <= idx < len(images):
                src = os.path.join(downloads, images[idx])
                dst = os.path.join(project_dir, target)
                shutil.copy(src, dst)
                print(f"✅ Copied and renamed to {target}")
                break
            else:
                print("❌ Invalid number. Try again.")
        except ValueError:
            print("❌ Please type a number.")

print("\n🎉 All images successfully copied and renamed!")
