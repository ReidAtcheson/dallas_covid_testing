import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import smooth


df=pd.read_csv("manually_tabulated_dallas_testing.csv",header=4)
df.set_index("date")

tests=df["tests"].values
cases=df["positives"].values


plt.plot(smooth.epi_smooth_dx(cases/tests),linewidth=4,color="orange")
plt.bar(range(0,len(cases)),cases/tests)
plt.title("Ratio of positive tests")
plt.ylabel("Positive ratio")
plt.xlabel("day")
plt.legend(["Trend","Raw data"])
plt.savefig("positive_ratio.svg")
plt.close()

plt.plot(smooth.epi_smooth_dx(cases),linewidth=4,color="orange")
plt.bar(range(0,len(cases)),cases)
plt.title("Cases per day")
plt.ylabel("cases")
plt.xlabel("day")
plt.legend(["Trend","Raw data"])
plt.savefig("cases_per_day.svg")
plt.close()

plt.plot(smooth.epi_smooth_dx(tests),linewidth=4,color="orange")
plt.bar(range(0,len(tests)),tests)
plt.title("Tests per day")
plt.ylabel("tests")
plt.xlabel("day")
plt.legend(["Trend","Raw data"])
plt.savefig("tests_per_day.svg")
plt.close()


