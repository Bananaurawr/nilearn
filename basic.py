from nilearn.datasets import MNI152_FILE_PATH

# Looking at our data
from nilearn import plotting
plotting.plot_img(MNI152_FILE_PATH,title="MNI152 template", output_file="mni152_plot.png")

# Simple image manipulation: Smoothing
from nilearn import image

smooth_anat_img = image.smooth_img(MNI152_FILE_PATH, fwhm=3)

# While we are giving a file name as input, the function returns
# an in-memory object:
smooth_anat_img