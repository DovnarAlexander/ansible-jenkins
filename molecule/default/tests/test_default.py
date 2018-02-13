import testinfra.utils.ansible_runner

import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    packages = [
        "tar"
    ]
    for package in packages:
        p = host.package(package)
        assert p.is_installed


def test_java_present_in_path(host):
    assert host.exists("java")


def test_correct_java_version_installed(host):
    major = os.environ['java_major']
    minor = os.environ['java_minor']
    if major == '9':
        version = "\"%s.0.%s\"" % (major, minor)
    else:
        version = "\"1.%s.0_%s\"" % (major, minor)
    o = host.run("java -version")
    assert version in o.stderr.split()


def test_correct_javahome_set(host):
    major = os.environ['java_major']
    minor = os.environ['java_minor']
    if major == '9':
        home = "/opt/java/jdk-%s.0.%s" % (major, minor)
    else:
        home = "/opt/java/jdk1.%s.0_%s" % (major, minor)
    o = host.run(". /etc/environment && echo $JAVA_HOME")
    assert home in o.stdout.split()
