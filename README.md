# Numerical Semigroups Python's Functions
We were looking a speedy way for building a numerical semigroup (NS). Finally, we got this, helped by itertools package in Python.

We are spanish speakers, so the assigment is in spanish as well. However, here's a brief description of each function.
We are sorry, but remeber, code speaks itself.

Using geners of an numerical semigroups, we defined using itertools the following functions:
- EsSN(geners) -> Verify if geners form a numerical semigroup.
- PerteSN(x,geners) -> Verify if x belongs to the NS formed by geners.
- GenInfinitoSN(geners,ini=0) -> Returns an infinite NS elements' iterator started in ini.
- ConjApery(geners,verb=False) -> Return a Apery(geners,min(geners))'s list of the NS formed by geners.
- GenSNMaxApery(geners,verb=False) -> returns an NS's iterator up to max(Apery(geners,min(geners))).
- GeneradorSN(geners,verb=False) -> Verify if geners forms a NS. If so, returns an NS's iterator up to max(Apery(geners,min(geners))). Otherwise, returns an error.
- ListaSN(geners,verb=False) -> Verify if geners forms a NS. If so, returns a NS's list up to max(Apery(geners,min(geners))). Otherwise, returns an error.

If verb = True, it returns information about the NS.

Authors:  
 - Rincón, Jose
 - Sánchez, Adrián
