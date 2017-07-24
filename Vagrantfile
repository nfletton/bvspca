# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  if ENV['VAGRANT_BASE_BOX_16_04']
    config.vm.box = ENV['VAGRANT_BASE_BOX_16_04']
  else
    config.vm.box = "xenial64"
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = ENV['HOME'] + "/ansible-playbooks/django-dev.yml"
    ansible.sudo = true
    ansible.extra_vars = ENV['HOME'] + "/ansible-playbooks/host_vars/dev.bowvalleyspca.org.yml"
  end
  config.vm.synced_folder ".", "/home/vagrant/bowvalleyspca_org", type: "nfs"
  config.vm.network "private_network", ip: "10.0.0.101"
  config.vm.network "forwarded_port", host: 5000, guest: 8000
  config.vm.provider "virtualbox" do |v|
    v.name = "bowvalleyspca_org"
  end
end
