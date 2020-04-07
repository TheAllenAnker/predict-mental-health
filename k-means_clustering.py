import numpy as np
import pyexcel
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
from pyecharts.charts import Scatter
from pyecharts import options as opts

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
# for i, j in enumerate(kmeans_model.labels_):
#     plt.plot(word_hit_arr[i], depression_score_arr[i], color=colors[j], marker=markers[j], ls='None')
# plt.show()

print(data)
# 分别将K-means分类结果存入两个数组中
cluster1 = []
cluster2 = []
for i, cluster in enumerate(kmeans_model.labels_):
    if cluster == 1:
        cluster2.append(data[i])
    else:
        cluster1.append(data[i])

print('Cluster 1: ', cluster1)
print('Cluster 2: ', cluster2)
x_data1, x_data2 = [], []
y_data1, y_data2 = [], []
for i in range(len(cluster1)):
    x_data1.append(cluster1[i][0])
    y_data1.append(cluster1[i][1])
for i in range(len(cluster2)):
    x_data2.append(cluster2[i][0])
    y_data2.append(cluster2[i][1])
print(x_data1, y_data1)
print(x_data2, y_data2)
group1_arr, group2_arr = [], []
for i in range(len(x_data1)):
    group1_arr.append([x_data1[i], y_data1[i]])
for i in range(len(x_data2)):
    group2_arr.append([x_data2[i], y_data2[i]])
print(group1_arr)
print(group2_arr)
# 使用 pyecharts 进行可视化
fig_size = opts.InitOpts(width='800px', height='600px')
scatter = Scatter(init_opts=fig_size)
# scatter.add_xaxis(xaxis_data=x_data1)
# scatter.add_yaxis(series_name='聚类 1',
#                   y_axis=y_data1,
#                   color='red',
#                   label_opts=opts.LabelOpts(is_show=False),
#                   symbol='circle')
# scatter.add_yaxis(series_name='聚类 2',
#                   y_axis=y_data2,
#                   label_opts=opts.LabelOpts(is_show=True),
#                   symbol_size=15,
#                   symbol='triangle')
