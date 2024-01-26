### az ml compute

```shell
az ml compute connect-ssh --name ci1 --resource-group std --workspace-name mle-cert --private-key-file-path sshkey.pem
```

```shell
az ml compute create --file compute.yml --resource-group std --workspace-name mle-cert
```

```shell
az ml compute create --name nc6-cluster --size Standard_NC6 --min-instances 0 --max-instances 5 --type AmlCompute --resource-group std --workspace-name mle-cert
```

```shell
az ml compute create --name nc6-cluster --type ComputeInstance --resource-group std --workspace-name mle-cert
```

```shell
az ml compute create -n nc6-inst-dereo -t ComputeInstance -g std -w mle-cert
```

```shell
az ml compute delete -n nc6-inst-dereo -g std -w mle-cert
```

```shell
az ml compute list -w mle-cert -g std
```

```shell
az ml compute list-sizes -w mle-cert -g std -t AmlCompute/ComputeInstance
```

```shell
az ml compute attach -w mle-cert -g std -n aml-cluster
```

```shell
az ml compute show -n aml-cluster -w mle-cert
```

```shell
az ml compute start/stop -n aml-cluster -w mle-cert
```

```shell
az ml compute detach -w mle-cert -g std -n aml-cluster
```

```shell
az ml compute update -n nc6-cluster-dereo --min-instances 1 -w mle-cert --tags type=test
```