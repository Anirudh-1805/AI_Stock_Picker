import warnings
from datetime import datetime

from .crew import StockPicker
from dotenv import load_dotenv
load_dotenv(override=True)
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run(sectorinput):
    """
    Run the research crew.
    """
    inputs = {
        'sector': sectorinput,
        "current_date": str(datetime.now())
    }

    # Create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)
