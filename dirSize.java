//Java 
//windows 11 and runs on omega

import java.io.File;

public class sxd5507_lab01 {
    //start of main
    public static void main (String[] args) {
        //to print the size of the directory
        System.out.printf("The total size of the directory is: %d bytes \n" , dirSpace(new File ("."))); 
    }
    //recursive function 
    public static long dirSpace(File directory) {
        //long to avoid overflow issue
        long total = (long) 0;
        File files[] = directory.listFiles();
        int num = files.length;
        //iterate through the list of entries 
        for( int i=0 ; i < num ; i++)
        {
            //if the entry is a file get the size and add it to total
            if (files[i].isFile())
            {
                total += files[i].length();
            }
            //if it a directory then call the function itself to go through all the file in them 
            else
            {
                total += dirSpace(files[i]);
            }
        }
        //return total size
        return total;
    }  
}

