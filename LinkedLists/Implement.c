#include<stdio.h>
#include<stdlib.h>

struct node
{
    struct node* next;
    int data;
};

struct node* endptr;
struct node* head = NULL;


void append(int data)
{
    struct node* new = (struct node*)malloc(sizeof(struct node));
    new->data = data;
    new->next = NULL;

    if(head == NULL)
    {
        head = new;
        endptr = new;
    }
    else
    {
        endptr->next = new;
        endptr = new;
    }

    

    printf("appended %d \n", endptr->data);

}


int main()
{
    //endptr = (struct node*)malloc(sizeof(struct node));
    endptr = head;
    append(1);
    append(2);
    append(3);

    //struct node* traverse = (struct node*)malloc(sizeof(struct node));
    struct node* traverse = head;

    while(traverse != NULL)
    {
        
        printf("%d \n", traverse->data);
        traverse = traverse->next;        
    } 

    free(traverse);
}