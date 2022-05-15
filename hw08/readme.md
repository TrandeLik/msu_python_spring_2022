## Profiling results
![Simple students](simple_student_profiling.png)
![Slots students](slots_student_profiling.png)
![Students with weakrefs](weakrefs_student_profiling.png)
### Conclusions
1) Slots save memory compared to simple classes (only if amount of objects is high enough)
2) Usage of weakrefs can save memory, because we store only refs in cache, but in reality consumption of memory is higher