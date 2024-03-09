#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author: yjf
@Create: 2024/1/19 9:47
@Message: null
"""
import os
from shutil import copy

import matplotlib
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print('demo')

    # # 基于 seg mask 从 voc2012 中复制对应的 image
    # src_image_path = r'C:\Users\40977\Desktop\temp\todo\MaskR_CNN_TEST\data\VOCdevkit\VOC2012\JPEGImages'
    # seg_class_path = 'VOCdevkit/VOC2007/SegmentationClass'
    # dst_image_path = 'VOCdevkit/VOC2007/JPEGImages'
    #
    # seg_list = os.listdir(seg_class_path)
    # print('seg mask file count {}'.format(len(seg_list)))
    # count = 0
    # for file_name in seg_list:
    #     file_prefix, file_extension = os.path.splitext(file_name)
    #     # print(file_name)
    #     from_path = os.path.join(src_image_path, file_prefix+'.jpg')
    #     to_path = os.path.join(dst_image_path, file_prefix+'.jpg')
    #     copy(from_path, to_path)
    #     count += 1
    #
    # print("copied count {}".format(count))

    # 查看本机已有字体
    # a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
    # for i in a:
    #     print(i)
    # plt.rcParams["font.family"] = 'Arial Unicode MS'

