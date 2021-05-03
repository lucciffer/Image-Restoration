# Image-Restoration  
Various techniques, including image inpainting, super resolution, denoising, etc are ways of restoring/conserving an old image or photograph.  
In this repository we shall look into some inpainting and super resolution techniques of restoring old photos.  

## Requirements/dependencies:  
- Python 3.x
- OpenCV
- [Matplotlib](https://pypi.org/project/matplotlib/)

All of them can be installed via `conda` or `pip` e.g.  
```
conda install matplotlib  
```  
or   
```
pip install matplotlib
```  
## Usage
###  Image Inpainting using OpenCV:  
First run the `mask_generator.py` to generate a mask for the given input image.  
Then to inpaint the image with the generated mask, run the `inpainting-using-opencv.py` by passing arguements. e.g.  
```
python inpainting-using-opencv.py --image [path to the image] --mask [path to the mask of the input image]  --method ['ns' or 'telea']
```
