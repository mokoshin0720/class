#include "types.h"
#include "stat.h"
#include "user.h"

int main(void)
{
// ⽂字列を定義
char buf[256] = "Helloworld\n";
// 1番に書き込む
write(1, buf, 256);
exit();
}