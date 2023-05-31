import sys
import numpy as np

def get_matrix(eval_file, posi_file, threshold):
    with open(posi_file) as file:
        positive_list = []
        for line in file:
            positive_list.append(line.strip())
    with open(eval_file) as file1:
        tp, tn, fp, fn = 0, 0, 0, 0
        fp_list=[]
        fn_list=[]
        for line1 in file1:
            line1 = line1.rstrip().split()
            entry = line1[0]
            e_val=float(line1[1])
            if e_val <= threshold and entry in positive_list:
                tp += 1
            elif e_val <= threshold and entry not in positive_list:
                fp += 1
                fp_list.append(entry)
            elif e_val > threshold and entry in positive_list:
                fn +=1
                fn_list.append(entry)
            else:
                tn +=1
        conf_matrix = np.array([[tp, fp], [fn, tn]])
        acc = (conf_matrix[0][0]+conf_matrix[1][1])/np.sum(conf_matrix)
        mcc = ((conf_matrix[1][1]*conf_matrix[0][0]) - (conf_matrix[0][1]*conf_matrix[1][0]))/np.sqrt((conf_matrix[1][1]+conf_matrix[0][1])*(conf_matrix[1][1]+conf_matrix[1][0])*(conf_matrix[0][0]+conf_matrix[0][1])*(conf_matrix[0][0]+conf_matrix[1][0]))
        
        tpr = tp / (tp + fn)
        fpr = fp / (fp + tn)
        
        return conf_matrix, acc, mcc, tpr, fpr

def get_entries(eval_file, posi_file, threshold):
    with open(posi_file) as file:
        positive_list = []
        for line in file:
            positive_list.append(line.strip())
    with open(eval_file) as file1:
        fp, fn = 0, 0
        fp_list=[]
        fn_list=[]
        for line1 in file1:
            line1 = line1.rstrip().split()
            entry = line1[0]
            e_val=float(line1[1])
            if e_val <= threshold and entry not in positive_list:
                fp += 1
                fp_list.append(entry)
            elif e_val > threshold and entry in positive_list:
                fn +=1
                fn_list.append(entry)
        return fp_list, fn_list

if __name__ == "__main__":
    eval_file = sys.argv[1]
    posi_file = sys.argv[2]
    threshold = float(sys.argv[3])
    matrix, acc, mcc, tpr, fpr = get_matrix(eval_file, posi_file, threshold)
    fp_list, fn_list= get_entries(eval_file, posi_file, threshold)
    print("Matrix:", matrix)
    print("ACC:", acc)
    print("MCC:", mcc)
    print("TPR:", tpr)
    print("FPR:", fpr)
    print("Threshold:", threshold)
    print("FP entries:", fp_list)
    print("FN entries:", fn_list)
