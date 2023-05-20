from Models import *

print("if you want to cluster many folders")
print("First make a folder of them then entre 1")
print("if you want to cluster 1 folder")
print("entre 2")
print("if you want to move images from folder to another folder according to face similarity")
print("entre 3")
n = input("Entre your choice: ")
if n == "1":
    # get the dataset folder of folders of images
    print("Entre the path of the dataset you want to cluster")
    base = input()
    print("Entre the path of the folder you want to save the clusters")
    base_output = input()
    
    # get the dataset folder of folders of images
    base = ''
    # get all the names of the folders in the dataset
    dirs = [x[0] for x in os.walk(base)][1:]
    # specify the output folder and create it if its not exsit
    base_output = 'Output_Dataset/'
    if not os.path.exists(base_output):
        os.makedirs(base_output)
    # specify the number of folders that the model will cluster each time
    step = 3
    max_label = 0
    for i in range(0,len(dirs),step):
        # get the directories of the folders and pass it to the model
        folders = dirs[i:i+step]
        # get the paths of the image and labels of these images from the model
        labels,paths = classify_Folders(folders)
        # move each class of the 
        for label in np.unique(labels):
            dir = base_output + str(max_label+label)
            os.mkdir(dir)
            for path in paths[labels == label]:
                shutil.copy(path, dir)
        max_label += len(np.unique(labels))
        
elif n == "2":
    print("Entre the path of the folder you want to cluster")
    base = input()
    print("Entre the path of the folder you want to save the clusters")
    base_output = input()
    labels,paths = classify_1folder(base)
    for label in np.unique(labels):
        dir = base_output + str(label)
        os.mkdir(dir)
        for path in paths[labels == label]:
            shutil.copy(path, dir)

elif n == "3":
    print("Entre the path of the Base Folder")
    Bdir = input()
    print("Entre the path of the Target Folder")
    Tdir = input()
    print("The number of images moved from target to base is", get_my_images(Bdir,Tdir))