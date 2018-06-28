#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define SPLIT 1

typedef struct ace_lev {
  int ace_1[2];
  int ace_2[2];
  int ace_3[2];
  int ace_4[2];
} ace_lev;

void deal(int*,int*,int*,int*,int*);
static void add(int*,int*,int*,int*,int*);
int org[14] = {14,'A',2,3,4,5,6,7,8,9,10,'J','Q','K'};
int totalitarianism(int*,struct ace_lev*);
int hit(int*,int*,int*,int*,int*,struct ace_lev*);
void janub(struct ace_lev*,int*,int,int);
void mashriq(int*,struct ace_lev*);
main() {
  int i,j,temp,l,*p,*split,*diamond,*spade,*heart,*club; time_t t; 
  int state = -1,sigma = -1,pi = -1;
  ace_lev *bangladesh = malloc((unsigned) sizeof(ace_lev));
  ace_lev *myanmar = malloc((unsigned) sizeof(ace_lev));
  srand((unsigned) time(&t));
  p = (int*) malloc((unsigned) sizeof(int) * 3); p[0] = 2;
  split = (int*) malloc((unsigned) sizeof(int) * 3); split[0] = -1;
  diamond = (int*) malloc((unsigned) sizeof(int) * 14);
  spade = (int*) malloc((unsigned) sizeof(int) * 14);
  heart = (int*) malloc((unsigned) sizeof(int) * 14);
  club = (int*) malloc((unsigned) sizeof(int) * 14);
  for(i = 0; i < sizeof(org) / sizeof(int); i++) 
    spade[i] = club[i] = heart[i] = diamond[i] = org[i];
  deal(p,diamond,spade,club,heart);
  /*p[1] = 5;
    p[2] = 5; */

  j = l = 0;
  while((j < 21) || (l < 21)) {

    if(sigma != 1) {
      if(state != SPLIT) printf("Your cards:\n"); 
      else printf("Your first hand:\n");
      for(i = 1; i <= p[0]; i++) {
    if(p[i] == 65) printf("A\n"); else if(p[i] == 74) printf("J\n"); 
    else if(p[i] == 75) printf("K\n"); else if(p[i] == 81) printf("Q\n");
    else printf("%d\n",p[i]);
      }
    }

    if((p[1] == p[2]) && (p[0] == 2)) {
      printf("You have two of the same card. Would you like to split? (Y/N) ");
      temp = getchar();
      if((temp == 89) || (temp == 121)) { 
    puts("Splitting...");
    split[0] = 2;
    temp = p[2];
    deal(p,diamond,spade,club,heart);
    deal(split,diamond,spade,club,heart); 
    p[1] = split[1] = temp;
    state = SPLIT; 
    /*Makes new cards for both decks*/
    printf("Your first hand:\n"); 
    for(i = 1; i <= p[0]; i++) {
      if(p[i] == 65 || p[i] == 11 || p[i] == 1) printf("A\n"); 
      else if(p[i] == 74) printf("J\n"); 
      else if(p[i] == 75) printf("K\n"); 
      else if(p[i] == 81) printf("Q\n");
      else printf("%d\n",p[i]);
    }
      }
    }

    if(j == 0) j = totalitarianism(p,bangladesh);
    printf("Card total: %d\n",j);

    if((state == SPLIT) && (sigma != 1)) {
      printf("\nSecond hand:\n");
      for(i = 1; i <= split[0]; i++) {
    if(split[i] == 65) printf("A\n"); 
    else if(split[i] == 74) printf("J\n"); 
    else if(split[i] == 75) printf("K\n"); 
    else if(split[i] == 81) printf("Q\n");
    else printf("%d\n",split[i]);
      }
      l = totalitarianism(split,myanmar); 
      printf("Card total: %d\n",l);
    }
    
    if(pi != 1) {
      if(split[0] == -1) puts("Do you want to hit or hold? (1,2)");
      else puts("Do you want to hit or hold on your first hand? (1,2)");
      scanf("%d",&temp);
      if(temp == 1) j = hit(p,diamond,spade,club,heart,bangladesh);
      if(temp == 2) {
    //printf("Your final total: %d\n",j);
    pi = 1;
    printf("Your final total for your first hand: %d\n",j);
      }
    }
    
    if((state == SPLIT) && (sigma != 1)) {
      puts("Do you want to hit or hold on your second hand? (1,2)");
      scanf("%d",&temp);
      if(temp == 1) j = hit(split,diamond,spade,club,heart,myanmar);
      if(temp == 2) {
    //printf("Your final total: %d\n",l);
    sigma = 1;
    printf("Your final total for your second hand: %d\n",j);
      }
    }

    if(((sigma == 1) && (pi == 1)) || ((state != SPLIT) && (pi == 1))) {
      printf("\nFinal statistics:\n");
      printf("Your final total for your first hand: %d\n",j);
      if(state == 1) printf("Your final total for your second hand: %d\n",l);

      break;
    }
  }
  if((j == 21) && (p[0] == 2)) printf("Excellent! Blackjack!\n");
  if(j > 21) printf("You bust with a total of %d!",j);
  if(j == 21) printf("Congratulation! A winner is you!\n");
  free(diamond);
  free(spade);
  free(club);
  free(heart);
  free(p);
  free(split);
}

