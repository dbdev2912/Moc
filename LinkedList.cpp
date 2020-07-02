#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct LinkedList
{
    int DATA;
    struct LinkedList *NEXT;
};
typedef struct LinkedList *node;

node CreateNode(int value)
{
    node temp=(node)malloc(sizeof(struct LinkedList));
    temp->NEXT=NULL;
    temp->DATA=value;
    return temp;
}

node Add_head(node head, int value)
{
    node temp=CreateNode(value);
    if(head==NULL)
    {
        head=temp;
    }
    else
    {
        temp->NEXT=head;
        head=temp;
    }
    return head;
}

node Add_tail(node head, int value)
{
    if(head==NULL)
    {
        head=CreateNode(value);
    }
    else
    {
        node p=head;
        while(p->NEXT!=NULL)
            p=p->NEXT;
        p->NEXT=CreateNode(value);
    }
    return head;
}

node Pos_add(node head, int pos, int value)
{
    node temp=CreateNode(value);
    if(head==NULL or pos<=0)
        head=Add_head(head, value);
    else
    {
        int k=1;
        node p=head;
        while(p!=NULL and k!=pos)
        {
            k+=1;
            p=p->NEXT;
        }
        if(k!=pos)
        {
            head=Add_tail(head, value);
        }
        else
        {
            temp->NEXT=p->NEXT;
            p->NEXT=temp;
        }
        
    }
    return head;
}

node Del_head(node head)
{
    if(head==NULL)
        printf("There is nothing to be removed");
    else
    {
        head=head->NEXT;
    }
    return head;
}

node Del_tail(node head)
{
    if(head==NULL)
        printf("There is nothing to remove");
    else
    {
        node p = head;
        while(p->NEXT->NEXT!=NULL)
            p=p->NEXT;
        p->NEXT=p->NEXT->NEXT;
    }
    return head;
}

node Del_pos(node head, int pos)
{
    if(head==NULL)
        printf("There is nothing to remove");
    else
    {
        if(pos<=0)
        {
            head=Del_head(head);
        }
        else
        {
            int k=1;
            node p=head;
            while(p->NEXT->NEXT!=NULL and k!=pos)
            {
                k+=1;
                p=p->NEXT;
            }
            if(k!=pos)
            {
                head=Del_tail(head);
            }
            else
            {
                p->NEXT=p->NEXT->NEXT;
            }
            
        }
        
    }   
    return head;
}


void Travel(node head)
{
    node p=head;
    printf("LinkedList: ");
    while(p!=NULL)
    {
        printf("%5d", p->DATA);
        p=p->NEXT;
    }
    printf("\n\n");
}

/*--- Loại bỏ phần tử trùng lập ---*/
int chk_data_exists(node head, int data)
{
    node p=head;
    while(p!=NULL)
    {
        if(p->DATA==data)
            return true;
        p=p->NEXT;
    }
    return false;
}
node TRIM(node head)
{
    node p=head;
    node b;
    while(p!=NULL)
    {
        if(not chk_data_exists(b, p->DATA))
            b=Add_tail(b, p->DATA);
        p=p->NEXT;
    }
    return b;
}


/*--- Tìm độ dài danh sách ---*/

int LENGTH(node head)
{
    int length=0;
    node p=head;
    while(p!=NULL)
    {
        length+=1;
        p=p->NEXT;
    }
    return length;
}

/*--- Tìm MIN, MAX ---*/
int MIN(node head)
{
    node p=head;
    int min=p->DATA;
    while (p!=NULL)
    {
        if(p->DATA<=min)
        {
            min=p->DATA;
        }
        p=p->NEXT;
    }
    return min;
}

int MAX(node head)
{
    node p=head;
    int max=p->DATA;
    while(p!=NULL)
    {
        if(p->DATA>=max)
            max=p->DATA;
        p=p->NEXT;
    }
    return max;
}


