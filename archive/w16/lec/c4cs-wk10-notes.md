gprof
=====

 - What's profiling?
 - *Last* thing you do, useful 1% of the time, *very useful* for that 1%


## Build a Profiler

```
// Several takes on this primitive:

for ( ; i < (LONG_TIME/32); i++) {
  // Prevent the compiler from optimizing out empty loop
  asm("nop;");
}

// Goal: Build up something like this during lecture:
struct data {
  uint64_t hits;
  unsigned ticks_total;
  unsigned ticks_start;
};

void fn_enter(hack) {
  time_data[hack].hits++;
  time_data[hack].ticks_start = clock();
}

void fn_exit(hack) {
  time_data[hack].ticks_total += clock() - time_data[hack].ticks_start;
}

// at_exit(print_stats)
void print_stats(void) {
  int i;

  for (i=0; i < 5; i++) {
    printf("hack[%d]\thits %llu\tticks %u\ttime %lf\n",
        i,
        time_data[i].hits,
        time_data[i].ticks_total,
        ((double) time_data[i].ticks_total) / CLOCKS_PER_SEC);
  }
}
```

### How we get there

1. What information does a profiler need?

2. How can we get it?

3. Iterate

4. Improve, tricks like `at_exit`


### Run gprof on our program

 - Requires flag `-pg` at every step [compile, link]

 - A little fragile
   - Program must run to completion sucessfully
   - Not unlike our test example!
   - Can use objdump to find calls to `_mprofil` (or w/e)
   - [Extra time? Maybe show a SIGINT handler that still prints ours]

 - `gprof PROFILED_PROGRAM gmon.out`
   - Lotta output here, help parse it

