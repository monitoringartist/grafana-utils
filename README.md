[<img src="https://monitoringartist.github.io/managed-by-monitoringartist.png" alt="Managed by Monitoring Artist: DevOps / Docker / Kubernetes / AWS ECS / Zabbix / Zenoss / Terraform / Monitoring" align="right"/>](http://www.monitoringartist.com 'DevOps / Docker / Kubernetes / AWS ECS / Zabbix / Zenoss / Terraform / Monitoring')

# Grafana Dashboard Exporter/Importer

Export/import Grafana dashboards (Grafana 5+).

## Dashboard

![Grafana Dashboard Exporter/Importer](https://raw.githubusercontent.com/monitoringartist/grafana-dashboard-exporter/master/doc/grafana-dashboard-exporter-importer.png)

## Dashboard restore operation

Use [dashboard API](http://docs.grafana.org/http_api/dashboard/#create-update-dashboard) to restore dashboard. For example:
```
cat <exported-dashboard.json> | jq '. + {overwrite: true}' | curl -X POST \
-H "Content-Type: application/json" -H "Authorization: Bearer <api-key-with-write-permissions>" \
<grafana-uri>/api/dashboards/db -d @-
```

When importing dashboards for the first time reset the `id`:
```
cat <exported-dashboard.json> | jq '. * {overwrite: true, dashboard: {id: null}}' | curl -X POST \
-H "Content-Type: application/json" -H "Authorization: Bearer <api-key-with-write-permissions>" \
<grafana-uri>/api/dashboards/db -d @-
```

# Author

[Devops Monitoring Expert](http://www.jangaraj.com 'DevOps / Docker / Kubernetes / AWS ECS / Google GCP / Zabbix / Zenoss / Terraform / Monitoring'),
who loves monitoring systems and cutting/bleeding edge technologies: Docker,
Kubernetes, ECS, AWS, Google GCP, Terraform, Lambda, Zabbix, Grafana, Elasticsearch,
Kibana, Prometheus, Sysdig,...

Summary:
* 3000+ [GitHub](https://github.com/monitoringartist/) stars
* 20 000+ [Grafana dashboard](https://grafana.net/monitoringartist) downloads
* 1 000 000+ [Docker image](https://hub.docker.com/u/monitoringartist/) pulls

Professional devops / monitoring / consulting services:

[![Monitoring Artist](http://monitoringartist.com/img/github-monitoring-artist-logo.jpg)](http://www.monitoringartist.com 'DevOps / Docker / Kubernetes / AWS ECS / Google GCP / Zabbix / Zenoss / Terraform / Monitoring')
