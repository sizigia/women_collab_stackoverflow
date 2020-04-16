
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There aren't any necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.  
I used the following libraries:
- [matplotlib.pyplot](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.html) -- matplotlib version '3.1.3'
- [numpy](https://numpy.org/) -- version '1.18.1'
- [pandas](https://pandas.pydata.org/) -- version '1.0.1'
- [re](https://docs.python.org/3/library/re.html) -- version '2.2.1'
- [seaborn](https://seaborn.pydata.org/) -- version '0.10.0'

## Project Motivation<a name="motivation"></a>

For this project, I was interested in using Stack Overflow Developer Survey data from 2019 related to women developers, specially those actively working at the time of the survey, to gain insights on:

1. What kind of employment was predominant among the women participants?
2. Were they working as developers or similar?
3. What kind of education most of them had?
4. What are the top 10 countries these women are located?
5. Was there some relation between their ethnicity and the country they were located?
6. What was the social media site of choice accordingnly with their age?
7. What was the frequency of participation in Stack Overflow?

This approach is by far non-comprehensive and many of these question are merely an approximation to reality.  
That said, there's a lot more of analysis to be done!  


## File Descriptions <a name="files"></a>

- README.md, this very file you're reading

#### Essentials:
- data
- Women in Stack Overflow Annual Developer Survey (2019).ipynb
- helpers.py

#### Disposables:
- women_SO_notes.txt
- img

There's a [Jupyter notebook](#essentials) containing the full analysis.  
It goes hand-by-hand with [*helpers.py*](#essentials), an additional Python file where I stored my helper functions. Without it, little to no analysis can be done.  
  
The third member of this trinity is the folder [***data***](#essentials). It contains two *csv* files corresponding to the public data for women developers I used for the analysis and the schema relating column names from the data to the questions asked in the survey.The last one is a README file with more information about the data.  
  
The folder [***img*** and *women_SO_notes.txt*](#disposables) are files produced by the notebook. They may change if you change parts of the analysis. You can delete them if forking the project, it's totally cool :)


## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://www.faustinamaria.com/women-stackoverflow).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

>This database - The Public 2019 Stack Overflow Developer Survey Results - is made available under the Open Database License (ODbL): http://opendatacommons.org/licenses/odbl/1.0/.  
Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/  
You are free to share, adapt, and create derivative works from The Public 2019 Stack Overflow Developer Survey Results as long as you attribute Stack Overflow, keep the database open (if you redistribute it), and continue to share-alike any adapted database under the ODbl.