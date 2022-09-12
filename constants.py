import os

import aws_cdk as cdk
from aws_cdk import aws_lambda

app = cdk.App()
env = app.node.try_get_context("env")
cdk_json_params = app.node.try_get_context(env)

# 環境共通の定数
APP_NAME = f"EnvParamDemo_{env}"
ACCOUNT = os.environ["CDK_DEFAULT_ACCOUNT"]
REGION = os.environ["CDK_DEFAULT_REGION"]

RUNTIME_PYTHON_VERSION: aws_lambda.Runtime = aws_lambda.Runtime.PYTHON_3_9
RUNTIME_ARCHITECTURE = aws_lambda.Architecture.ARM_64

# 環境毎の定数
ENV_PARAM_A = cdk_json_params["ENV_PARAM_A"]
ENV_PARAM_B = cdk_json_params["ENV_PARAM_B"]
