


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char* argv[], char** env){
// sleep(5);
printf("env: Myname is %s\n",getenv("MYNAME"));
    printf("env: Myname is %s\n",env[1]);
printf("中文111!\n");
    // char** env1;
    // for (env1=env; *env1 != 0; env1++)
    // {
    //     char* thisEnv = *env1;
    //     printf("%s\n", thisEnv);
    // }
return 0;
}
///%include:test.c
