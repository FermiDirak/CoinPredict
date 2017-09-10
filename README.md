# CoinPredict
Uses Tensorflow to predict trends in cryptocurrencies on the GDAX exchange


cache: contains preprocessed datasets
config: contains configuration settings for poject
data: contains raw file data
data_extraction: uses the GDAX exchange to extract exchange rates data
doc: contains documentation for the project
feature_extraction: extracts feature data from raw data
graphs: contains graphs created from analysis
model_creation: creates models to predict with
profiling: contains scripts used to profile and benchmark
reports: output reports on performance and benchmarks
tests: Unit tests for project
README: Notes to orient project newcomers
TODO: list of future improvements and bugfixes


Before you can use this application, you must first set up a postgresql server
`CREATE DATABASE CoinPredict`