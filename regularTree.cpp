#include <iostream>

using namespace std;

class Node
{
private:
	Node *children;
	int size;
public:
	Node(int size)
	{
		children = new Node[size];
		this->size = size;
	}
	Node(){}
	Node getChild(int index)
	{
		return children[index];
	}
	void add(int n)
	{
		for(int i = 0; i < size; i++)
		{
			children[i] = new Node(i);
		}
	}

};
int main()
{
	Node n;
	Node n1(5);
	return 0;
}