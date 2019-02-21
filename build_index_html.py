import json
import random
import sys
from jinja2 import Template

status_apis = {
    'dev': 'https://status.dev.data.humancellatlas.org',
    'integration': 'https://status.dev.data.humancellatlas.org',
    'staging': 'https://status.dev.data.humancellatlas.org',
    'prod': 'https://status.data.humancellatlas.org'
}

build_servers = {
    'dev': 'https://allspark.dev.data.humancellatlas.org',
    'integration': 'https://allspark.dev.data.humancellatlas.org',
    'staging': 'https://allspark.dev.data.humancellatlas.org',
    'prod': 'https://allspark-prod.data.humancellatlas.org'
}


if __name__ == '__main__':
    env_filter = None if len(sys.argv) < 2 else sys.argv[1]
    with open('config.json', 'r') as fh:
        entries = json.load(fh)

    with open('template.html', 'r') as fh:
        template_str = fh.read()

    headers = [
        dict(cells=('System Name', 'Deployment Stage', 'Build Status', 'Status', 'Availability (30 day)', 'Metrics'))
    ]
    deployments = []
    for s in entries['systems']:
        deployments += [
            dict(
                name=s['system_name'],
                env=d['name'],
                ci_cd_url=f"{build_servers[d['name']]}/{s['group']}/{s['repo']}/commits/{d['branch']}",
                build_status_image=f"{status_apis[d['name']]}/build/{s['group']}/{s['repo']}/{d['branch']}.svg",
                health_check_endpoint=d['health_check_endpoint'],
                metrics_url=d.get('metrics_url'),
                system_status_image=f"{status_apis[d['name']]}/service/{d['health_check_id']}.svg",
                availability_image=f"{status_apis[d['name']]}/availability/{d['health_check_id']}.svg",
                metrics_emoji=random.choice(['📈', '📉', '📊']) if d.get('metrics_url') else '❌'
            ) for d in s['deployments']
        ]
    if env_filter:
        deployments = [d for d in deployments if d['env'] == env_filter]
    template = Template(template_str)
    print(template.render(headers=headers, deployments=deployments))


