import typer
from bg_specklepy.SpeckleServer.client import Client
from bg_specklepy.Operations.columnOffsetEvaluation import ColumnOffsetEvaluation
from specklepy.transports.memory import MemoryTransport
from specklepy.transports.server import ServerTransport
from specklepy.api import operations
from pydantic import BaseModel, ConfigDict
from stringcase import camelcase

# Example Model can be found here: https://speckle.xyz/streams/ff47530e95


class SpeckleProjectData(BaseModel):
    """Values of the project / model that triggered the run of this function."""

    project_id: str
    model_id: str
    version_id: str
    speckle_server_url: str

    model_config = ConfigDict(alias_generator=camelcase, protected_namespaces=())


class FunctionInputs(BaseModel):
    """
    These are function author defined values, automate will make sure to supply them.
    """

    tolerance: float
    echo_level: int
    scale_spheres: bool

    class Config:
        alias_generator = camelcase


def main(speckle_project_data: str, function_inputs: str, speckle_token: str):
    project_data = SpeckleProjectData.model_validate_json(speckle_project_data)
    inputs = FunctionInputs.model_validate_json(function_inputs)

    stream_id = project_data.project_id
    commit_id = project_data.version_id
    speckle_server = project_data.speckle_server_url

    # Initiating appropriate server objects
    client_obj = Client(speckle_server, speckle_token)
    commit = client_obj.commit.get(stream_id, commit_id)

    memory_transport = MemoryTransport()
    server_transport = ServerTransport(stream_id, client_obj)
    commit_data = operations.receive(
        commit.referencedObject, server_transport, memory_transport
    )

    # Define and run analysis
    evaluation = ColumnOffsetEvaluation(
        client_obj=client_obj,
        stream_id=stream_id,
        commit_object=commit,
        commit_data=commit_data,
        tolerance=inputs.tolerance,
        echo_level=inputs.echo_level,
        scale_spheres=inputs.scale_spheres,
    )
    evaluation.run()


if __name__ == "__main__":
    typer.run(main)
