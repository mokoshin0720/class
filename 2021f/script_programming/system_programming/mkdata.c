#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main(int ac, char *av[])
{

  int age;
  char sex;
  FILE *fp;
  char name[64];

  if (!(ac > 1)){
    fprintf(stderr, "Usage: %s name_list_file\n", av[0]);
    exit(0);
  }

  if((fp = fopen(av[1], "r")) == NULL) {
    fprintf(stderr, "Cannot open: %s\n", av[1]);
    exit(-1);
  }

  while ((fscanf(fp, "%s", name)) > 0) {
    if (rand()%2) {
      sex = 'M';
    }else {
      sex = 'F';
    }
    age = rand()%100;
    
    printf("%s %c %d\n", name, sex, age);
  }
}
  
