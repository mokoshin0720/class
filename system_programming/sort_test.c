#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
​
struct entry {
  char name[32];
  char sex;
  int  age;
  struct entry *next;
  struct entry *prev;;
};
​
struct entry *CreateEntry()
{
  struct entry *ep;
​
  ep = (struct entry *)malloc(sizeof(struct entry));
  ep->next = NULL;
  ep->prev = NULL;
  
  return ep;
}
​
struct entry *ReadEntryData(struct entry *Top)
{
  struct entry *ep;
  char *cp, *tp;
  char buf[512];
  char name[32];
  char sex;
  int age;
​
​
  while (fgets(buf, sizeof(buf), stdin) != NULL) {
    /*
     * Node setup
     */
    if (Top == NULL) {
      Top = CreateEntry();
      ep = Top;
    } else {
      //      for (ep = Top; ep->next != NULL; ep = ep->next);
      ep->next = CreateEntry();
      ep->next->prev = ep;
      ep = ep->next;
    }
​
    cp = buf;
    tp = cp;
    if((cp = index(tp, ' ')) == NULL) {
      fprintf(stderr, "Input format fail: %s\n", tp);
      exit(-1);
    }
    *cp++ = '\0';
    strcpy(ep->name, tp);
    
    ep->sex = *cp++;
    cp++;
​
    ep->age = atoi(cp);
  }
  return (Top);
}
​
/*
 * Modifty the sorting function
 */
struct entry * sortlist(struct entry *top)
{
  struct entry *sortp;
  struct entry *cp;
  struct entry *maxp;
    struct entry *ep;
  int flag;
​
  maxp = top;
​
  for(cp = top; cp != NULL; cp = cp->next) {
    if (maxp->age < cp->age) maxp = cp;
  }
  if (top != maxp) {
    maxp->prev->next = maxp->next;
    if(maxp->next) maxp->next->prev = maxp->prev;
    top->prev = maxp;
    maxp->next = top;
    maxp->prev = NULL;
    top = maxp;
  }
    
  sortp = top;
​
  
  while (sortp->next != NULL) {
    maxp = sortp->next;
​
    flag = 0;
    for (cp = sortp->next; cp != NULL; cp = cp->next) {
      if (cp->age > maxp->age) {
	maxp = cp;
	flag++;
      }
    }
    if (!flag) {
      if (sortp->next->next != NULL) {
	sortp = sortp->next;
	continue;
      }
      break;
    }
​
    /*
     * move maxp sortp 
     */
    maxp->prev->next = maxp->next;
    if (maxp->next != NULL)
      maxp->next->prev = maxp->prev;
    maxp->next = sortp->next;
    maxp->prev=sortp;
    sortp->next = maxp;
    sortp = maxp;
  }
      
    
  return(top);
}
​
int main()
{
  struct entry *Top;
  struct entry *ep;
​
  /*
   * read data
   */
  Top = (struct entry *)NULL;
  Top = ReadEntryData(Top);
​
  /*
   * Print out Entry Data
   *
  printf("Name\tSex\tAge\n");
  for (ep = Top; ep != NULL; ep = ep->next) {
    printf("%s\t%c\t%d\n", ep->name, ep->sex, ep->age);
  }
  */
  /* 
   * sorting by age
   */
  Top = sortlist(Top);
​
  printf("Name\tSex\tAge\n");
  for (ep = Top; ep != NULL; ep = ep->next) {
    printf("%s\t\t%c\t%d\n", ep->name, ep->sex, ep->age);
  }
​
​
}