#include <iostream>
#include <algorithm>

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
		clear(head);
	}
	void deepCopy(Tree *&t)const
	{
		//Tree *t;
		if (this->head != NULL)
		{
			//t->head = new Node();
			//t->head->item = this->head->item;
			copyHelp(this->head, t->head);
		}
		//return t;
	}
	void copyHelp(Node *original, Node *&newNode) const
	{
		/*if (original->left != NULL)
		{
			copyHelp(original->left, newNode->left);
			newNode = new Node();
			newNode->item = original->item;
			newNode->left = original->left;
			newNode->right = original->right;
			cout << "Copying nodes, value original: " << original->item << ". New node value: " << newNode->item << endl;
			//copyHelp(original->left, newNode->left);
			//copyHelp(original->right, newNode->right);
		}
		else if (original->right != NULL)
		{
			copyHelp(original->right, newNode->right);
			newNode = new Node();
			newNode->item = original->item;
			newNode->left = original->left;
			newNode->right = original->right;
			cout << "Copying nodes, value original: " << original->item << ". New node value: " << newNode->item << endl;

		}*/
		if(original != NULL)
		{

			newNode = new Node();
			newNode->item = original->item;
			newNode->left = original->left;
			newNode->right = original->right;
			cout << "Copying nodes, value original: " << original->item << ". New node value: " << newNode->item << endl;
			copyHelp(original->left, newNode->left);
			copyHelp(original->right, newNode->right);
		}

	}
	void clear(Node *node)
	{
		if(node != NULL)
		{
			clear(node->left);
			clear(node->right);
			delete node;
		}
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
 	int maxHight()
 	{
 		return maxHightHelper(head);
 	}
    int maxHightHelper(Node *node)
    {
    	if(node == NULL)
    		return 0;
    	return (1+max(maxHightHelper(node->left),maxHightHelper(node->right)));
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
	Tree *tt = new Tree();
	t.deepCopy(tt);
	cout <<"Printing copy" << endl;
	tt->print();
	cout << "adding new items" << endl;
	tt->add(3);
	tt->add(7);
	tt->print();
	cout<<"Max hight is "<<t.maxHight() << endl;
	cout << "Printing original" << endl;
	t.print();
	return 0;
}