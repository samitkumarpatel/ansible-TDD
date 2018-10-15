import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    
    m = host.file('/poc/poc.sh')
    assert m.exists
    assert m.user == 'root'

    service = host.file('/etc/systemd/system/poc.service')
    assert service.exists
    assert m.user == 'root'

def test_systemd_service(host):
    s = host.service('poc.service')
    assert s.is_enabled
    assert s.is_running
