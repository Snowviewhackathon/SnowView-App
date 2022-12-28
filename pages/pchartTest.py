import pandas as pd
import io, requests
import plotly.express as px

df = pd.read_csv(
    io.StringIO(
        requests.get(
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
        ).text
    )
)
df["Date"] = pd.to_datetime(df["date"])
df["Country"] = df["location"]
df["7day_rolling_avg"] = df["daily_people_vaccinated_per_hundred"]

Date = df[df.Country == "India"].Date
New_cases = df[df.Country == "India"]["7day_rolling_avg"]

px.line(df, x=Date, y=New_cases, title="India Daily New Covid Cases").update_layout(
    xaxis_title="Date", yaxis_title="7 day avg"
)
