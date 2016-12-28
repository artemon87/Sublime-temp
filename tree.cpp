#include <iostream>

using namespace std;

class Tree
{
	struct Node
	{
		Node *right = NULL;
		Node *left = NULL;
		int item;
	};
private:
	Node *head;
	int size;
public:
	Tree()
	{
		head = NULL;
		size = 0;
	}
	~Tree()
	{
	}
	void print()
	{
		Node *temp = head;
		if (temp!= NULL)
			printHelper(temp);
	}
	void printHelper(Node *temp)
	{
		if(temp != NULL)
		{
			cout << temp->item << endl;
			printHelper(temp->left);
			printHelper(temp->right);

		}
		
	}
	void add(int value)
	{
		Node *it = head;
		if (it == NULL)
		{
			Node *newNode = new Node();
			newNode->item = value;
			head = newNode;
		}
		else
		{
			while(true)
			{
				if (it->item <= value)
				{
					if(it->right != NULL)
						it = it->right;
					else
					{
						Node *newNode = new Node();
						newNode->item = value;
						it->right = newNode;
						break;
					}
				}
				else
				{
					if(it->left != NULL)
						it = it->left;
					else
					{
						Node *newNode = new Node();
						newNode->item = value;
						it->left = newNode;
						break;
					}
				}
			}

		}
		
	}

};
int main()
{
	Tree t;
	t.add(6);
	t.add(2);
	t.add(1);
	t.add(9);
	t.print();
	return 0;
}