import os 
  
# Function to rename multiple files 
def main():
    a = "C:/Users/SHASHANK PRADHAN/Documents/WORK/JOB/Iesoft/Project/resources/";
    for count, filename in enumerate(os.listdir(a)): 
        dst ="img" + str(count) + ".png"
        src =a+ filename 
        dst =a+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
