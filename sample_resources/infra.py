import pathlib

from aws_cdk import aws_lambda
from constructs import Construct

import constants


class SampleResources(Construct):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id)

        aws_lambda.Function(
            self,
            "Function",
            code=aws_lambda.Code.from_asset(
                str(pathlib.Path(__file__).resolve().parent.joinpath("runtime")),
            ),
            runtime=constants.RUNTIME_PYTHON_VERSION,
            architecture=constants.RUNTIME_ARCHITECTURE,
            handler="index.handler",
            environment={
                "ENV_PARAM_A": constants.ENV_PARAM_A,
                "ENV_PARAM_A": constants.ENV_PARAM_B,
            },
        )
