# %% Run profiler
!python -m cProfile -o profresult heat_main.py

# %%
import pstats
from pstats import SortKey

p = pstats.Stats("profresult")
p.strip_dirs().sort_stats(SortKey.TIME).print_stats(10)
# %%
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(10)
