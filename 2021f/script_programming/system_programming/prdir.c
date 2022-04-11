#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>

void prdir(char []);

int main(int ac, char *av[])
{
    if (ac == 1) // 引数なしの場合
        prdir(".");
    else // 引数でディレクトリを指定した場合（複数可）
        while ( --ac ) {
            printf("%s:\n", *++av);
            prdir(*av);
        }
}

void prdir(char dirname[])
{
    DIR *dir_ptr;
    struct dirent *direntp;

    if (( dir_ptr = opendir(dirname)) == NULL) // ディレクトリが開けるかのvalidation
        fprintf(stderr, "cannot open %s\n", dirname);
    else // ディレクトリが開けた場合
    {
        while ((direntp = readdir(dir_ptr)) != NULL)
            printf("%s\n", direntp->d_name); // ファイル名を出力
        closedir(dir_ptr);
    }
}