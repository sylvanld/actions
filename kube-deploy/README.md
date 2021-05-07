# Deploy to Kubernetes

*This action aims to quickly deploy applications with kubernetes.*

## Usage

For example, to apply kubernetes deployment described in `deployment.yml` file to your cluster, use:

```yaml
- uses: sylvanld/actions/kube-deploy
  with:
    kubectl_version: v1.21.0
    kube_config: ${{secrets.KUBERNETES_CONFIG}}
    deployment: deployment.yml
```

**with:**

|parameter|description|optional|default|
|-|-|-|-|
|**kube_config**|Multiline string containing configuration to access your cluster (usually located in ~/.kube/config)|no|-|
|**kubectl_version**|Version of kubernetes used to send apply commands to your cluster|yes|latest stable|
|**deployment**|Path to the file describing Deployments/Services/Ingresses/... |yes|`deployment.yml`|

## Environment variables substitution

For convenience you can use the following environment variables in your kubernetes deployment manifest.

**DEPLOYED_VERSION**: Tag associated to the current branch. (without ` refs/tags` prefix)

> :warning: Be careful as this is **only suitable for tag branches**. (i.e:  on release, or when manually creating tags)
