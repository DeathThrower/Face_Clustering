# Face_Clustering
program to cluster and divide folder/s of persons based on the face using the pretrained deep learning network Keras Facenet to get the face embedding, clusteval to get the best K used in Kmeans and sklearn Kmeans to cluster the persons according to the face embeddings 
## Setup
run the "setup.py" file to install the required packages
>python -u setup.py
## Models 

### Keras Facenet

The DL model resposible for getting the face embedding of the Image

### clusteval

The ML model resposible for getting the optimal K requires for Kmean Clustering 

### sklearn Kmeans

The ML model resposible for Clusering the faces according to thier embedding 

## How to use it
first you clone the repo
> git clone https://github.com/DeathThrower/Image_Clustering

then navigate to the Image_Clustering folder
> cd Image_Clustering

then run the setup
> python -u setup.py

then run the main.py
> python -u main.py
