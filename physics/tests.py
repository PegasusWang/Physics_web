#coding=utf-8
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

n_groups = 6

means_men = (20, 35, 30, 35, 27, 18)
#std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20, 25, 18)
#std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
#bar_width = 0.35
bar_width = 0.2

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 #align="center",
                 #yerr=std_men,
                 error_kw=error_config,
                 label='Men')

rects2 = plt.bar(index + bar_width, means_women, bar_width,
                 alpha=opacity,
                 color='r',
                 #align="center",
                 #yerr=std_women,
                 error_kw=error_config,
                 label='Women')

rects3 = plt.bar(index+bar_width*2, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 #align="center",
                 #yerr=std_men,
                 error_kw=error_config,
                 label='Men')

rects4 = plt.bar(index+bar_width*3, means_men, bar_width,
                 alpha=opacity,
                 color='g',
                 #align="center",
                 #yerr=std_men,
                 error_kw=error_config,
                 label='Men')

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2.0, 1.05*height,
                '%d'%int(height), ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)


plt.xlabel(u'题号')
plt.ylabel(u'人数')
plt.title(u'答题结果统计')
plt.xticks(index + bar_width, ('1', '2', '3', '4', '5', '6'))
#plt.legend()
ax.set_ybound(0, 40)

plt.tight_layout()
plt.show()
#plt.savefig(u't.png')
