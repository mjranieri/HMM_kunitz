import matplotlib.pyplot as plt
import numpy as np

def plot_roc_curve(tpr_list, fpr_list):
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_list, tpr_list, color='blue', lw=2, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (FPR)')
    plt.ylabel('True Positive Rate (TPR)')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()

def calculate_auc(tpr_list, fpr_list):
    sorted_indices = np.argsort(fpr_list)
    sorted_fpr = np.array(fpr_list)[sorted_indices]
    sorted_tpr = np.array(tpr_list)[sorted_indices]
    auc = np.trapz(sorted_tpr, sorted_fpr)
    return auc

def main():
    tpr_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.994, 0.994, 0.989, 0.984, 0.984, 0.984, 0.973,  0.946, 0.936, 0.930, 0.920, 0.909, 0.872, 0.813]
    fpr_list = [0.462, 0.040, 0.003, 0.0003, 7.379, 3.514, 1.757, 3.514, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    auc = calculate_auc(tpr_list, fpr_list)
    if auc > 1.0:
        auc = 1.0
    elif auc < 0.0:
        auc = 0.0

    print("AUC:", auc)

    plot_roc_curve(tpr_list, fpr_list)

if __name__ == '__main__':
    main()
