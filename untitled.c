/* ************************************************************************* */
/* Organizacion del Computador II                                            */
/*                                                                           */
/*   main: Archivo principal para la solucion del trabajo practico 2         */
/*                                                                           */
/* ************************************************************************* */

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>

int rolld8();
int rolld20();
int roll6d8();

int main(int argc, char* argv[]){

  FILE *pFile;
  pFile = fopen( "ConMenos5.txt", "a" );
  
  srand(time(NULL));
  for(int i =0; i<10000;i++){
    int at1,at2,at3,at4;
    int roll;
    int cantSmites = 0;
    if(rolld20()>10){
      at1=rolld8()+15;
      at1+=roll6d8();
      cantSmites++;
    }else{
      at1=0;
    }

    if(rolld20()>10){
      at2=rolld8()+15;
      if(cantSmites<2){
        at2+=roll6d8();
        cantSmites++;
      }
    }else{
      at2=0;
    }

    if(rolld20()>10){
      at3=rolld8()+15;
      if(cantSmites<2){
        at3+=roll6d8();
        cantSmites++;
      }
    }else{
      at3=0;
    }

    if(rolld20()>10){
      at4=rolld8()+15;
      if(cantSmites<2){
        at4+=roll6d8();
        cantSmites++;
      }
    }else{
      at4=0;
    }
    int dmg = at1+at2+at3+at4;
    fprintf(pFile,"%d\n",dmg);

  }
  fclose(pFile);
  return 0;
}

int rolld20(){
  return rand()%20 + 1;
}
int rolld8(){
  return rand()%8 + 1;

}

int roll6d8(){
  return rolld8() + rolld8() + rolld8() + rolld8() + rolld8() + rolld8();
}






