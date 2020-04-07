import numpy as np
import pyexcel
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

# 读取文件中每个研究对象的抑郁分数、词典命中数两项数据
depression_scores_sheet = pyexcel.get_sheet(file_name='depression_scores.csv')
word_hit_sheet = pyexcel.get_sheet(file_name='word_hit_count.csv')
depression_scores = []
word_hit = []
for row in depression_scores_sheet:
    depression_scores.append(row[1])
for row in word_hit_sheet:
    word_hit.append(row[1])
print('Depression Scores: ', depression_scores)
print('Word Hit Counts: ', word_hit)

depression_score_arr = np.array(depression_scores)
word_hit_arr = np.array(word_hit)
# plt.figure()
# plt.axis([0, 1500, -1, 1])
# plt.grid(True)
# plt.plot(word_hit_arr, depression_score_arr, 'k.')
# plt.show()

# 定义随机选择的 K 值范围
data = np.vstack((word_hit_arr, depression_score_arr)).T
# print(data)
# K = range(1, 9)
# distortions = []
# for k in K:
#     kmeans = KMeans(n_clusters=k, n_init=10)
#     kmeans.fit(data)
#     distortions.append(sum(np.min(cdist(data, kmeans.cluster_centers_, 'euclidean'), axis=1)) / data.shape[0])
# plt.plot(K, distortions, 'bx-')
# plt.xlabel('k')
# plt.show()

plt.figure(figsize=(8, 10))
plt.axis([0, 1500, -1, 1])
plt.grid(True)
colors = ['r', 'c']
markers = ['o', 'v']
kmeans_model = KMeans(n_clusters=2).fit(data)
for i, j in enumerate(kmeans_model.labels_):
    plt.plot(word_hit_arr[i], depression_score_arr[i], color=colors[j], marker=markers[j], ls='None')
plt.show()
