import dlt

@dlt.table
def demo_table_dab_new():
    return spark.range(10)