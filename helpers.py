import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def search_question(schema, search_term):
    """
    Parameters:
        schema (pandas.core.frame.DataFrame): dataframe containing two columns
            'Column' - strings corresponding with the column names from the main dataframe
            'QuestionText' - strings corresponding to the question asked on the survey
        search_term (str): term to search to retrieve index and text
        
    Returns:
        questions (list): list of dictionaries, where each dictionary corresponds to a distinct question has three keys
                            * id (int): index
                            * colname (str): column name
                            * question (str): text from the question found.
    """
    
    idx_ = schema[schema['QuestionText'].str.contains(search_term)].index
    
    questions = []
    
    for i in idx_:
        questions.append(
            {
                'id': i,
                'colname': schema['Column'][i],
                'question': schema['QuestionText'][i]
            })
    
    return questions


def get_counts(pd_serie):
    """
    Takes in a column with numeric values and returns the percentage of unique values in the dataset.
    
    Parameters:
        pd_serie (pandas.core.series.Series): pandas Series
        
    Returns:
        pandas.core.series.Series with percentages of the unique values in the original data input.
        
    """
    return pd_serie.value_counts() / (pd_serie.shape[0] - sum(pd_serie.isnull())) * 100

def plot_stats(x, y, title='Title', xlabel_='X labels', ylabel_='Y labels', xticks_labels=None, color=(0.1, 0.2, 0.5, 0.7), filename=None):
    """
    Plots a bar graph out of pandas Series values (index, values).
    
    Parameters:
        x: labels
        y: values
        
        Optional values
            title (str): graph title - default 'Title'
            xlabel_ (str): label for the X axis - default 'X labels'
            ylabel_ (str): label for the Y axis - default 'Y labels'
            xticks_labels (list): change the X labels for the given list of labels - default None
            color (tuple): default (0.1, 0.2, 0.5, 0.7)
            filename (str): name and extension of the file to save the graph - default None
        
    Returns:
        bar graph with the specified characteristics
    """
    plt.bar(x, y, align='center', color=color)
    plt.xticks(x, labels=xticks_labels, rotation='vertical')
    plt.yticks(ticks=np.arange(0, 110, 10), labels=list(map(lambda ytick: f"{round(ytick, 1)}%", np.arange(0, 110, 10))))
    plt.title(title)
    plt.xlabel(xlabel_)
    plt.ylabel(ylabel_)
    plt.autoscale()
    
    if filename:
        plt.savefig(filename, bbox_inches = "tight")
    elif handles and legend_labels:
        plt.legend(handles, legend_labels)
    
    return plt.show()