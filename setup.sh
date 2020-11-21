python -m spacy download en_core_web_sm
python -m spacy download en_core_web_sm
apt-get update
apt-get install openjdk-8-jdk-headless -qq > /dev/null --fix-missing
wget https://mirrors.estointernet.in/apache/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
tar xvf spark-3.0.1-bin-hadoop2.7.tgz
pip install -q findspark
pip install pyLDAvis textacy -qq > /dev/null