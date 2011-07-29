#include <stdio.h>

int main()
{
  float my_float;
  int my_int;
  int my_ch;

  my_float = 75.345;
  my_int = (int) my_float;
  my_ch = (int) my_float;
  printf ("Convert from float my_float=%f to my_int=%d and my_ch=%c\n", my_float, my_int, my_ch);

  my_int = 69;
  my_float = (float) my_int;
  my_ch = my_int;
  printf ("Convert from int my_int=%d to my_float=%f and my_ch=%c\n", my_int, my_float, my_ch);

  my_ch = '*';
  my_int = my_ch;
  my_float = (float) my_ch;
  printf ("Convert from int my_ch=%c to my_int=%d and my_float=%f\n", my_ch, my_int, my_float);
}
