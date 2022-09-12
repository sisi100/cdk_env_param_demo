import os

ENV_PARAM_A = os.getenv("ENV_PARAM_A")
ENV_PARAM_B = os.getenv("ENV_PARAM_B")


def handler(event, context):
    print(f"{ENV_PARAM_A}!{ENV_PARAM_B}!")
