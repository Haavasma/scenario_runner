from setuptools import setup, find_packages

setup(
    name="scenario_runner",
    version="0.9.13",
    description="Scenario Runner",
    # include srunner and agents modules
    packages=find_packages(),
    # include scenario_runner.py
    py_modules=["scenario_runner", "agents", "srunner", "manual_control"],
    install_requires=[
        "py-trees==0.8.3",
        "networkx==2.2",
        "Shapely==1.7.1",
        "psutil",
        "xmlschema==1.0.18",
        "ephem",
        "tabulate",
        "opencv-python==4.2.0.32",
        "numpy>=1.21.0, <1.24.0",
        "matplotlib",
        "six",
        "simple-watchdog-timer",
        "carla==0.9.13",
    ],
)
