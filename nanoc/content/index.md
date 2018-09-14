---
title: DCP Status
---
# Data Coordination Platform: Status

| System | Stage | Build Status | System Availability |
|-----|--------|----------------|---------------------|
| DCP | `integration` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/dcp/integration.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/commits/integration) |  |
| | `staging`| [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/dcp/staging.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/commits/staging) | |
| | `prod`| [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/dcp/prod.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/dcp/commits/prod) | |
| Upload | `dev` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/upload-service/master.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/upload-service/commits/master) | ![](https://status.dev.data.humancellatlas.org/service/upload-health-check-dev.svg) |
| | `integration` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/upload-service/integration.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/upload-service/commits/integration) | ![](https://status.dev.data.humancellatlas.org/service/upload-health-check-integration.svg) |
| | `staging` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/upload-service/staging.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/upload-service/commits/staging) | ![](https://status.dev.data.humancellatlas.org/service/upload-health-check-staging.svg) |
| | `prod` | [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/upload-service/prod.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/upload-service/commits/prod) | ![](https://status.data.humancellatlas.org/service/upload-health-check-prod.svg) |
| Data Storage | `dev` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/data-store/master.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/data-store/commits/master) | ![](https://status.dev.data.humancellatlas.org/service/dss-health-check-dev.svg) |
| | `integration` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/data-store/integration.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/data-store/commits/integration) | ![](https://status.dev.data.humancellatlas.org/service/dss-health-check-integration.svg) |
| | `staging` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/data-store/staging.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/data-store/commits/staging) | ![](https://status.dev.data.humancellatlas.org/service/dss-health-check-staging.svg) |
| | `prod` | [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/data-store/prod.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/data-store/commits/prod) | ![](https://status.data.humancellatlas.org/service/dss-health-check-prod.svg) |
| Lira | `dev` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/lira/master.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/lira/commits/master) | ![](https://status.dev.data.humancellatlas.org/service/analysis-health-check-dev.svg) |
| | `integration` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/lira/integration.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/lira/commits/integration) | ![](https://status.dev.data.humancellatlas.org/service/analysis-health-check-integration.svg) |
| | `staging` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/lira/staging.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/lira/commits/staging) | ![](https://status.dev.data.humancellatlas.org/service/analysis-health-check-staging.svg) |
| | `prod` | [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/lira/prod.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/lira/commits/prod) | ![](https://status.data.humancellatlas.org/service/analysis-health-check-prod.svg) |
| Logs | `hca` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/logs/master.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/logs/commits/master) | ![](https://status.dev.data.humancellatlas.org/service/logs-health-check-dev.svg) |
| | `hca-prod` | [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/logs/master.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/logs/commits/master) | ![](https://status.data.humancellatlas.org/service/logs-health-check-prod.svg) |
| Metrics | `hca` | [![](https://status.dev.data.humancellatlas.org/build/HumanCellAtlas/metrics/master.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/metrics/commits/master) | ![](https://status.dev.data.humancellatlas.org/service/metrics-health-check-dev.svg) |
| | `hca-prod` | [![](https://status.data.humancellatlas.org/build/HumanCellAtlas/metrics/master.svg)](https://allspark.data.humancellatlas.org/HumanCellAtlas/metrics/commits/master) | ![](https://status.data.humancellatlas.org/service/metrics-health-check-prod.svg) |

*Last updated at <span id="timestamp">_</span>. Refreshing in two minutes...*

<script type="text/javascript">
var setDatetime = function() {
    var n = new Date().toISOString()
    document.getElementById("timestamp").innerText = n;
};

window.onload = setDatetime;

setInterval(function() {
        window.location.reload();
    },
    2*60000
);
</script>

