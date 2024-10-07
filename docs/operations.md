# Betriebshandbuch

## Deployment

Es gibt GithubActions für das Deployment, die API-SPecification und die
PRs hier [ZAPPI-Docs](https://github.com/ZeitOnline/docs-zappi/actions/)
. Diese werden automatisch angestoßen beim Erstellen von PRs bzw beim
Merge oder Push in den master-Branch.

## Prozesssteuerung

Das Repo ist in zeit.web als submodule eingebunden. Wenn man die
API-Spezifikation ändern möchte, muss man einen eigenen PR in zeit.web
stellen und dort das Submodule updaten.

## Monitoring/Observability

-   [Dashboard](https://grafana.ops.zeit.de/d/6pGBoElMz/zappi?orgId=1&from=now-24h&to=now)
-   [Honeycomb](https://ui.honeycomb.io/zeit-online/datasets/www/result/8EnYuw8S38w)
    `service.name == fastly.zappi`
-   [Kibana](https://kibana.ops.zeit.de/app/r/s/GkTB1)
    `dataview=gke-main-production` und `kubernetes.labels.app == zappi`
