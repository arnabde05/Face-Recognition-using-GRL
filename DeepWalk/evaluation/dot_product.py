import os
import numpy as np

train_folder_path = r"F:\Face_recognition\graph neural network\code\deepwalk\deepwalk\emb\train\90"
test_folder_path = r"F:\Face_recognition\graph neural network\code\deepwalk\deepwalk\emb\test\75"

def load_embeddings(folder_path):
    embeddings = []
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                embedding = np.fromfile(file, sep=' ')
                embedding = embedding[1:]
                # print(embedding)
                embeddings.append(embedding)
    return embeddings


def calculate_accuracy(test_embeddings, train_embeddings, threshold):
    correct_matches = 0
    total_tests = len(test_embeddings)

    for i, test_embedding in enumerate(test_embeddings):
        similarity_scores = np.dot(test_embedding, np.array(train_embeddings).T)
        max_similarity = np.max(similarity_scores)
        if max_similarity >= threshold:
            train_image_index = np.argmax(similarity_scores)
            print(f"Dot product similarity for test image {i+1} (subject {i+13}):")
            print(f"Best match is with train image {train_image_index+1} (subject {train_image_index+13}), with dot product similarity of {max_similarity:.4f}")
            print()

            correct_matches += 1

    accuracy = (correct_matches / total_tests) * 100
    return accuracy


# Load embeddings from train and test folders
train_embeddings = load_embeddings(train_folder_path)
test_embeddings = load_embeddings(test_folder_path)

# Set the threshold for dot product similarity
threshold = 7

# Calculate accuracy and print dot product similarity details
accuracy = calculate_accuracy(test_embeddings, train_embeddings, threshold)

print(f"Accuracy: {accuracy:.2f}%")
