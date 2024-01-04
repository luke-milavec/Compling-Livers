# Compling-Livers
### This model was created with data provided by Lord Lab at Pitt, based off [pix2pix](https://www.tensorflow.org/tutorials/generative/pix2pix) and [Aladdin Persson's recreation of pix2pix](https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/GANs/Pix2Pix)

The model uses images of GATA6 proteins in developing liver cells to predict the resulting vascular structure of the fully developed liver cells. This is based off the labs [previous research](https://www.nature.com/articles/ncomms10243).

# Usage
1. Download raw data via Lord Lab (Closed source)
2. Run format_data.py
3. Create evaluation folder for results
4. Run train.py

# Retrospective 1/4/2024
I started this project with no prior experience in ML and was tasked with creating a model that could predict the vascular structure better than pix2pix. I, expectedly, into a lot of issues with overfitting given the data set was 39 points. The semester, and thus the project, ended before many of these were ironed out. I regret not pushing the timeline on the first prototype but, I hope to revisit a similar project soon.

