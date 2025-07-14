from setuptools import setup, find_packages

setup(
    name="csv_processor",
    version="0.1",
    packages=find_packages(),  # найдет все подпакеты с __init__.py
    install_requires=['tabulate'],  # установит tabulate автоматически
)