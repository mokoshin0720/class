#include "types.h"
#include "stat.h"
#include "user.h"

int main(void)
{
char buffer[256];
// 1番を使ってInputという⽂字を出⼒する
printf(1, "Input: ");
// 0番を使ってキーボードからの⼊⼒を受け取る
read(0, buffer, 256);
// 1番を使って、受け取った⽂字列を出⼒する
printf(1, "Output: %s\n", buffer);
exit();
}