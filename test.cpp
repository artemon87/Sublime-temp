#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

void reverse(string);
int main()
{
	int i = 6;
	cout << i << endl;
	reverse("Hello my name is");
	string st = "string";
	char c[st.length() + 1];
	strcpy(c, st.c_str());
	std::vector<char> v;
	v.push_back(c[1]);
	cout << v[0];
	return 0;
}
void reverse(string s1)
{
	//const char *ch = s1.c_str();

	char *ch2;// = new char[s1.length() +1];
	vector<char> output;
	strcpy(ch2, s1.c_str());
	int last = s1.length() + 1;
	int letters = 0;
	int lastKnown = 0;
	int start = last;
	while(true)
	{
		start = start - letters;
		letters = 0;
		cout << "while loop entered " << endl;
		while(ch2[start] != ' ' || start == 0)
		{
			cout << ch2[start] << endl;
			start--;
			letters++;
		}
		lastKnown = start;
		for(int i = 0; i < letters; i++)
		{
			output.push_back(ch2[lastKnown+i]);
		}
		if(start == 0)
		{
			break;
		}

	}
	for(int i = 0; i < s1.length() + 1; i++)
	{
		cout << output[i] ;
	}
	



}