# Betriebshandbuch

## Deployment

Erfolgt durch die Aktualisierung des Submodules in [zeit.web](https://github.com/ZeitOnline/zeit.web/blob/main/.gitmodules).
Der Deployment Prozess folgt ab da, dem regulären Deployment von zeit.web.

## Monitoring/Observability

- [Dashboard](https://grafana.ops.zeit.de/d/6pGBoElMz/zappi?orgId=1&from=now-24h&to=now)
- [Honeycomb](https://ui.honeycomb.io/zeit-online/environments/production/datasets/fastly.zappi)
    `service.name == fastly.zappi`
- [Kibana](https://kibana.ops.zeit.de/app/r/s/GkTB1)
    `dataview=gke-main-production` und `kubernetes.labels.app == zappi`
