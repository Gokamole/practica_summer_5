from Dprocessing import Data_Proc 

def main():
    filename = "var12.csv"  
    processor = Data_Proc(filename)  
    processor.valid_file()  

if __name__ == "__main__":
    main() 
