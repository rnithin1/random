#include <stdio.h>
#include <unistd.h> 

int main(void) {
    printf("The page size for this system is %ld bytes.\n",
            sysconf(_SC_PAGESIZE)); 
    return 0;
}
