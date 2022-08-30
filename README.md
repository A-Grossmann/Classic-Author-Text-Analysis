# Classic-Author-Text-Analysis
Reads through txts using the Guttenberg library of open source classic novels.  Determines many attributes of their writings and constructs a DataFrame for such.   Able to predict who wrote what using Machine Learning. This is a Multi-Class Classification problem.

Author_Methods code:

        - The first file Author_Methods.py is set up to scrub txt files located in the same directory as the code.   'path_directory' variable should be changed           if needing files locally located.
        see changing 'path directory for txt file' in the portoin of code below in the Author_Methods.py file.
        
        path_of_the_directory = 'path directory for txt files'
        ext = ('.txt')
        for file in os.listdir(path_of_the_directory):
          if file.endswith(ext):
    	      print(f'{file}')
    	      file = text_analysis(f'{file}') 
          else:
            continue
        
       - The csv here has the data from running the program for the txt files located in the repository.
        
       - New text and new authors can be added to the data by altering the code for a new text_analysis(new file name) instance.  This will create a new line in            the csv DataFrame. The Author_Data csv file which is essentially a feature set of the txts.
       - Versions for code noted if virtual environment needed:
       
                        nltk == 3.7
                        pandas == 1.4.3
                        numpy == 1.22.3
                        matplotlib == 3.5.3
                        regex ==2022.7.25
                        scikit-learn==1.1.2
   
   Analyzing which features to use...
   
   corr_matrix code:
   
        -Data written into a csv file for correlation matrix to cancel out redundant variables in the KNN Algorythm
        Common types of Adverbs for word pecentages showed redundant.
    
    averaging_author_data code:
        -This code writes a DataFrame to a csv file to look at each classical author charicteristics on average on how they write.   Some features do not show a              high level of variance from author to author.  These 
        
  Finding a machine learning algorythm for data:
  
  running_knn3 py file:
        This shows code for the K Nearest Neighbor method.  the skikit-learn package was used for knn clasification analysis.   The different amount of neighbors and the accuracy metrics was used on the 70%,30% Train, Test slit data sets.  An 54% accuracy was obtained for n = 3 in KNN.
