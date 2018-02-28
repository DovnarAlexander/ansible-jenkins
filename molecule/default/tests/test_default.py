import testinfra.utils.ansible_runner

import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    packages = [
        "tar",
        "git",
        "unzip"
    ]
    for package in packages:
        p = host.package(package)
        assert p.is_installed


def test_correct_jenkins_version_installed(host):
    target_version = os.environ['jenkins_test_version']
    jenkins = 'http://127.0.0.1:8080'
    uri = 'login?from=%2F'
    command = "curl '"+jenkins+'/'+uri+"'"
    command += "|egrep 'Jenkins ver.+<.a' -o"
    o = host.run(command)
    assert target_version in o.stdout


def test_corrent_jenkins_plugin_installed(host):
    target_plugin_list = [
        'git',
        'workflow-aggregator',
        'jobConfigHistory',
        'ssh',
        'ssh-slaves'
    ]
    jenkins = 'http://127.0.0.1:8080'
    uri = 'pluginManager/api/xml'
    request = 'depth=1&xpath=/*/*/shortName&wrapper=plugins'
    web_request = uri + '?' + request
    command = "curl -u jenkins:jenkins '"+jenkins+'/'+web_request+"'"
    command += "| grep -o '"
    for plugin in target_plugin_list:
        com = command + plugin + "'"
        o = host.run(com)
        assert plugin in o.stdout
