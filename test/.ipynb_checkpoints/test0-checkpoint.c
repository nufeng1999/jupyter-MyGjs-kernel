



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <sys/prctl.h>

int getsline(char *result)
{
    int point = 0;
    int word;
    long i=0;
    while(1)
    {
        i++;
        usleep(100);
        word = getc(stdin);//等待用户输入或从缓存中读一个字符
        if(word != '\n')//读到回车符就认为一行指令被读完了
        {
            *result = word;//记录这个字符
            result ++;
            point ++;
            //putc(word,stdout);
        }
        else
        {
            result = '\0';//给指针末尾添加一个结束符
            result = result - point;//让指针指回字符串的头
            return 0;
        }
    }
    return 0;
}

int main()
{
    // char buff[3];
   
   // memset( buff, '\0', sizeof( buff ));
   
   // fprintf(stdout, "Going to set full buffering on\n");
   // setvbuf(stdout, buff, _IOFBF, 3);
    char *line;
    line = malloc(150);
    printf("Please enter text\n");
    getsline(line);
    printf("You enter:%s\n",line);
    free(line);
    // prctl(PR_SET_PDEATHSIG,SIGHUP);
    // raise(SIGCHLD);
    return 0;
}
