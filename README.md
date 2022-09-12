# cdk_env_param_demo

CDK/Pythonで環境毎に変数を変えるデモ

## deploy
```.py
# dev環境をdeploy
$ cdk deploy 'EnvParamDemo/*' --context env=dev

# prod環境をdeploy
$ cdk deploy 'EnvParamDemo/*' --context env=prod
```
