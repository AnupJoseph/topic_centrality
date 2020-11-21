from configs import COLS, politicians, RETWEET_COLS
import os
from text_processing import processor
from pyspark.sql.types import StringType()


def lda_maker(sc):
    textProcessor = sc.udf(lambda string: processor(string), StringType())
    sc.udf.register("textProcessor", textProcessor)

    final_data = sc.read.format("csv").options(header='true', inferschema='true').load(
        os.path.realpath("../data/SenSanders/SenSanders_data.csv"))
    final_data = final_data.withColumn('clean_text', textProcessor('clean_text'))

    for politician in politicians[1:]:
        next_frame = sc.read.format("csv").options(header='true', inferschema='true').load(
            os.path.realpath(f"../data/{politician}/{politician}_data.csv"))
        next_frame = next_frame.withColumn('clean_text', textProcessor('clean_text'))
        final_data = final_data.union(next_frame)
    print("Set spark context and created a subset")
    return final_data