import os
from bg_specklepy.analysis_column_eccentricity import (
    FunctionInputs,
    SpeckleProjectData,
    main,
)


def test_operations_column_offset_evaluation():
    speckle_project_data = SpeckleProjectData(
        projectId="9a9689bf01",
        modelId="231110ac11-institute-var-2-ifc.ifc",
        versionId="c13d21b3cf",
        speckleServerUrl="http://latest.speckle.systems",
    )
    function_inputs = FunctionInputs(tolerance=0.02, echoLevel=1, scaleSpheres=False)
    speckle_token = os.getenv("SPECKLE_TOKEN")
    main(
        speckle_project_data.json(by_alias=True),
        function_inputs.json(by_alias=True),
        speckle_token,
    )


if __name__ == ("__main__"):
    test_operations_column_offset_evaluation()
