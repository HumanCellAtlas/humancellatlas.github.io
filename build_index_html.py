import argparse
import json
import random
import sys
from jinja2 import Template

random.seed(0)

status_apis = {
    'dev': 'https://status.dev.data.humancellatlas.org',
    'integration': 'https://status.dev.data.humancellatlas.org',
    'staging': 'https://status.dev.data.humancellatlas.org',
    'prod': 'https://status.data.humancellatlas.org',
}

build_servers = {
    'dev': 'https://allspark.dev.data.humancellatlas.org',
    'integration': 'https://allspark.dev.data.humancellatlas.org',
    'staging': 'https://allspark.dev.data.humancellatlas.org',
    'prod': 'https://allspark-prod.data.humancellatlas.org',
}

NAME = sys.argv[0].split('/')[-1]
CLI = argparse.ArgumentParser(
    description=f"`{NAME}` is a tool for generating HCA DCP status pages"
)
CLI.add_argument(
    '--environment-filter',
    dest="environment_filter",
    type=str,
    required=False,
    help="Filter by deployment environment"
)
CLI.add_argument(
    '--project-filter',
    dest="project_filter",
    type=str,
    required=False,
    help="Filter by project's repo short link"
)


if __name__ == '__main__':
    options = CLI.parse_args(sys.argv[1:])

    with open('config.json', 'r') as fh:
        entries = json.load(fh)

    with open('template.html', 'r') as fh:
        template_str = fh.read()

    headers = [
        dict(cells=('System Name', 'Environment', 'Build Status', 'Status', 'Availability (30 day)', 'Metrics'))
    ]
    environments = []
    for s in entries['systems']:
        environments += [
            dict(
                name=s['system_name'],
                repo=s['repo'],
                env=e['name'],
                ci_cd_url=f"{build_servers[e['name']]}/{s['group']}/{s['repo']}/commits/{e['branch']}",
                build_status_image=f"{status_apis[e['name']]}/build/{s['group']}/{s['repo']}/{e['branch']}.svg",
                health_check_endpoint=e['health_check_endpoint'],
                metrics_url=e.get('metrics_url'),
                system_status_image=f"{status_apis[e['name']]}/service/{e['health_check_id']}.svg",
                availability_image=f"{status_apis[e['name']]}/availability/{e['health_check_id']}.svg",
                metrics_emoji=random.choice(['📈', '📉', '📊']) if e.get('metrics_url') else '❌'
            ) for e in s['environments']
        ]

    title_parts = []
    if options.project_filter:
        environments = [d for d in environments if d['repo'] == options.project_filter]
        title_parts.append(f"{options.project_filter} project")

    if options.environment_filter:
        environments = [d for d in environments if d['env'] == options.environment_filter]
        title_parts.append(f"{options.environment_filter} environment")

    template = Template(template_str)
    print(
        template.render(
            title=', '.join(title_parts) if len(title_parts) else 'all projects and environments',
            headers=headers, deployments=environments
        )
    )


