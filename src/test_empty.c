


#include <stdio.h>
#include <stdint.h>
#include <x86intrin.h>


unsigned int junk=0;

int main(){
    uint64_t t0, t1, i;

    for (i = 0; i < 100; i++){
        t0 = _rdtscp(&junk);
        asm volatile(
        );
        t1 = _rdtscp(&junk);
        
        printf("%ld\n", t1-t0);
    }
}
