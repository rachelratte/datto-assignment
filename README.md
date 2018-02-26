# datto-assignment
Big data coding assignment for Datto internship interview

Contents: 

    ratter_datto_assignment.py
    
        A python 3.5 program that reads target columns from a csv of stock data into a pandas dataframe, calculates the average of two columns ('open' and 'close'), then exports this data into a parquet file.
        
        Usage: target csv is named 'quandl_full_data.csv' is in same directory as ratter_datto_assignment.py. Exported data will be named 'quandl_full_data.parquet' and will reside in the same directory as ratter_datto_assignment.py
        
        Requires: Pandas and pyarrow (or fastparquet)
       
       
       
Assignment Questions:

      With a file that’s 1.7GB, Pandas will have to read the entire contents into memory… this will be slow. How can you test your script without having to process all of this data every time?
      
              Add parameter nrows = # (where # is a manageably small number) to the read_csv() function, to read in and work with a                     smaller portion of the database as a proof of concept.
              
      There are numerous ways to compute the average column and add it to the Pandas, what’s the most efficient way?
              
               Generally (but not always!), built in functions are your best bet for efficiency. In this case I used pandas' built-in                    mean() function because it's efficient both computationally and line-wise.
               
               
      A stock’s price will almost never be zero, and will never be negative… how do you filter out these values before computing the average?
                I checked each row to see if both the 'close' and 'open' columns had values >0. If they don't, we drop the row assuming                   that the data is incorrect.
