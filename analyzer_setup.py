# analyzer_setup.py

from presidio_analyzer import AnalyzerEngine
from recognizers import get_custom_recognizers


def get_analyzer():
    analyzer = AnalyzerEngine()

    # Add custom recognizers
    for recognizer in get_custom_recognizers():
        analyzer.registry.add_recognizer(recognizer)

    return analyzer