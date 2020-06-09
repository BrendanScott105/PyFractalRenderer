# On the precision code
The precision version uses arbitrary precision libraries    
This being the case, it is very slow and not optimized in any way past the original optimizations in the base program file    
It also has issues saving images when built into an executable, and since I'm facing issues right now, it is not supported

You can use it and attempt to fix it, by all means, but it's not really worth it when Kalles Fraktaler, a free program, exists already which implements pertubation theory and series approximation.

# On the Periodicity checking code
The peridoicity checking code checks the previous 2 values of the complex number Z if I'm remembering correctly, and does not save too much time, in fact, it might take longer.

# On the fast code
The faster code utilizes multiplication and addition in the formulas to utilize the faster calculation methods over exponentiation    
However, it does this through more variables, and as such, uses more memory, not making any drastic time saves

# Extra
I also at one point had code that was about experimental as it could get, and would attempt to render fractals using a box filling method, where a box outline would be drawn, if it's outline was one color, it would get filled in, while if it was not uniform, it would be split into four new boxes. I trashed it because it didn't work, but I may [that's a big may] attempt to reimplement it at some point.
