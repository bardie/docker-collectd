# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

$bootstrap=<<SCRIPT
apt-get update
apt-get -y install python-pip
pip install docker-py
curl -sSL https://get.docker.com/ubuntu/ | sudo sh
gpasswd -a vagrant docker
service docker restart
curl -L https://github.com/docker/compose/releases/download/1.1.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "worker" do |worker|
    worker.vm.box = "ubuntu/trusty64"
    worker.vm.hostname = "worker"
    worker.vm.network :private_network, ip: "192.168.33.10"
    worker.vm.provider "virtualbox" do |vb|
     vb.customize ["modifyvm", :id, "--memory", "2048"]
    end
    worker.vm.provision :shell, inline: $bootstrap
  end

  config.vm.define "monitor" do |monitor|
    monitor.vm.box = "ubuntu/trusty64"
    monitor.vm.hostname = "monitor"
    monitor.vm.network :private_network, ip: "192.168.33.11"
    monitor.vm.provision :shell, inline: $bootstrap
  end

end

