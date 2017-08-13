#include <stdio.h>
#include <stdlib.h>

/* Declare a buffer for user input of size 2048 */
static char input[2048];

int calcprompt(void);

int main(int argc, char*argv[]) {
  calcprompt();
}

int calcprompt(void) {
  printf("Calcualtor CLI\nCtrl + C to exit\n");
  while (1) {
    /* Output our prompt */
    fputs("> ", stdout);

    /* Read a line of user input of maximum size 2048 */
    fgets(input, 2048, stdin);

    int parsed = atoi(input);
    /* Echo input back to user */
    printf("%d\n", parsed);
  }
}
