def deffuzifikasi(apred_list, r_list):
    z = 0
    z_sum = 0
    z_val = 0
    for i, val in enumerate(apred_list):
        z_sum += val * r_list[i]
        z_val += val
    z_avg = z_sum / z_val
    return int(z_avg)
