# About Repository
This is just a documentation of me learning about Neuro-AI. The projects added in this repository are all documentations of things I learn so it will be a tad bit messy. However I will keep everything updated as best as I could since I use colab for the ipynb

## Projects
### 1. Cerebramorphic: fMRI Representation Encoder
The encoder we built allows researchers to more clearly understand the results of fMRI by inputing the raw fMRI beta estimates from BOLD Moments datasets (which are roughly 27000 voxels). The denoiser will remove scanner artefacts while preserving memory encoding signal. Then the contrastive encoder compresses to 256-dim vector — similar content maps to nearby points which outputs the temporal resonance map: encoding strength per second + memorability decay prediction

### 2. Emotional Synchrony using (In progress)
The goal of this project is to build a tool that maps the "Portrayed Emotion" of a character (ground truth from the dataset) against the "Brain Response" of the viewers to see if the viewers' brains actually "felt" what the character was "portraying." Here we use Intersubject Correlation or ISC to measure this "shared experience" between each person.
