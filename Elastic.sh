#!/bin/bash
cd ~
sudo apt-get -y update
#Java Install
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer
cd ~
mkdir scripts
#Add to system values!
touch ~/scripts/javadir.d
if [ -f ~/.profile ]; then
  echo "Profile exists!"
else
  cp /etc/skel/.profile ~/.profile
fi
cp ~/.profile ~/.profile_backup
echo 'JAVA_HOME="/usr/lib/jvm/java-8-oracle"'> ~/scripts/javadir.d
echo 'JRE_HOME="/usr/lib/jvm/java-8-oracle/jre"'> ~/scripts/javare.d
cat ~/.profile_backup ~/scripts/javadir.d > ~/.profile
source ~/.profile
cat ~/.profile_backup ~/scripts/javare.d > ~/.profile
source ~/.profile
#Done. 
rm -rf scripts
#Elastic install
curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.1.tar.gz
tar -xvf elasticsearch-5.5.1.tar.gz
cd elasticsearch-5.5.1/bin
sudo chmod +x ./elasticsearch
./elasticsearch
