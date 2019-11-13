# Culturize Docker configuration

## Requirements 

### Github account
https://github.com/join

### Git 
Get [git](https://git-scm.com/downloads)

### Docker. 
Choose the right version for your system https://docs.docker.com/install/ 

### Docker-Compose
https://docs.docker.com/compose/install/ 

### Configuration
Before starting:
Either add your user to the docker group on the system or run every next docker command in the README as sudo. To add your user to the docker group run `sudo usermod -aG docker $USER`. 

1. Fork this repository to your account.

1. Clone the repository `git clone https://github.com/username/CultURIze-Back-End-Docker` on your web-server. And enter the "Culturize-Back-End-Docker" directory.

### Nginx or Apache ?
Depending on what webserver you are running, choose the right configuration.

### Nginx

1. Remove or rename the default configuration file for Nginx `(/etc/nginx/sites-enables/default.conf)` if doing this set-up for the first time.


- `sudo rm /etc/nginx/sites-enabled/default.conf`
or

- `sudo mv /etc/nginx/sites-enabled/default.conf /etc/nginx/sites-enabled/default.conf.bak`


2. place the configuration file found in this repository (/CultURIze-Back-End-Docker/docs/nginx-conf/)  in `/etc/nginx/sites-available/` directory on your webserver. 

- `sudo mv /home/user/CultURIze-Back-End-Docker/tree/master/docs/nginx-conf/culturize.conf /etc/nginx/sites-available/`

3. Create symbolic link from /etc/nginx/sites-available to /etc/nginx/sites-enabled/ like so:

- `cd /etc/nginx/sites-enabled`
- `sudo ln -s ../sites-available/culturize.conf .`
    
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

 <!-- (configure your Apache/Nginx to redirect a webhook url to the localhost:8000 and configure all traffic which is not /github/ towards our new redirection file uploaded from github.)
-->

### Apache

1. Remove or rename the default configuration file for Apache2 `(/etc/apache2/sites-enables/000-default.conf)` 

- `sudo rm /apache2/nginx/sites-enabled/000-default.conf`
or

- `sudo mv /etc/apache2/sites-enabled/000-default.conf /etc/nginx/sites-enabled/000-default.conf.bak`

2. place the configuration file found in this repository (/CultURIze-Back-End-Docker/docs/apache2-conf/)  in `/etc/nginx/sites-available/` directory on your webserver. 
- `sudo mv /home/user/CultURIze-Back-End-Docker/tree/master/docs/apache-conf/culturize.conf /etc/apache2/sites-available/`

3. Create symbolic link from /etc/apache2/sites-available to /etc/apache2/sites-enabled/ 

- `cd /etc/apache2/sites-enabled`
- `sudo ln -s ../sites-available/culturize.conf .`
 
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`


### For Apache, enable http_proxy mod:
By running `a2enmod proxy` abd `a2enmod proxy_http` in your terminal
[More information](https://www.digitalocean.com/community/tutorials/how-to-rewrite-urls-with-mod_rewrite-for-apache-on-ubuntu-16-04)

- `sudo cp /home/user/CultURIze-Back-End-Docker/tree/master/docs/nginx-conf/culturize.conf /etc/nginx/sites-available/`

3. Create symbolic link from /etc/nginx/sites-available to /etc/nginx/sites-enabled/ like so:

- `cd /etc/nginx/sites-enabled`
- `sudo ln -s ../sites-available/culturize.conf .`
    
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

 <!-- (configure your Apache/Nginx to redirect a webhook url to the localhost:8000 and configure all traffic which is not /github/ towards our new redirection file uploaded from github.)
-->

### Apache

1. Remove or rename the default configuration file for Apache2 `(/etc/apache2/sites-enables/000-default.conf)` 

- `sudo rm /apache2/nginx/sites-enabled/000-default.conf`
or

- `sudo mv /etc/apache2/sites-enabled/000-default.conf /etc/nginx/sites-enabled/000-default.conf.bak`

2. place the configuration file found in this repository (/CultURIze-Back-End-Docker/docs/apache2-conf/)  in `/etc/nginx/sites-available/` directory on your webserver. 
- `sudo cp /home/user/CultURIze-Back-End-Docker/tree/master/docs/nginx-conf/culturize.conf /etc/nginx/sites-available/`

3. Create symbolic link from /etc/apache2/sites-available to /etc/apache2/sites-enabled/ 

- `cd /etc/apache2/sites-enabled`
- `sudo ln -s ../sites-available/culturize.conf .`
 
4. Run the `docker-compose build` command from inside the cloned repository to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`


> Note, for Apache, enable http_proxy mod by running `a2enmod proxy` abd `a2enmod proxy_http` in your terminal
>>>>>>> 8989d2dcc343abd0b4737d6dc2db798368761ec5

### Configuring the Webhook

### Configuring the Webhook

7. Our next step is to add our newly created webhook `http://SERVER_IP/github/` to github. 
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
on the server in your repository the folder apache-htaccess getting filled with information.
<!--
8. Our last step is to configure all traffic which is not /github/ towards our new redirection file uploaded
 from github. 
 

For nginx:
You can do this by adding the following lines to the file `/etc/nginx/conf.d/culturize.conf`. This rule forwards all traffic which is not /github/ towards
port 801 of our local machine, where our apache culturize redirection rules resides.

```
server {
    listen 80;
    listen [::]:80;

    location /github/ {
            proxy_pass http://127.0.0.1:8000/;
    }

    location / {
           proxy_pass http://127.0.0.1:801/;
    }
}
```


For Apache2:
```
<VirtualHost *:80>
    ProxyPreserveHost On
    ProxyRequests Off

    ProxyPass /github/ http://127.0.0.1:8000/
    ProxyPassReverse /github/ http://127.0.0.1:8000/

    ProxyPass / http://127.0.0.1:801/
    ProxyPassReverse / http://127.0.0.1:801/
</VirtualHost>
```
-->

****
## Removing the configuration
1. Run the command `docker-compose stop` inside the repository folder of the culturize docker
2. Run the command `docker-compose rm` inside the repository folder
3. Run the command `docker-compose rmi` inside the repository folder
