#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

ino_t get_inode(char *);
void print_path_to(ino_t);
void inum_to_name(ino_t, char *, int);

int main()
{
    print_path_to(get_inode(".")); // カレントディレクトリまでの絶対パスを出力
    putchar('\n');
    return 0;
}

/*
引数のディレクトリまでのパスを出力する関数
*/
void print_path_to(ino_t this_inode)
{
    ino_t my_inode;
    char its_name[BUFSIZ];

    if(get_inode("..") != this_inode)
    {
        chdir(".."); // 1つ上のディレクトリへ移動する
        
        inum_to_name(this_inode, its_name, BUFSIZ); // サブディレクトリ名の取得
        my_inode = get_inode("."); // カレントディレクトリのiノード番号を取得
        print_path_to(my_inode);  //　再帰処理
        printf("%s/", its_name);
    }
}

/*
カレントディレクトリから引数のiノード番号を持つファイルを探し、名前をnamebufにコピーする関数
*/

void inum_to_name(ino_t inode_to_find, char *namebuf, int buflen)
{
    DIR *dir_ptr;
    struct dirent *direntp;

    dir_ptr = opendir(".");
    if(dir_ptr == NULL) // ディレクトリが存在しない場合
    {
        perror(".");
        exit(1);
    }

    while((direntp = readdir(dir_ptr)) != NULL)
        if(direntp->d_ino == inode_to_find)
        {
            strncpy(namebuf, direntp->d_name, buflen);
            namebuf[buflen-1] = '\0';
            closedir(dir_ptr);
            return;
        }
    fprintf(stderr, "error looking for inum %llu\n", inode_to_find);
    exit(1);
}

/*
ファイルのiノード番号を返す関数
*/
ino_t get_inode(char *frame)
{
    struct stat info;

    if(stat(frame, &info) == -1)
    {
        fprintf(stderr, "stat error");
        perror(frame);
        exit(1);
    }
    return info.st_ino;
}