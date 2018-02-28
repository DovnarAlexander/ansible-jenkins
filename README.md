[![Build Status](https://img.shields.io/travis/fubarhouse/ansible-role-python/master.svg?style=for-the-badge)](https://travis-ci.org/DovnarAlexander/ansible-jenkins)
[![Ansible Galaxy](https://img.shields.io/ansible/role/24099.svg?style=for-the-badge)](https://galaxy.ansible.com/DovnarAlexander/jenkins)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://raw.githubusercontent.com/DovnarAlexander/jenkins/master/LICENSE)

DovnarAlexander/jenkins
=========

**[Ansible Galaxy DovnarAlexander/jenkins](https://galaxy.ansible.com/DovnarAlexander/jenkins)**

This role helps you to install any version of Jenkins (LTS and Not).
It manages:
- Jenkins users;
- Credentials (SSH including key generation, Secret Text and Username-Password);
- Installs plugins;
- Jenkins Slaves (JNLP and SSH);
- Some Jenkins main configuration (the main Hostname and Email).

Role Variables
--------------

### Jenkins Version

```yaml
# file: defaults/main.yml

# Do you want install Jenkins from stable rep or not
jenkins_stable: True

```

If you want to install non-LTS version - set it to False.

```yaml
# file: defaults/main.yml

# What version should be installed
jenkins_version: latest

```

If you want to install some specific version - input full version here (x.xx.x)

```yaml
# file: defaults/main.yml

# Do you want to updated the Jenkins (if older version has been already installed)
jenkins_update: False

```

If you do not want to update the version to the latest - set it to True.

### Jenkins Configuration

```yaml
# file: defaults/main.yml

# Jenkins HTTP port
jenkins_http_port: 8080

```

You can change the default HTTP port here.

```yaml
# file: defaults/main.yml

# Jenkins Home path
jenkins_home: /var/lib/jenkins

```

You can change default Jenkins Home path here.

```yaml
# file: defaults/main.yml

# Jenkins External Hostname for main configuration
jenkins_notification_hostname: 'http://{{ inventory_hostname }}:{{ jenkins_http_port }}/'

```

You can set external Jenkins Hostname here manually.

```yaml
# file: defaults/main.yml

# Jenkins EEmail for main configuration
jenkins_notification_email: 'admin@example.com'

```

You can set Jenkins Notification Email here.

### Jenkins Admin

```yaml
# file: defaults/main.yml

# Jenkins New Admin details
jenkins_admin:
  id: jenkins
  password: jenkins

```

By default it is a not good idea to use default admin credentials.
If you insist - you can change id to 'admin' and password for anything you want.

```yaml
# file: defaults/main.yml

# Jenkins admin token location
jenkins_admin_token_file: '{{ jenkins_home }}/secrets/admin_token'

```

You can specify local place to store Jenkins Admin token.

### Jenkins Configuration

```yaml
# file: defaults/main.yml

# List of required users to create
# jenkins_users:
#   -
#     id: test-user
#     email: test-user@gmail.com
#     password: test-user
jenkins_users: []

```

You can create the required amount of users using this list of dicts.

```yaml
# file: defaults/main.yml

# List of required Jenkins plugins to install
jenkins_plugins:
  - git
  - workflow-aggregator
  - jobConfigHistory
  - ssh
  - ssh-slaves
  - mailer
```

The list of Jenkins plugins which should be installed during installation.

```yaml
# file: defaults/main.yml

# List of Nodes to create\configure
# jenkins_nodes:
#   -
#     name: master
#     type: master
#     labels: master
#     executors: 7
#   -
#     name: test-jnlp
#     executors: 1
#     labels: test-jnlp
#     type: jnlp
#     home_path: /home/jenkins
#     description: 'test-jnlp'
#   -
#     name: test-ssh
#     executors: 1
#     labels: test-ssh
#     type: ssh
#     external_host: 127.0.0.1
#     credentials: jenkins-local-slave
#     home_path: '/var/lib/jenkins'
#     description: 'test-ssh'
#     environment:
#       FOO: bar
#       BAR: foo
jenkins_nodes: []

```

You can create the required slaves using this variable. It also helps to change number of executors for every slave and to manage environment variables for the slaves.

```yaml
# file: defaults/main.yml

# Jenkins user-password pairs credentials
# jenkins_userpass_credentials:
#   -
#     id: test-credentials
#     description: "For test"
#     username: test-credentials-user
#     password: test-credentials-password
jenkins_userpass_credentials: []

```

Using this list of dicts you can create all required username-password pair credentials.

```yaml
# file: defaults/main.yml

# Jenkins secret-text credentials
# jenkins_secret_text_credentials:
#   -
#     id: test-text-credentials
#     description: "For test"
#     secret_text: test-text-credentials
jenkins_secret_text_credentials: []

```

Using this list of dicts you can create all required secret text credentials.

```yaml
# file: defaults/main.yml

# Jenkins SSH credentials
# jenkins_ssh_credentials:
#   -
#     id: test-ssh-user
#     username: test-ssh-user
#     print: True
#     description: "For test"
#   -
#     id: jenkins-local-slave
#     username: jenkins
#     local: True
#     description: "For test"
jenkins_ssh_credentials: []


```

Using this list of dicts you can create all required SSH credentials.

### Jenkins Configuration (unchangable)

```yaml
# file: defaults/main.yml

# Required Python Pip packages
pip_packages:
  - setuptools
  - lxml
  - python-jenkins
  - pyopenssl
  - urllib3

```

The list of Python Pip packages to install.

```yaml
# file: defaults/main.yml

# Pip index URL
pip_index_url: https://pypi.python.org/simple/

```

Full URL to pipy installation simple repository.

Jenkins Process Linux owner.

```yaml
# file: defaults/main.yml

# Jenkins system user
jenkins_system_user: jenkins

```

Jenkins Process Linux owner.

Example Playbook
----------------

### Step 1: add role

Add role name `DovnarAlexander.jenkins` to your playbook file.

### Step 2: if java is not installed on the target host you can use 

If you want to install Java using **[DovnarAlexander/oracle-java](https://galaxy.ansible.com/DovnarAlexander/oracle-java)** playbook - install it with requirements.yml

```
ansible-galaxy install DovnarAlexander.oracle-java
```

### Step 3: add variables

If you need - modify variables your playbook\variables file.

Simple example:

```yaml
---
# file: simple-playbook.yml

- hosts: all

  roles:
    - DovnarAlexander.oracle-java
    - DovnarAlexander.jenkins

  vars:
    jenkins_version: 2.60.3
    jenkins_plugins:
      - git
      - workflow-aggregator
      - jobConfigHistory
      - ssh
      - ssh-slaves
      - powershell
```

### Step 4: add jenkins group in your inventory file

```ini
---
# file:inventory.ini

[jenkins]
your_host

[java:children]
jenkins

```
```yaml
java:
  children:
    jenkins:
      hosts:
        your_host:
```