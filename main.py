import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df_ = pd.read_excel(r'C:\Users\ap\Desktop\miuul\PYTHON\gezinomi_tanıtım\miuul_gezinomi.xlsx')
df = df_.copy()
df.info()
df.shape
df.columns
df.head()

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()
df["ConceptName"].nunique()
df["ConceptName"].value_counts()
df.groupby("SaleCityName").agg({"Price":"sum"})
df.groupby("ConceptName").agg({"Price":"sum"})
df.groupby("SaleCityName").agg({"Price":"mean"})
df.groupby(["SaleCityName","ConceptName"]).agg({"Price":"mean"})

bins=[-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"]= pd.cut(df["SaleCheckInDayDiff"],bins, labels=labels)
df.head()

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price":"mean"}).sort_values("Price", ascending=False)
agg_df.reset_index(inplace=True)

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=['D', 'C','B','A'])
agg_df.groupby("SEGMENT").agg({"Price" : ["mean","max","sum"]})

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"]==new_user]

new_user2 = "GIRNE_YARIM PANSIYON_LOW"
agg_df[agg_df["sales_level_based"]==new_user2]