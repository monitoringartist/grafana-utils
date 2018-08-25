# multiprocess Lambda function to backup all Grafana dashboards to S3 bucket
# perf test: 500 dashboards, <100 secs, ~1GB RAM

import datetime, boto3
from botocore.vendored import requests
from multiprocessing import Process, Pipe

config = {
    'domain.com': {
      'url': 'https://domain.com',
      'key': '=grafana-api-key-with-read-permissions-for-all-dashboards=',
    },
}

def backup_dashboard(d, path, conf, headers, s3):
        if 'folderTitle' in d:
             path = path + d['folderTitle'].replace(' ', '-').replace(':', '').replace('/', '-').replace('\'', '') + '/'
        path = path + d['uid'] + '___' + d['title'].replace(' ', '-').replace(':', '').replace('/', '-').replace('\'', '') + '.json'
        print path
        r = requests.get('%s/api/dashboards/uid/%s' % (conf['url'], d['uid']), headers=headers)
        object = s3.Object('s3-backup', 'backup-folder/' + path)
        object.put(Body=r.text.encode('utf-8'))

def lambda_handler(event, context):
    global config
    conf = config[event['config']]
    dt = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '/'
    headers = {'Authorization': 'Bearer %s' % (conf['key'])}
    r = requests.get('%s/api/search?type=dash-db&query=&' % (conf['url']), headers=headers)
    s3 = boto3.resource('s3')
    parent_connections = []
    processes = []
    for d in r.json():
        parent_conn, child_conn = Pipe()
        parent_connections.append(parent_conn)
        process = Process(target=backup_dashboard, args=(d, event['config'] + '/' + dt, conf, headers, s3,))
        processes.append(process)
    for process in processes:
        process.start()
    for process in processes:
        process.join()
