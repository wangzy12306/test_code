#include <stdio.h>
#include <string.h>
#include "a.h"
#include <iostream>
using namespace std;
class line
{
	public:
		line(const char* s)
		{
			cout << "构造函数0\n";
			mine = new char[100];
			strncpy(mine,s,100);
			ganrao = new char[100];
			strncpy(ganrao,"10086",100);
		};
		~line(){
			delete [] mine;
			cout << "析构函数\n";
		};
		line(const line& old)
		{
			cout << "构造函数1\n";
			mine = new char[100];
			strncpy(mine,old.ganrao,100);
		};
		void display()
		{
			printf("line %s\n",mine);
		};
		void display1()
		{
			printf("line %s\n",ganrao);
		}; 
		
	private:
		char* mine;
		char* ganrao;
};

int main()
{
	line ff("wwww");
	line gg = ff;
	gg.display1(); //乱码,因为拷贝构造函数并未调用第一个构造函数
	return 0;
}





















