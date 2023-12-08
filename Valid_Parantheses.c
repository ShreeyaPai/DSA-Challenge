 struct Stack
{
    char a[5000];
    int top;
};
typedef struct Stack stack;

void push(stack* s,char c)
{
    s->a[++s->top]=c;
}

char pop(stack*s)
{
    return s->a[s->top--];
}

bool isValid(char * s){
    char c,p;int flag=0;
    stack stk; stk.top=-1;
    while((c=*s++)!='\0')
    {
        if(c=='('||c=='['||c=='{')
        push(&stk,c);
        if(c==')'||c=='}'||c==']')
        {
            if(stk.top==-1){flag=1;break;}
            p=pop(&stk);
            switch(p)
    {
        case '(': if(c!=')') flag=1;break;
        case '{': if(c!='}') flag=1;break;
        case '[': if(c!=']') flag=1;break;
    }
        }
    }
    if (flag==1||stk.top!=-1) return false;
    return true;
}
