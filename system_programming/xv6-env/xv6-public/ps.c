#include "procinfo.h"
#include "types.h"
#include "stat.h"
#include "user.h"
#include "param.h"

int
main(void)
{
  // procを列挙
  enum procstate {UNUSED, EMBRYO, SLEEPING, RUNNABLE, RUNNING, ZOMBIE};
  
  // 静的配列の定義
  static char *states[] = {
    [UNUSED]        "UNUSED",
    [EMBRYO]        "EMBRYO",
    [SLEEPING]      "SLEEPING",
    [RUNNABLE]      "RUNNABLE",
    [RUNNING]       "RUNNING",
    [ZOMBIE]        "ZOMBIE",
  };

  // プロセス情報が書かれているprocinfo型を定義
  struct procinfo procinfo_table[NPROC];
  // getprocsで動いているプロセス数の取得
  int numbers = getprocs(procinfo_table);

  printf(1, "pid / ppid / state / name / sz\n");
  for (int i = 0; i < numbers; i++) {
    // 使われていないプロセスは飛ばす
    if (procinfo_table[i].state == UNUSED)
        continue;

    printf(1, "%d / %d / ", procinfo_table[i].pid, procinfo_table[i].ppid);
    printf(1, "%s / %s / ", states[procinfo_table[i].state], procinfo_table[i].name); 
    printf(1, "%d / ", procinfo_table[i].sz);
    printf(1, "\n");
  }

  exit();
}
