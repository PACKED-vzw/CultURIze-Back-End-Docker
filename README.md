# Culturize Docker configuration

## Requirements 

* [Git](https://git-scm.com/downloads)
* [Docker](https://docs.docker.com/install/)
* [Docker-Compose](https://docs.docker.com/compose/install/) 
* Server with [Apache2](https://httpd.apache.org/) or [Nginx](https://nginx.org/). The server needs to have at least a public [IP address](https://en.wikipedia.org/wiki/IP_address)

## Configuration
Before starting:
Either add your user to the docker group on the system or run every next docker command in the README as sudo. To add your user to the docker group run `sudo usermod -aG docker $USER`. 

1. Clone this [repository](https://github.com/PACKED-vzw/CultURIze-Back-End-Docker) to your webserver: 
 `git clone https://github.com/username/CultURIze-Back-End-Docker` 
 
 2. And enter the directory of the cloned repository: `cd CultURIze-Back-End-Docker`

### Apache or Nginx?
Depending on what webserver you are running, choose the right configuration.

#### Nginx

1. Remove or rename the default configuration file for Nginx `(/etc/nginx/sites-enables/default.conf)` if doing this set-up for the first time.
    - `sudo rm /etc/nginx/sites-enabled/default.conf` or
    - `sudo mv /etc/nginx/sites-enabled/default.conf /etc/nginx/sites-enabled/default.conf.bak`

2. place the configuration file found in this repository (/CultURIze-Back-End-Docker/docs/nginx-conf/)  in `/etc/nginx/sites-available/` directory on your webserver. 
    - `sudo mv /home/user/CultURIze-Back-End-Docker/docs/nginx-conf/culturize.conf /etc/nginx/sites-available/`

3. Create symbolic link from /etc/nginx/sites-available to /etc/nginx/sites-enabled/ like so:
    - `cd /etc/nginx/sites-enabled`
    - `sudo ln -s ../sites-available/culturize.conf .`
    
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

#### Apache

1. Remove or rename the default configuration file for Apache2 `(/etc/apache2/sites-enables/000-default.conf)` 
    - `sudo rm /apache2/sites-enabled/000-default.conf` or
    - `sudo mv /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf.bak`

2. place the configuration file found in this repository (/CultURIze-Back-End-Docker/docs/apache2-conf/)  in `/etc/apache2/sites-available/` directory on your webserver. 
    - `sudo mv /home/user/CultURIze-Back-End-Docker/docs/apache2-conf/culturize.conf /etc/apache2/sites-available/`

3. Create symbolic link from /etc/apache2/sites-available to /etc/apache2/sites-enabled/ 
    - `cd /etc/apache2/sites-enabled`
    - `sudo ln -s ../sites-available/culturize.conf .`
    
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

6. enable http_proxy mod and restart your webserver by typing following commands in your terminal [More information](https://www.digitalocean.com/community/tutorials/how-to-rewrite-urls-with-mod_rewrite-for-apache-on-ubuntu-16-04)

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2.service
```

### Configuring the Webhook

Our next step is to add our newly created webhook `http://SERVER_IP/github/` to github. 
To achieve this, go to your github project, in the project menu navigate to settings.
Then in the your settings menu, situated on the left of the screen, select webhooks
then 'add a webhook'. On this page you can fill in:
 * **payload url :** with your newly created webhook url `http://SERVER_IP/github/`
 * **content-type :** can be set to `application/json`
 * **secret :** may be left empty
 * **Which events would you like to trigger this webhook? :** set this to 'just push events'
 * Finaly make sur that the active checkbox is checked.
Once this is saved each time you will push to your repository a POST method will be
issued to your webhook with informations regarding the push event.

To check if it works you can push a change to your repository and you should notice
on the server in your repository the folder apache-htaccess getting filled with the htaccess-files.

## Start creating PIDs with the CultURIze tool
You're all set now! Everytime you'll upload PIDs to the repository for which you congured the webhook, it will automatically be published at [http://your-server-IP/$subdirectory/$PID](http://your-server-IP/subdirectory/PID), e.g. http://example.org/rembrand/work/1

## Removing the configuration
1. Run the command `docker-compose stop` inside the repository folder of the culturize docker
2. Run the command `docker-compose rm` inside the repository folder
3. Run the command `docker-compose rmi` inside the repository folder
