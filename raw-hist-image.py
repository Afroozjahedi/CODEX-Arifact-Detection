import matplotlib.pyplot as plt
import os

base_path = "/Users/ajahedi/OneDrive - Inside MD Anderson/CODEX Resources & Papers/qc folder/Stitching/Raw_tissue plots/IWP5Reg01/no/"


all_files = os.listdir(base_path)
png_files = [f for f in all_files if f.endswith('.png')]

intensities = []

for image_filename in png_files:
    full_image_path = os.path.join(base_path, image_filename)
    image = plt.imread(full_image_path)
    image = image[:, :, :3].mean(axis=2)  # Convert to grayscale
    intensities.extend(image.ravel())

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(intensities, bins=50, color='gray', alpha=0.7)
plt.title('Histogram of Intensities')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
