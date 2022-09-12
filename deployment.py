from aws_cdk import Aspects, Stack, Stage
from constructs import Construct

from sample_resources.infra import SampleResources


class DemoStage(Stage):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack = Stack(self, "SampleEnvStack")
        SampleResources(stack, "SampleEnv")
