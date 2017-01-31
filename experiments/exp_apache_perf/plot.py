import logging

import numpy as np
from pandas import Categorical

from core import prepare
from core import draw

# === helpers === #
BENCH_NAME = 'apache'
EXP_NAME = '%s_perf' % BENCH_NAME

# NOTE 1: since all compilers perform roughly the same, we leave gcc only for simplicity
def main(t="perf"):
    logging.info("Processing data")
    df = prepare.process_results(t)
    if t == "tput":
        prepare.reorder_compilers(df, t)
        plot = draw.LinePlotTput()
        plot.get_data(df, [])
        plot.build_plot(
            xlim=(0, 54),
            xticks=range(0, 60, 10),
            ylim=(0.42, 0.92),
            yticks=np.arange(0.1, 1, 0.1),
        )
        plot.save_plot("apache_%s.pdf" % t)

    else:
        logging.error("Unknown plot type")
        exit(-1)
