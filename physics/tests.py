#coding=utf-8
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']    # set default font


def draw_result(a_num, b_num, c_num, d_num, n_groups):
    """Draw result.

    :param a_num: tuple of select A users.
                  eg: (12, 2, 34, 12, 78, 13).
    :param n_groups: The length of tuple a_num.
    """
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, a_num, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='A')

    rects2 = plt.bar(index + bar_width, b_num, bar_width,
                     alpha=opacity,
                     color='r',
                     error_kw=error_config,
                     label='B')

    rects3 = plt.bar(index+bar_width*2, c_num, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='C')

    rects4 = plt.bar(index+bar_width*3, d_num, bar_width,
                     alpha=opacity,
                     color='g',
                     error_kw=error_config,
                     label='D')

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
    #plt.xticks(index + bar_width, ('1', '2', '3', '4', '5', '6'))
    plt.xticks(index + bar_width, tuple(map(str, range(1, n_groups+1))))
    ax.set_ybound(0, 40)

    plt.tight_layout()
    plt.show()
    #plt.savefig(u't.png')


n_groups = 6
a_num = (20, 35, 30, 35, 27, 18)
b_num = (25, 32, 34, 20, 28, 18)
c_num = (25, 32, 34, 27, 25, 18)
d_num = (25, 31, 33, 20, 25, 18)
draw_result(a_num, b_num, c_num, d_num, n_groups)
