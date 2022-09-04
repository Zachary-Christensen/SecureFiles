# SecureFiles
This project uses the given key to encrypt or decrypt a list of files passed either as command line options or hard coded as a list within the script.



How to use:

  ./SecureFiles.py (decrypt|encrypt) key {filename}
  
  Example:
  
    ./SecureFiles.py encrypt key file1 secret.txt
    
    OR
    
    Add filenames as strings to filenames list variable located in main method and simply run 
    
      ./SecureFiles.py encrypt key
