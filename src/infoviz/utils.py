import matplotlib.pyplot as plt

def set_rcParams(**kwargs):
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['font.family'] = 'serif'
    for k, v in kwargs.items():
        try:
            plt.rcParams[k] = v
        except KeyError:
            pass