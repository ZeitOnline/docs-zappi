# Betriebshandbuch

## Deployment

Erfolgt durch die Aktualisierung des Submodules in [zeit.web](https://github.com/ZeitOnline/zeit.web/blob/main/.gitmodules).
Der Deployment Prozess folgt ab da, dem regulären Deployment von zeit.web.

## Monitoring/Observability

- [Dashboard](https://grafana.ops.zeit.de/d/IesWjbTGz/friedbert-appserver?from=now-1h&to=now&timezone=browser)
- [Honeycomb](https://ui.honeycomb.io/zeit-online/environments/production/datasets/fastly.zappi)
    `service.name == fastly.zappi`
- [Kibana]([https://kibana.ops.zeit.de/app/r/s/GkTB1](https://ec58528dccc64561807e8a3c2dc88805.europe-west3.gcp.cloud.es.io/app/r/s/hDD2R))
    `dataview=gke-main-production-25-01` und `kubernetes.labels.app == zappi`
