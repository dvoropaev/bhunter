#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
int N = 6;

struct checkDevidersData{
	unsigned long long int number;
	unsigned long long int a;
	unsigned long long int b;
	int *result;
};


void *checkDeviders(void *data){                                                 //------------?
	struct checkDevidersData *range = (struct checkDevidersData *) data;
	for(unsigned long long int i=range->a; i<range->b; i++){
		//printf("%llu %llu %llu\n", range->number, i, range->number%i);
		if(range->number%i == 0){
			//printf("devider: %llu\n", i);
			*(range->result)=0;
			return NULL;
		}
	}
	return NULL;
}

int isPrime(unsigned long long int number){
	int result = 1;
	unsigned long long int MAX = sqrtl(number);
	//printf("MAX = %llu\n", MAX);
	pthread_t *threads = (pthread_t*) malloc(N * sizeof(pthread_t)); 
	struct checkDevidersData *ranges = (struct checkDevidersData*) malloc(N * sizeof(struct checkDevidersData));
	for(int i = 0; i < N; i++){
		ranges[i].number=number; //-----------------------------------?
		ranges[i].a = 2 + i*(MAX/N+1);
		ranges[i].b = 2 + (i+1)*(MAX/N+1);
		ranges[i].result = &result;
		printf("new thread: %llu..%llu\n", ranges[i].a, ranges[i].b);
		pthread_create(&(threads[i]), NULL, checkDeviders, &ranges[i]);
	}
	
	for(int i = 0; i < N; i++)
		pthread_join(threads[i], NULL);
	free(threads);
	free(ranges);
	
	return result;
}


int main(){
	unsigned long long int number;
	struct timespec start, finish;
	double elapsed;
	while(1){
		scanf("%i", &N);
		scanf("%llu", &number);
		clock_gettime(CLOCK_MONOTONIC, &start);
		if(isPrime(number) == 1)
			printf("YES ");
		else
			printf("NO  ");
		clock_gettime(CLOCK_MONOTONIC, &finish);
		elapsed = (finish.tv_sec - start.tv_sec);
		elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0; //-------------?
		printf("(%f sec)\n\n", elapsed);
	}

	return 0;
}
