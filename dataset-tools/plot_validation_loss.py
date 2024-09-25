import pandas as pd
import matplotlib.pyplot as plt

# Ensure that matplotlib uses LaTeX fonts
#plt.rcParams.update({
#    "text.usetex": True,               # Use LaTeX for text rendering
#    "font.family": "serif",            # Use serif fonts in plots
#    "font.serif": ["Palatino"],        # Set Palatino as the font for text
#    "axes.labelsize": 12,              # Label size
#    "font.size": 12                    # General font size
#})
plt.rcParams.update({
    "text.usetex": True,               # Use LaTeX for text rendering
    "font.family": "serif",            # Use serif fonts in plots
    "font.serif": ["Latin Modern"],    # Set Latin Modern as the font for text
    "axes.labelsize": 12,              # Label size
    "font.size": 12                    # General font size
})

# Load the CSV files into DataFrames for each model
csv_file_unet = "best_model_unet_multiclass_merged30e.csv"      # UNet
csv_file_fpn = "best_model_FPN_multiclass_merged30e.csv"        # FPN
csv_file_pspnet = "best_model_pspnet_multiclass_merged30e.csv"  # PSPNet
csv_file_deeplab = "best_model_deeplabv3_multiclass_merged30e.csv" # DeepLab

df_unet = pd.read_csv(csv_file_unet)
df_fpn = pd.read_csv(csv_file_fpn)
df_pspnet = pd.read_csv(csv_file_pspnet)
df_deeplab = pd.read_csv(csv_file_deeplab)

# Create the plot
plt.figure(figsize=(8, 5))

# Plot Validation loss for each model with different colors
plt.plot(df_unet['Epoch'], df_unet['Val_Loss'], label='UNet', color='blue')
plt.plot(df_fpn['Epoch'], df_fpn['Val_Loss'], label='FPN', color='green')
plt.plot(df_pspnet['Epoch'], df_pspnet['Val_Loss'], label='PSPNet', color='red')
plt.plot(df_deeplab['Epoch'], df_deeplab['Val_Loss'], label='DeepLabV3+', color='purple')

# Set plot labels and title with LaTeX formatting
plt.xlabel(r'\textbf{Epochs}')
plt.ylabel(r'\textbf{Validation Loss}')
#plt.title(r'\textbf{Validation Loss Over Epochs for Different Models}')

# Show grid, legend, and save the plot
plt.grid(True)
plt.legend(loc='best')

# Save the figure as a PNG or PDF to include in the LaTeX document
plt.savefig('validation_loss_plot.png', dpi=300, bbox_inches='tight')  # PNG format
# plt.savefig('Validation_loss_plot.pdf', bbox_inches='tight')  # PDF format

# Display the plot
plt.show()