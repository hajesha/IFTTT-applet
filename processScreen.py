import numpy as np
import cv2
import time
from sklearn.cluster import MiniBatchKMeans


def get_colors(hist, centroids):
    show_color = None

    for (percent, color) in zip(hist, centroids):
        show_color = color.astype("uint8").tolist()

    return show_color


def centroid_histogram(clt):
    num_labels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=num_labels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


frame = cv2.imread("test.jpg")
start = time.perf_counter()
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
image = image.reshape((image.shape[0] * image.shape[1], 3))

clt = MiniBatchKMeans(n_clusters=1, max_iter=10, n_init=1)
clt.fit(image)
hist = centroid_histogram(clt)
color = get_colors(hist, clt.cluster_centers_)
end = time.perf_counter()
print(color)
print(f"Took {end - start:0.4f} seconds")