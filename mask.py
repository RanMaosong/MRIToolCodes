import matplotlib.pyplot as plt 
import math
import numpy as np
import random


def radial_mask(h, w, sampling_rate):
    def inner(line_num):
        T = np.linspace(0, math.pi, line_num)
        umask = np.zeros((h, w))

        for i in range(line_num):
            kk = math.tan(T[i])
            c1 = math.sqrt(kk*kk + 1)
            for m in np.arange(-h/2+0.5, h/2-0.5):
                for n in np.arange(-w/2+0.5, w/2-0.5):
                    mm = int(m + h/2+0.5)
                    nn = int(n + w/2 + 0.5)
                    d = abs(kk*m-n) / c1
                    if d < 1/2:
                        umask[mm, nn] = 1
        return umask

    left = 1
    right = 256
    right_mask = inner(right)
    tmp_sampling_ratio = np.sum(right_mask) / right_mask.size
    while tmp_sampling_ratio < sampling_rate:
        left = right
        right *= 2
        right_mask = inner(right)
        tmp_sampling_ratio = np.sum(right_mask) / right_mask.size

    while left < right - 1:
        mid = (left + right) // 2
        umask = inner(mid)
        cur_sampling_rate = np.sum(umask) / umask.size
        print("[{}, {}, {}]={}".format(left, mid, right, cur_sampling_rate))
        if cur_sampling_rate <= sampling_rate:
            left = mid
        else:
            right = mid
    
    left_mask = inner(left)
    right_mask = inner(right)

    left_sampling_ratio = np.sum(left_mask) / left_mask.size
    right_sampling_ratio = np.sum(right_mask) / right_mask.size

    if abs(left_sampling_ratio - sampling_rate) < abs(right_sampling_ratio - sampling_rate):
        print("采样率: ", left_sampling_ratio)
        return left_mask
    else:
        print("采样率: ", right_sampling_ratio)
        return right_mask



def uniform_mask(h, w, total_line_num, cent_line_num):
    sampling_indices = []
    other_indices = []
    for i in range(h//2 - cent_line_num//2, h//2 + cent_line_num//2):
        sampling_indices.append(i)
    
    for i in range(0, h//2 - cent_line_num//2):
        other_indices.append(i)
    
    for i in range(h//2 + cent_line_num//2, h):
        other_indices.append(i)
    
    step = len(other_indices) // (total_line_num - cent_line_num)
    for i in range(0, len(other_indices), step):
        sampling_indices.append(other_indices[i])
    
    mask = np.zeros((h, w), dtype=np.int8)
    for i in sampling_indices:
        mask[i, :] = 1
    
    print("采样率: ", np.sum(mask)/ mask.size)
    return mask
    

def cartesian(h, w, total_line_num, cent_line_num):
    random.seed(15)
    sampling_indices = []
    other_indices = []
    for i in range(h//2 - cent_line_num//2, h//2 + cent_line_num//2):
        sampling_indices.append(i)
    
    for i in range(0, h//2 - cent_line_num//2):
        other_indices.append(i)
    
    for i in range(h//2 + cent_line_num//2, h):
        other_indices.append(i)
    
    random_indices = random.sample(other_indices, total_line_num - cent_line_num)
    sampling_indices.extend(random_indices)
    mask = np.zeros((h, w), dtype=np.int8)
    for i in sampling_indices:
        mask[i, :] = 1
    
    print("采样率: ", np.sum(mask)/ mask.size)
    return mask


if __name__ == "__main__":
    # mask = radial_mask(320, 320, 0.3)
    # mask = uniform_mask(320, 320, 40, 10)
    # mask = cartesian(320, 320, 70, 10)
    mask = np.random.normal(size=(320, 320))
    mask = np.where(mask > 0.5, 1, 0)
    plt.imshow(mask, cmap="gray")
    plt.show()
