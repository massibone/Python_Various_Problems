import polars as pl

# Definiamo la query senza eseguirla (Lazy)
query = (
    pl.scan_csv("dati.csv")
    .filter(pl.col("età") > 30)
    .select(["id", "nome", "età", "città", "reddito"])
    .join(pl.scan_csv("dati_altro.csv"), on="id")
    .group_by("città")
    .agg([
        pl.col("età").mean().alias("età_media"),
        pl.col("reddito").sum().alias("reddito_totale")
    ])
)
