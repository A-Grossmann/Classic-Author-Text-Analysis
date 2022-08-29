# Classic-Author-Text-Analysis
Reads through txts using the Guttenberg library of open source classic novels.  Determines many attributes of their writings and constructs a DataFrame for such.   Able to predict who wrote what using Machine Learning  

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
        
       - New text and new authors can be added to the data by altering the code for a new text_analysis(new file name) instance.  This will create a new line in            the csv DataFrame.
       - Versions for code noted if virtual environment needed:
       
                        nltk == 3.7
                        pandas == 1.4.3
                        numpy == 1.22.3
                        matplotlib == 3.5.3
                        regex ==2022.7.25
   corr_matrix code:
   
        -Data written into a csv file for correlation matrix to cancel out redundant variables in the KNN Algorythm
        Common types of Adverbs for word pecentages showed redundant.
        
        
        
