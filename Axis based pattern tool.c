#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//find absolute value of x
int x_val(int xpoint,int ypoint){
return(
sqrtf((xpoint-5)*(xpoint-5))
);
}

//find absolute value of y
int y_val(int xpoint,int ypoint){
return(
 sqrtf((ypoint-5)*(ypoint-5)));
}


//detect current quadrant and apply x reflection 
int horo_reflect(int xpoint,int ypoint){
if(xpoint<5){
  return(xpoint+(2*x_val(xpoint,ypoint)));
}
else{
  return(xpoint-(2*x_val(xpoint,ypoint)));
}
}

//detect current quadrant and apply y reflection 
int verti_reflect(int xpoint, int ypoint){
   if(ypoint<5){
     return(ypoint+(2*y_val(xpoint,ypoint)));
     }
   else{
   return(ypoint-(2*y_val(xpoint,ypoint)));
   }

}


int horo_translate(int xpoint, int shift_val){
if(shift_val<0){
  return xpoint+(shift_val*-1);
} 
else{
  return (xpoint-shift_val);
} 
}


int verti_translate(int ypoint, int shift_val){
  if(shift_val<0){
    return (ypoint+(shift_val*-1));
  }
  else{
    return ypoint-shift_val;
  }

}




int main(void) {

  
char x_y[11][11];
 //define the 4 quadrants of the cartesian plane



/*
*/

//---------------------create visual xy axis---------------
//define (x,0)
//for(int x=0;x<11;x++){
//if(x_y[5][x]!='0'){x_y[5][x]='-';}
//}

//define(0,y)
//for(int y=0;y<11;y++){
//if(x_y[y][5]!='0'){x_y[y][5]='|';}
//}

//x_y[5][5]='|';
//-----------------------------------------------------------

//fill in white space with spaces
for(int y=0;y<11;y++){
  for(int x=0;x<11;x++){
  //if(x_y[y][x]!='0'&&x_y[y][x]!='-'&&x_y[y][x]!='|')
  //   {x_y[y][x]=' ';}
  
  x_y[y][x]=' ';      }
  }




//fill in starting pattern.

for(int y=1,count=1;y<11;y++){
    for(int x=0; x<count;x++){x_y[y][x]='*';}
     

     if(count!=5){count+=1;}else{break;}
     }






//----------------------------reclectt---------------------
for(int y=0;y<11;y++){
  for(int x=0;x<11;x++){
     //reflect across y axis from left to right
    
      

     
    //horosontal tranlation demo--
    //if(x_y[y][x]=='*'){
    //  x_y[y][horo_translate(x,1)]='g';
    //}

    //vertical translation demo
    //if(x_y[y][x]=='*'){
    //   x_y[verti_translate(y,-1)][x]='t';
    // }

     
    //---------reflect across x and y axis, then quadrant reflect
    if(x_y[y][x]=='*'){
     x_y[y][horo_reflect(x,y)]='Q';
     x_y[verti_reflect(x,y)][x]='F';
     x_y[verti_reflect(x,y)][horo_reflect(x,y)]='t';



    }
     }

     
  }
//--------------------------------------------------------


//----------------------------standardize---------------------
//set reflection/shift pattern to '*', 

for(int y=0;y<11;y++){
  for(int x=0;x<11;x++){

   if(x_y[y][x]!='*'&&x_y[y][x]!=' '){
     x_y[y][x]='*';

   }
  }}

//--------------------------------------------------------


//----------------------------output---------------------
//output resulting graph, 
for(int y=0;y<11;y++){
  for(int x=0;x<11;x++){
    printf("%c",x_y[y][x]);
    if(x==10){printf("\n");}


  }
}
//--------------------------------------------------------

/*


  */
  return 0;
}