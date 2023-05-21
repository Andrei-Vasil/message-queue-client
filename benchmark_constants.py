import datetime

BENCHMARK_ID = 1

BENCHMARK_CODING_LANGUAGES = ["rust", "cpp", "python-async", "python-multithreaded"]
BENCHMARK_CODING_LANGUAGE = "python"
assert BENCHMARK_CODING_LANGUAGE in BENCHMARK_CODING_LANGUAGES

BENCHMARK_FILE = f'{datetime.date.today()}-{BENCHMARK_ID}-{BENCHMARK_CODING_LANGUAGE}.csv'
