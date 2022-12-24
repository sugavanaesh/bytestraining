#include<stdio.h>
int main(){
    int data=5;
    //bit = 3 we are checking the 3rd bit
    //to check
    if((data &(1<<3))==0)
    printf("OFF");
    else
    printf("ON")

    //ToTurnOn
    data = data | (1<<3)
    printf("%d",data);

    //ToTurnOff
    data = data & (~(1<<3))
    printf("%d",data);

    //ToToggle
    data = data ^ (1<<3)
}