int hit(int* p,int* diamond,int* spade,int* club,int* heart,struct ace_lev* qwerty) {
  int q;
  add(p,diamond,spade,club,heart);
  int i = p[0];
  /*Print the card*/
  printf("New card: ");
  if(p[i] == 65) printf("A\n"); 
  else if(p[i] == 74) printf("J\n"); 
  else if(p[i] == 75) printf("K\n"); 
  else if(p[i] == 81) printf("Q\n");
  else printf("%d\n",p[i]);

  q = totalitarianism(p,qwerty);
  return q;
}

void deal(int* p,int* diamond,int* spade,int* club,int* heart) {
  int i,j,k;
  for(i = 1; i <= p[0]; i++) {
    j = rand() % 4 + 1;
    if(j == 1) {
      p[i] = diamond[(rand() % diamond[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == diamond[j]) break;
      for(k = j; k < diamond[0] - 1; k++) diamond[k] = diamond[k + 1];
      --diamond[0];
    }
    if(j == 2) {
      p[i] = spade[(rand() % spade[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == spade[j]) break;
      for(k = j; k < spade[0] - 1; k++) spade[k] = spade[k + 1];
      --spade[0];
    }
    if(j == 3) {
      p[i] = heart[(rand() % heart[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == heart[j]) break;
      for(k = j; k < heart[0] - 1; k++) heart[k] = heart[k + 1];
      --heart[0];
    }
    if(j == 4) {
      p[i] = club[(rand() % club[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == club[j]) break;
      for(k = j; k < club[0] - 1; k++) club[k] = club[k + 1];
      --club[0];
    }
  }
}

static void add(int* p,int* diamond,int* spade,int* club,int* heart) {
  int temp[10],i,j,k;
  for(i = 0; i < p[0]; i++) temp[i] = p[i];
  ++p[0];
  p = realloc(p,sizeof(int) * (1 + p[0]));
  i = p[0];
  j = rand() % 4 + 1;
    if(j == 1) {
      p[i] = diamond[(rand() % diamond[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == diamond[j]) break;
      for(k = j; k < diamond[0] - 1; k++) diamond[k] = diamond[k + 1];
      --diamond[0];
    }
    if(j == 2) {
      p[i] = spade[(rand() % spade[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == spade[j]) break;
      for(k = j; k < spade[0] - 1; k++) spade[k] = spade[k + 1];
      --spade[0];
    }
    if(j == 3) {
      p[i] = heart[(rand() % heart[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == heart[j]) break;
      for(k = j; k < heart[0] - 1; k++) heart[k] = heart[k + 1];
      --heart[0];
    }
    if(j == 4) {
      p[i] = club[(rand() % club[0]) + 1];
      for(j = 0; 1; j++) if(p[i] == club[j]) break;
      for(k = j; k < club[0] - 1; k++) club[k] = club[k + 1];
      --club[0];
    }
}

int totalitarianism(int* p,struct ace_lev* qwerty) {
  int i,j = 0,k;
  for(i = 1; i <= p[0]; i++) { 
    if((p[i] > 14) && (p[i] != 65)) j+= 10;
    else if(p[i] == 65) {
      puts("Do you want your ace to equal 1 or 11?");
      scanf("%d",&k);
      janub(qwerty,p,k,i);
      if(k == 1) j += 1; else j += 11;
    }
    else j+= p[i]; 
  }
  return j;
}

void janub(struct ace_lev* qwerty,int* p,int value,int location) {
  int i;
  for(i = 1; i <= p[0]; i++) {
    if(qwerty->ace_1[0] != 1 || qwerty->ace_1[0] != 11) {
      qwerty->ace_1[0] = value;
      qwerty->ace_1[1] = location;
    }
    else if(qwerty->ace_2[0] != 1 || qwerty->ace_2[0] != 11) {
      qwerty->ace_2[0] = value;
      qwerty->ace_2[1] = location;
    }
    else if(qwerty->ace_3[0] != 1 || qwerty->ace_3[0] != 11) {
      qwerty->ace_3[0] = value;
      qwerty->ace_3[1] = location;
    }
    else if(qwerty->ace_4[0] != 1 || qwerty->ace_4[0] != 11) {
      qwerty->ace_4[0] = value;
      qwerty->ace_4[1] = location;
    }
  }
  mashriq(p,qwerty);
}

void mashriq(int* p,struct ace_lev* qwerty) {
  if(qwerty->ace_1[0] == 1 || qwerty->ace_1[0] == 11)
    p[qwerty->ace_1[1]] = qwerty->ace_1[0];
  if(qwerty->ace_2[0] == 1 || qwerty->ace_2[0] == 11)
    p[qwerty->ace_2[1]] = qwerty->ace_2[0];
  if(qwerty->ace_3[0] == 1 || qwerty->ace_3[0] == 11)
    p[qwerty->ace_3[1]] = qwerty->ace_3[0];
  if(qwerty->ace_4[0] == 1 || qwerty->ace_4[0] == 11)
    p[qwerty->ace_4[1]] = qwerty->ace_4[0];
}