/*--- Sắp xếp danh sách ---*/
node A_ORDER(node head)
{
    node p, b;
    for(p=head; p!=NULL; p=p->NEXT)
    {
        for(b=head; b!=NULL; b=b->NEXT)
        {
            if(p->DATA<b->DATA)
            {
                p->DATA+=b->DATA;
                b->DATA=p->DATA-b->DATA;
                p->DATA=p->DATA-b->DATA;
            }
        }
    }
    return head;
}

node D_ORDER(node head)
{
    node p, b;
    for(p=head; p!=NULL; p=p->NEXT)
    {
        for(b=head; b!=NULL; b=b->NEXT)
        {
            if(p->DATA>b->DATA)
            {
                p->DATA+=b->DATA;
                b->DATA=p->DATA-b->DATA;
                p->DATA=p->DATA-b->DATA;
            }
        }
    }
    return head;
}

/*--- Tìm số lớn thứ N trong danh sách ---*/

int Find_the_N_th(node head, int n)
{
    if(n>LENGTH(head) or n<=0)
        return -1;
    int i=0;
    node p=head; 
    
    p=D_ORDER(p);
    while(i<n-1)
    {
        p=p->NEXT;
        i+=1;
    }
    return p->DATA;
}

/*--- Chọn ra các node chứa data là bôi chung của head và tail,
                            bội chung nhỏ nhất(nếu có) sẽ được in 2 lần  ---*/

int GET_TAIL_VAL(node head)
{
    node p=head;
    while(p->NEXT!=NULL)
    {
        p=p->NEXT;
    }
    return p->DATA;
}

int find_Lcmd(int head, int tail)
{
    int Lcmd=(head>tail)?head:tail;
    while(Lcmd%head or Lcmd%tail) Lcmd++;
    return Lcmd;
}
int chk_cmds(int head, int tail, int num)
{
    if(num%tail==0 and num%head==0)
        return true;
    else
        return false;   
}

void CMDs(node head)
{
    node p=head;
    int h=p->DATA;
    int t=GET_TAIL_VAL(p);
    int Lcmd=find_Lcmd(h, t);
    while(p!=NULL)
    {
        if(chk_cmds(h, t, p->DATA))
        {
            if(p->DATA==Lcmd)
            {
                printf("%5d%5d", p->DATA, p->DATA);
            }
            else
            {
                printf("%5d", p->DATA);
            }           
        }
        p=p->NEXT;
    }
    putchar('\n');
}

void xoa_trung_lap(node head)
{
    head=TRIM(head);
    Travel(head);
}

/*====================== MAIN ===================*/
int main()
{
    srand(time(0));
    node head=NULL;
    node head_;
    for(int i=6; i>0; i--)
    {
        int n=rand()%100+20;
        head=Add_tail(head, n);
            n=rand()%100+20;
        head_=Add_tail(head_, n);
    }
    head=Pos_add(head, 5, 10);
    head=Pos_add(head, 5, 10);
    head=Pos_add(head, 4, 1000);
    head=Add_head(head, 2);
    head=Add_tail(head, 5);
    Travel(head);
    
    //===== DUNG MIN-MAX-LENGTH =====//
    printf("LIST's MIN: %5d\n", MIN(head));
    printf("LIST's MAX: %5d\n", MAX(head));
    printf("LIST's LENGTH: %5d\n", LENGTH(head));

    /* Dung ket hop */
   head=TRIM(head);
   printf("Trimmed ");
   Travel(head);
    /*--------------*/

    /*=== Tim boi chung cua head va tail, neu la bcnn thi in x2 ===*/
    head=TRIM(head);
    printf("\nThe common divisor(s) of head and tail: ");
    CMDs(head);


    /*=== Tim so lon thu n trong danh sach ===*/
    /* 
        int n;
        scanf("%d", &n); 
    */
    head=D_ORDER(head);
    printf("The %dth is: %5d\n", 5/* n */, Find_the_N_th(head, 5 /* n */));

    /*=== SAP XEP DANH SACH ===*/
    head=D_ORDER(head);
    printf("Descending: ");
    Travel(head);

    head=A_ORDER(head);
    printf("Ascending: ");
    Travel(head);
}