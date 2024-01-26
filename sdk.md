```python
MLClient(
    credential: TokenCredential, # credencial a ser usada
    subscription_id: str | None = None, # subscription
    resource_group_name: str | None = None, # resource group
    workspace_name: str | None = None, # workspace
    registry_name: str | None = None, # registry
    **kwargs: Any
)
```

```python
AmlCompute(*,
    name: str, # nome do cluster
    description: str | None = None, # descrição do cluster
    size: str | None = None, # tamanho do cluster (ex.: STANDARD_DS11_V2)
    tags: dict | None = None, # dicionário contendo as tags
    ssh_public_access_enabled: bool | None = None, # indica se a porta ssh está fechada
    ssh_settings: AmlComputeSshSettings | None = None, # configurações de acesso ssh
    min_instances: int | None = None, # numero minimo de instancias
    max_instances: int | None = None,  # numero maximo de instancias
    network_settings: NetworkSettings | None = None, # configurações de rede do cluster
    idle_time_before_scale_down: int | None = None, # tempo até o cluster desligar automaticamente
    identity: IdentityConfiguration | None = None, # as identidades associadas com o cluster
    tier: str | None = None, # tier que pode ser Dedicated ou LowPriority
    enable_node_public_ip: bool = True, # liga ou desliga ips publicos
    **kwargs
)
```

```python
ComputeInstance(
    *,
    name: str,
    description: str | None = None,
    size: str | None = None,
    tags: dict | None = None,
    ssh_public_access_enabled: bool | None = None,
    create_on_behalf_of: AssignedUserConfiguration | None = None,
    network_settings: NetworkSettings | None = None,
    ssh_settings: ComputeInstanceSshSettings | None = None,
    schedules: ComputeSchedules | None = None,
    identity: IdentityConfiguration | None = None,
    idle_time_before_shutdown: str | None = None,
    idle_time_before_shutdown_minutes: int | None = None,
    setup_scripts: SetupScripts | None = None,
    enable_node_public_ip: bool = True,
    custom_applications: List[CustomApplications] | None = None,
    **kwargs
)
```