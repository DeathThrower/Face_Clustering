from sklearn.cluster import KMeans
from clusteval import clusteval
from keras_facenet import FaceNet
import os
import shutil
import numpy as np 

def load_emb_faces(dir, face_threshold = 0.85):
    emb_faces = list()
    paths = list()
    # enumerate files
    for filename in os.listdir(dir):
        path = dir + '/' + filename
        # if there is a face
        try:
            # get the embedding of the face
            emb_face = FaceNet().extract(path, threshold=face_threshold,)[0]['embedding']
            emb_faces.append(emb_face)
            paths.append(path)
        except :
            pass
    print("-----------------------------------------------------------------------------------------------------",len(emb_faces))
    return emb_faces,paths

def cluster(emb_faces, n_clusters = -1):
    if(len(emb_faces)==0):
        return []
    # Set parameters, as an example dbscan
    ce = clusteval(verbose=False)

    # Fit to find optimal number of clusters using dbscan
    results= ce.fit(emb_faces)

    # getting the optimal number of clusters
    index = np.argsort(list(results['score']['score']))[-1] # np.argmax(results['score']['score'])
    n = int(results['score'].iloc[index]['clusters'])

    n_clusters = n if n_clusters == -1 else n_clusters
    # clustering using KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(emb_faces)

    labels = np.array(kmeans.labels_)
    return labels

def classify_1folder(datapath, face_threshold = 0.9):
    emb_faces, paths = load_emb_faces(datapath,face_threshold)
    labels = cluster(np.array(emb_faces))
    return labels,np.array(paths)
def classify_Folders(dirs, face_threshold = 0.9):
    emb_faces, paths = list(), list()
    for dir in dirs:
        emb_faces_, paths_ = load_emb_faces(dir,face_threshold)
        emb_faces = emb_faces + emb_faces_ 
        paths = paths + paths_
    labels = cluster(np.array(emb_faces))
    return labels,np.array(paths)

def get_my_images(Bdir,Tdir, face_threshold = 0.85, sim_threshold = 0.5, p_threshold = 0.6):
    n = 0
    # get the paths of the target folder images
    paths = np.array([Tdir + '/' + filename for filename in os.listdir(Tdir)])
    # get the embedding of the base folder images
    base = [FaceNet().extract(Bdir + '/' + filename , threshold= face_threshold)[0]['embedding'] for filename in os.listdir(Bdir)]
    # for every image in the target folder
    for path in paths:
        # get the embedding of the image
        embedding = FaceNet().extract(path, threshold=face_threshold)[0]['embedding']
        # find the percentage of similar images in the base folder images
        p = np.sum(np.array([FaceNet().compute_distance(embedding,b) for b in base]) < sim_threshold) / len(base)
        # if the percentage is bigger than 0.3 move the image
        if (p>=p_threshold):
            shutil.move(path, Bdir)
            n+=1
    return n