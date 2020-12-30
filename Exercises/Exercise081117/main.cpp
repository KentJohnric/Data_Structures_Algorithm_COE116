#include <iostream>

struct nodeType
{
    int age;
    nodeType *link;
};

void insert_info(nodeType*&, nodeType*);
void insert_back(nodeType*&, nodeType*);
void printList(nodeType*&, nodeType*);

int main()
{
    nodeType *head, *current;
    head = new nodeType;
    current = head;
    bool eoc = true;
    char choice;
    
    std::cout<<"//MAIN";
    do
    {
        std::cout<<"Enter your age: ";
        std::cin>>current->age;
        std::cout<<" "<<current<<std::endl;

        std::cout<<"Do you want to create another node(Y/N)? ";
        std::cin>>choice;

        if (choice == 'N' || choice == 'n')
        {
            current->link=NULL;
            eoc=false;
        }
        else
        {
            current->link=new nodeType;
            current=current->link;
        }


    }while(eoc);
    
    printList(head,current);
    std::cin.ignore();
    std::cin.get();

    insert_info(head, current);
    printList(head,current);
    std::cin.ignore();
    std::cin.get();

    insert_back(head, current);
    printList(head,current);
    std::cin.ignore();
    std::cin.get();

    return 0;
}

void insert_info(nodeType *&head_, nodeType *curr)
{
    nodeType *newNode;
    newNode = new nodeType;
    std::cout<<"//INSERT FIRST";
    std::cout<<"Enter num: ";
    std::cin>>newNode->age;
    newNode->link = head_;
    head_ = newNode;
}

void insert_back(nodeType *&head_, nodeType *curr)
{
    nodeType *newNode;
    newNode = new nodeType;
    curr = head_;
    std::cout<<"//INSERT BACK";
    std::cout<<"Enter num: ";
    std::cin>>newNode->age;
    
    bool eol = false;
    while(eol!=true)
    {
    	if(curr->link == NULL)
		{
			curr->link = newNode;
		 	eol = true; 
    	}
    	else
		{
         	curr=curr->link;
    	}
    }
    newNode->link = NULL;
}

void printList(nodeType *&head_, nodeType *curr)
{
    curr=head_;
    while(curr!=NULL)
    {
        std::cout<<curr->age<<" "<<curr<<std::endl;
        curr=curr->link;
    }
}
