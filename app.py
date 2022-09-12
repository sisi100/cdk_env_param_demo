import aws_cdk as cdk

import constants
from deployment import DemoStage

env = cdk.Environment(account=constants.ACCOUNT, region=constants.REGION)
app = cdk.App()
DemoStage(app, constants.APP_NAME, env=env)
app.synth()
