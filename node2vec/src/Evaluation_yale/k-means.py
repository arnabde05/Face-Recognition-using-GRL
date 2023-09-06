import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


# Load flattened embeddings
train_path = "F:\\Face_recognition\\graph neural network\\code\\node2vec\\node2vec\\flattened_all"

# read the embeddings for train and test images and store their respective IDs
train_embeddings = []
train_ids = []
for filename in os.listdir(train_path):
    if filename.endswith(".emb"):
        emb_path = os.path.join(train_path, filename)
        train_embeddings.append(np.loadtxt(emb_path))
        train_id = filename.split("_")[0]
        train_ids.append(train_id)
train_embeddings = np.array(train_embeddings)

# Apply k-means clustering
kmeans = KMeans(n_clusters=10, random_state=0).fit(train_embeddings)
predicted_labels = kmeans.labels_

# Print the cluster labels
print(predicted_labels)

true_labels = {
              "01_centerlight_flattened.emb": "1",
              "01_glasses_flattened.emb": "1",
              "01_happy_flattened.emb": "1",
              "01_leftlight_flattened.emb": "1",
              "01_noglasses_flattened.emb": "1",
              "01_normal_flattened.emb": "1",
              "01_rightlight_flattened.emb": "1",
              "01_sad_flattened.emb": "1",
              "01_sleepy_flattened.emb": "1",
              "01_surprised_flattened.emb": "1",
              "01_wink_flattened.emb": "1",
              "02_centerlight_flattened.emb": "2",
              "02_glasses_flattened.emb": "2",
              "02_happy_flattened.emb": "2",
              "02_leftlight_flattened.emb": "2",
              "02_noglasses_flattened.emb": "2",
              "02_normal_flattened.emb": "2",
              "02_rightlight_flattened.emb": "2",
              "02_sad_flattened.emb": "2",
              "02_sleepy_flattened.emb": "2",
              "02_surprised_flattened.emb": "2",
              "02_wink_flattened.emb": "2",
              "03_centerlight_flattened.emb": "3",
              "03_glasses_flattened.emb": "3",
              "03_happy_flattened.emb": "3",
              "03_leftlight_flattened.emb": "3",
              "03_noglasses_flattened.emb": "3",
              "03_normal_flattened.emb": "3",
              "03_rightlight_flattened.emb": "3",
              "03_sad_flattened.emb": "3",
              "03_sleepy_flattened.emb": "3",
              "03_surprised_flattened.emb": "3",
              "03_wink_flattened.emb": "3",
              "04_centerlight_flattened.emb": "4",
              "04_glasses_flattened.emb": "4",
              "04_happy_flattened.emb": "4",
              "04_leftlight_flattened.emb": "4",
              "04_noglasses_flattened.emb": "4",
              "04_normal_flattened.emb": "4",
              "04_rightlight_flattened.emb": "4",
              "04_sad_flattened.emb": "4",
              "04_sleepy_flattened.emb": "4",
              "04_surprised_flattened.emb": "4",
              "04_wink_flattened.emb": "4",
              "05_centerlight_flattened.emb": "5",
              "05_glasses_flattened.emb": "5",
              "05_happy_flattened.emb": "5",
              "05_leftlight_flattened.emb": "5",
              "05_noglasses_flattened.emb": "5",
              "05_normal_flattened.emb": "5",
              "05_rightlight_flattened.emb": "5",
              "05_sad_flattened.emb": "5",
              "05_sleepy_flattened.emb": "5",
              "05_surprised_flattened.emb": "5",
              "05_wink_flattened.emb": "5",
              "06_centerlight_flattened.emb": "6",
              "06_glasses_flattened.emb": "6",
              "06_happy_flattened.emb": "6",
              "06_leftlight_flattened.emb": "6",
              "06_noglasses_flattened.emb": "6",
              "06_normal_flattened.emb": "6",
              "06_rightlight_flattened.emb": "6",
              "06_sad_flattened.emb": "6",
              "06_sleepy_flattened.emb": "6",
              "06_surprised_flattened.emb": "6",
              "06_wink_flattened.emb": "6",
              "07_centerlight_flattened.emb": "7",
              "07_glasses_flattened.emb": "7",
              "07_happy_flattened.emb": "7",
              "07_leftlight_flattened.emb": "7",
              "07_noglasses_flattened.emb": "7",
              "07_normal_flattened.emb": "7",
              "07_rightlight_flattened.emb": "7",
              "07_sad_flattened.emb": "7",
              "07_sleepy_flattened.emb": "7",
              "07_surprised_flattened.emb": "7",
              "07_wink_flattened.emb": "7",
              "08_centerlight_flattened.emb": "8",
              "08_glasses_flattened.emb": "8",
              "08_happy_flattened.emb": "8",
              "08_leftlight_flattened.emb": "8",
              "08_noglasses_flattened.emb": "8",
              "08_normal_flattened.emb": "8",
              "08_rightlight_flattened.emb": "8",
              "08_sad_flattened.emb": "8",
              "08_sleepy_flattened.emb": "8",
              "08_surprised_flattened.emb": "8",
              "08_wink_flattened.emb": "8",
              "09_centerlight_flattened.emb": "9",
              "09_glasses_flattened.emb": "9",
              "09_happy_flattened.emb": "9",
              "09_leftlight_flattened.emb": "9",
              "09_noglasses_flattened.emb": "9",
              "09_normal_flattened.emb": "9",
              "09_rightlight_flattened.emb": "9",
              "09_sad_flattened.emb": "9",
              "09_sleepy_flattened.emb": "9",
              "09_surprised_flattened.emb": "9",
              "09_wink_flattened.emb": "9",
              "10_centerlight_flattened.emb": "10",
              "10_glasses_flattened.emb": "10",
              "10_happy_flattened.emb": "10",
              "10_leftlight_flattened.emb": "10",
              "10_noglasses_flattened.emb": "10",
              "10_normal_flattened.emb": "10",
              "10_rightlight_flattened.emb": "10",
              "10_sad_flattened.emb": "10",
              "10_sleepy_flattened.emb": "10",
              "10_surprised_flattened.emb": "10",
              "10_wink_flattened.emb": "10",
              "11_centerlight_flattened.emb": "11",
              "11_glasses_flattened.emb": "11",
              "11_happy_flattened.emb": "11",
              "11_leftlight_flattened.emb": "11",
              "11_noglasses_flattened.emb": "11",
              "11_normal_flattened.emb": "11",
              "11_rightlight_flattened.emb": "11",
              "11_sad_flattened.emb": "11",
              "11_sleepy_flattened.emb": "11",
              "11_surprised_flattened.emb": "11",
              "11_wink_flattened.emb": "11",
              "12_centerlight_flattened.emb": "12",
              "12_glasses_flattened.emb": "12",
              "12_happy_flattened.emb": "12",
              "12_leftlight_flattened.emb": "12",
              "12_noglasses_flattened.emb": "12",
              "12_normal_flattened.emb": "12",
              "12_rightlight_flattened.emb": "12",
              "12_sad_flattened.emb": "12",
              "12_sleepy_flattened.emb": "12",
              "12_surprised_flattened.emb": "12",
              "12_wink_flattened.emb": "12",
              "13_centerlight_flattened.emb": "13",
              "13_glasses_flattened.emb": "13",
              "13_happy_flattened.emb": "13",
              "13_leftlight_flattened.emb": "13",
              "13_noglasses_flattened.emb": "13",
              "13_normal_flattened.emb": "13",
              "13_rightlight_flattened.emb": "13",
              "13_sad_flattened.emb": "13",
              "13_sleepy_flattened.emb": "13",
              "13_surprised_flattened.emb": "13",
              "13_wink_flattened.emb": "13",
              "14_centerlight_flattened.emb": "14",
              "14_glasses_flattened.emb": "14",
              "14_happy_flattened.emb": "14",
              "14_leftlight_flattened.emb": "14",
              "14_noglasses_flattened.emb": "14",
              "14_normal_flattened.emb": "14",
              "14_rightlight_flattened.emb": "14",
              "14_sad_flattened.emb": "14",
              "14_sleepy_flattened.emb": "14",
              "14_surprised_flattened.emb": "14",
              "14_wink_flattened.emb": "14",
              "15_centerlight_flattened.emb": "15",
              "15_glasses_flattened.emb": "15",
              "15_happy_flattened.emb": "15",
              "15_leftlight_flattened.emb": "15",
              "15_noglasses_flattened.emb": "15",
              "15_normal_flattened.emb": "15",
              "15_rightlight_flattened.emb": "15",
              "15_sad_flattened.emb": "15",
              "15_sleepy_flattened.emb": "15",
              "15_surprised_flattened.emb": "15",
              "15_wink_flattened.emb": "15"}

true_labels = np.array(list(true_labels.values()), dtype=int)

accuracy = accuracy_score(true_labels, predicted_labels)
print ("Accuracy: ", accuracy)


cm = confusion_matrix(true_labels, predicted_labels)

sns.heatmap(cm)

plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')

# show plot
plt.show()