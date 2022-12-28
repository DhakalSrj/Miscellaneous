//C programming
//windows 11 and runs on omega 

#include <stdio.h>
#include <string.h> // string library 
#include <dirent.h> //structure for directory stream 
#include <sys/stat.h> //structure of data returned by the function stat() used below 


//recurcive function that calculates the total size of all file in the current directory/folders and sub folders 
int DirSpace(const char *target)
{
	int total = 0;
	//to initialize the search and find the first entry opendir() is used 
	DIR *directory = opendir(target);
	/*to get the information about the specified file and place it in the memory area pointed by	
    the buf argument given by int stat(const char *path, struct stat *buf); */
	struct stat filestat;
	//if directory is null print invalid message 
	//return 1 means there is an error 
	if (directory == NULL)
	{
		printf("\n This is an Invalid Directory \n");
		return 1;
	}
	//directory entry 
	struct dirent *file;
	char name[256];
	
	// iterate while the next entry is not null
	while((file = readdir(directory)) != NULL)
	{
		//is no abosulte or relative paths present do nothing
		if (strcmp (file->d_name, ".") == 0 || strcmp(file->d_name,"..") == 0)
		{
		}
		//if the entry type is a directory i.e. DT_DIR given by dirent.h then call the function itself and go through the files 
		else if(file->d_type == DT_DIR)
		{
			//this gives us  (./D/File)
			strcpy(name,target);
			strcat(name,"/");
			strcat(name,file->d_name);
			total += DirSpace(name);
		}
		//if the entry is a file then get the size 
		else 
		{
		    //this gives us (./File)
			strcpy(name,target);
			strcat(name,"/");
			strcat(name,file->d_name);
			stat(name, &filestat);//obtains information on the named file and writes it to file status
			total += filestat.st_size;
		}
	}
	//closes the directory stream 
	closedir(directory);
	//returns the total size 
	return total;
}
//start of main
int main( int argc, const char *argv[])
{
	char target[256] = ".";
	printf("\nThe total size of the directory is: %d bytes\n",DirSpace(target));
	//end of main
	return 0;
}


	
	
	
	
	
