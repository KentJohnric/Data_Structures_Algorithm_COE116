#include <iostream>

using namespace std;

struct Node
{
    int age;
    Node *link;
};

void printList(Node *hd, Node *cr)
{
    cr=hd;
    while(cr!=NULL)
    {
        cout<<cr->age<<endl;
        cr=cr->link;
    }
}

int main()
{
    Node *head, *current;
    int ctr=1;
    head=new Node;
    current=head;
    bool frog=true;
    char choice;
    do
    {
        cout<<"Enter your age: ";
        cin>>current->age;

        cout<<"Do you want to create another node? (y/n)";
        cin>>choice;

        if (choice=='n')
        {
            current->link=NULL;
            frog=false;
        }
        else
        {
            current->link=new Node;
            current=current->link;
        }
       
		
    }while(frog);
    printList(head,current);
    return 0;
}

