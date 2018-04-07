import matplotlib.pyplot as plt
import os, time, glob
import pandas as pd
import pandas.api.types as ptypes
import seaborn as sns

def data_import(filename):
    patients = pd.read_csv(filename)
    return(patients)

def generate_tuples():
    filename = '/home/cot/mysite/seer_app/patient_table_data5000.csv'
    #filename = '~/GitHub/HW5-code/seer_app/patient_table_data5000.csv'
    self = data_import(filename)

    x_tuple = ()
    y_tuple = ()
    x_tuples = []
    y_tuples = []
    for col in self:
        typ = ptypes.infer_dtype(self[col])
        if typ == "integer":
            y_tuple = (col,col)
            y_tuples.append(y_tuple)
        elif typ == "string":
            x_tuple = (col,col)
            x_tuples.append(x_tuple)
    tuples = [x_tuples, y_tuples]
    return(tuples)

def compute_metrics(x,yaxis):
   result = {'MIN': x[yaxis].min(), 'MAX': x[yaxis].max(),'MEDIAN': x[yaxis].median(), 'MEAN': x[yaxis].mean()}
   return pd.Series(result, name='metrics')

def plot(X, Y):
    """Return filename of plot of boxplots."""
    filename = '~/Health-IT-Apps-Course/patient_table_data5000.csv'
    patients = data_import(filename)

    compute_metrics(patients.groupby(Y),Y)

    plt.figure()  # needed to avoid adding curves in plot

    sns.set_style("whitegrid")
    ax = sns.boxplot(x = patients[X], y= patients[Y])
    plt.title(Y + " for each " + X + " group")
    plt.xlabel(X +" group",fontsize=15)
    plt.ylabel(Y + " (in Years)",fontsize=15)
    plt.xlim(-1, 4)
    plt.ylim(0, 130)
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
       # Remove old plot files
       for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile
