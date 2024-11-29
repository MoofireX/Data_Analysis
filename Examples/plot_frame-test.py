import Data_Analysis as data
import pandas as pd
from matplotlib import pyplot as plt


frame = pd.DataFrame({"Jets" : [100],"Tanks" : [200], "Ships" : [300],"Oompa Loompa Warriors" : [1000]})

data.plot_frame(frame)
