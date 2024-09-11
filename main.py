from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap, ggtitle
from plotnine.data import mtcars
import datetime

plot = (ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
        + geom_point()
        + stat_smooth(method="lm")
        + facet_wrap("gear")
        + ggtitle(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        )

plot.save(filename="plotnine-save.jpg", format="jpg")
