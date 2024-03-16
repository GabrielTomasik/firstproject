df_wedding = df.loc[(df["Event"] == "Urodziny")].copy()


date_this_year = df_wedding["Day"].astype(str) + "/" + df_wedding["Month"].astype(str) + "/" + year_today
df_wedding["Date"] = pd.to_datetime(date_this_year, dayfirst = True)

df_wedding["Days Untill"] = (df_wedding["Date"] - date_today).dt.days.astype(int)
df_wedding["Days Untill"] = df_wedding["Days Untill"].apply(lambda x: (-x) + 365 if x < 0 else x)
df_wedding


df_wedding["Years Old"] = dt.date.today().year - df_wedding["Year"]
df_wedding