
# general
import re
import os

# Spark related configuratio
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.1-bin-hadoop2.7"
import findspark
findspark.init()

# Pyspark imports
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as func
sc = SparkSession.builder.master("local[*]").getOrCreate()

# Standard data analysis code
import pandas as pd
import numpy as np
import fire

# NLP related data 
import gensim
from gensim.models.coherencemodel import CoherenceModel
from gensim.test.utils import datapath
from gensim import corpora, models

# Module imports
from configs import COLS,politicians,RETWEET_COLS

from lda_build import lda_maker

class Controller(object):
    def lda(self,sample_size=100):
        print("Wait a moment this might take some time to run...")
        dataframe = lda_maker(sc)
        print(dataframe.show())




