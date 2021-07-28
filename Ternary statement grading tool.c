#include<stdio.h>

void check(int grade){
printf("\n%c\n",

//split grading scale into two, then 
//judge based on sub divisions.

(grade>70)
?
(grade >= 70 && grade <=79)?'c':((grade>=80 && grade <=89)?'B':'A')
:
(grade >= 70 && grade <=79)?'c':((grade>=65 && grade<=69)? 'd':'f') 
);


}

int main()
{
        int p, c, o;
        
        printf("Type your grade in Physics (whole number). \n");
        scanf("%d", &p);
        check(p);
        
        printf("Type your grade in Calculus (whole number). \n");
        scanf("%d", &c);
        check(c);
        
        printf("Type your grade in Organic Chemistry (whole number). \n");
        scanf("%d", &o);
        check(o);

return 0;
}
