//Sardina, Kent Johnric M.
//Fulache, Joshua Ruel A.

#include <iostream>

using namespace std;

struct Node
{
	int num;
	Node *link;
};
struct Node *head;
void printList(Node *hd, Node *cr)
{
	cr = hd;
	while(cr != NULL)
	{
		cout << cr->num << endl;
	}
}
void insertF(Node *&head_,Node *curr)
{
	Node *newNode;
	newNode = new Node;
	cout << "Enter num: ";
	cin >> newNode->num;
	newNode->link = head_;
	head_ = newNode;
}
void insertL(Node *head_, Node *curr)
{
	Node *newNode;
	newNode = new Node;
	cout << "Enter num: ";
	cin >> newNode->num;
	while (curr != NULL)
	{
		curr = curr->link;
	}
	curr->link = newNode;
}
void insertPos(Node *head_, Node *curr)
{
	int pos;
	Node *newNode;
	newNode = new Node;
	cout << "Enter Position";
	cin >> pos;
	cout << "Enter num: ";
	cin >> newNode->num;

}
int main()
{
	Node *head, *current;
	int ctr = 1;
	head = new Node;
	current = head;
	bool choc = true;
	char choice;
	do
	{
		cout << "Enter number: ";
		cin >> current->num;

		cout << "Do you want to create another node? (y/n)";
		cin >> choice;

		if (choice == 'n')
		{
			current->link = NULL;
			choc = false;
		}
		else
		{
			current->link = new Node;
			current = current->link;
		}
	} while (choc);
	{
		printList(head, current);
		cin.ignore();
		return 0;
	}
	insertF(head, current);
	cin.ignore();
	insertL(head, current);
	cin.ignore();
	insertPos(head, current);
	cin.ignore();
}