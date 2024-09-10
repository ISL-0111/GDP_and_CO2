import pandas as pd
import numpy as np
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

wdi_subset = wdi[['Country Name', 'Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)']]

wdi_subset["Log GDP Per Capita"] = np.log(wdi_subset["GDP per capita (constant 2010 US$)"])

my_chart = (
    so.Plot(
        wdi_subset, x="Log GDP Per Capita", y="Mortality rate, infant (per 1,000 live births)"
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Infant Mortality Rate")
    .theme({**style.library["seaborn-v0_8-whitegrid"]})
)

my_chart
