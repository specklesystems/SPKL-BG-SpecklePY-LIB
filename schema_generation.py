import json
from bg_specklepy.analysis_column_eccentricity import FunctionInputs


if __name__ == "__main__":
    print(json.dumps(FunctionInputs.schema()))