#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <pthread.h>
#include <err.h>

pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;

struct entry {
  char name[32];
  char sex;
  int  age;
  struct entry *next;
  struct entry *prev;;
};

// 1entry分のメモリを確保
struct entry *CreateEntry()
{
  struct entry *ep;

  ep = (struct entry *)malloc(sizeof(struct entry));
  ep->next = NULL;
  ep->prev = NULL;
  
  return ep;
}

// 構造体の要素全体をTopとする。
struct entry *ReadEntryData(struct entry *Top)
{
  struct entry *ep;
  char *cp, *tp;
  char buf[512];
  char name[32];
  char sex;
  int age;


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

    ep->age = atoi(cp);
  }
  return (Top);
}

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

  maxp = top;

  // 最大のageを"maxp"に格納
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

  // 最大ageを持ったstructをsortpに格納 -> 以降はソートなしで、ただのファイル順
  sortp = top;
  
  // nullデータになるまで、whileを回す
  while (sortp->next != NULL) {
    // 1番上の行をmaxpとする
    maxp = sortp->next;

    flag = 0; // 0か1を決めたいだけ -> 2以上に意味はない

    pthread_mutex_lock(&m);
    // 全てのデータを参照
    for (cp = sortp->next; cp != NULL; cp = cp->next) {
      // 1行目以降の最大値を取得
      if (cp->age > maxp->age) {
	      maxp = cp;
	      flag++;
      }
    }

    // 次のループのために、sortpをmaxpに置き換える
    if (!flag) {
      // sortpの置き換えをする
      if (sortp->next->next != NULL) {
	      sortp = sortp->next;
        pthread_mutex_unlock(&m);
      	continue;
      }
      pthread_mutex_unlock(&m);
      break;
    }
    else {
      maxp->prev->next = maxp->next;
      if (maxp->next != NULL) maxp->next->prev = maxp->prev;
      maxp->next = sortp->next;
      maxp->prev=sortp;
      sortp->next = maxp;
      sortp = maxp;
      pthread_mutex_unlock(&m);
    }
  }
      
    
  return(top);
}

int main()
{
  struct entry *Top;
  struct entry *ep;

  pthread_t thread1, thread2;
  int ret1, ret2;
  pthread_mutex_init(&m, NULL);

  /*
   * read data
   */
  Top = (struct entry *)NULL;
  Top = ReadEntryData(Top); // この時点では、上からdataを読み込んでいるだけ → nextを使うと次の行に行ける。
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

  pthread_create(&thread1, NULL, sortlist, Top);
  pthread_create(&thread2, NULL, sortlist, Top);

  // pthread_createのエラー処理
  if (ret1 != 0) {
    err(EXIT_FAILURE, "can not create thread 1: %s", strerror(ret1) );
  }
  if (ret2 != 0) {
    err(EXIT_FAILURE, "can not create thread 2: %s", strerror(ret2) );
  }

  printf("execute pthread_join thread1\n");
  pthread_join(thread1, Top);
  if (ret1 != 0) {
    errc(EXIT_FAILURE, ret1, "can not join thread 1");
  }

  printf("execute pthread_join thread2\n");
  pthread_join(thread2, Top);
  if (ret2 != 0) {
    errc(EXIT_FAILURE, ret2, "can not join thread 2");
  }


  printf("Name\tSex\tAge\n");
  for (ep = Top; ep != NULL; ep = ep->next) {
    printf("%s\t\t%c\t%d\n", ep->name, ep->sex, ep->age);
  }

  pthread_mutex_destroy(&m);

}
