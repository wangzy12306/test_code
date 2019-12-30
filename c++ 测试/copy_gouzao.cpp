#include <string.h>
#include <iostream>
//拷贝构造函数主要是为了把一个新类 = 一个旧类,类中会默认有一个拷贝构造函数
//但需要申请空间时,必须有这样一个函数,等于时为新类中变量申请并赋值
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
			//printf("line %s\n",mine);
			cout << "line " << mine << endl;
		};
		void display1()
		{
			//printf("line %s\n",ganrao);
			cout << "line " << ganrao << endl;
		}; 
		
	private:
		char* mine;
		char* ganrao;
};

int main()
{
	line ff("wwww");
	line gg = ff;
	ff.display();	//正常打印
	gg.display();	//正常打印
	ff.display1();	//正常打印,已对ganrao变量赋值
	gg.display1();	//乱码,因为拷贝构造函数并未调用第一个构造函数
	return 0;
}
