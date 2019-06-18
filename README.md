# Culturize Docker configuration
1. Install Docker. 
Choose the right version for your system https://docs.docker.com/install/ 

2. Install Docker compose https://docs.docker.com/compose/install/ 
 
3. clone this repository `git clone https://github.com/PACKED-vzw/CultURIze-Back-End-Docker` on your web-server. And enter the "Culturize-Back-End-Docker" directory.

4. Run the `docker-compose build` command to create the docker containers. 

5. Start the docker containers with `docker-compose up -d`

6. Configure your Apache/Nginx to redirect a webhook url to the localhost:8000 and configure all traffic which is not /github/ towards our new redirection file uploaded from github. 

For Nginx:
Make a new configuration file in `/etc/nginx/sites-available/` and name it culturize.conf with these contents

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
Create symbolic link from /etc/nginx/sites-available to /etc/nginx/sites-enabled/
```
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/culturize.conf .
``` 

For Apache2:
Make a new configuration file in `/etc/apache2/sites-available` and name it culturize.conf with thesse contents
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
Create symbolic link from /etc/apache2/sites-available to /etc/apache2/sites-enabled/ 
```
cd /etc/apache2/sites-enabled
sudo ln -s ../sites-available/culturize.conf .
``` 
> Note, for Apache, enable http_proxy mod by running `a2enmod proxy` abd `a2enmod proxy_http` in your terminal

> Note, do not forget to remove the default configuration file for Nginx/Apache if doing a fresh install. 

7. Our next step is to add our newly created webhook `http://SERVER_IP/github` to github. 
To achieve this, go to your github project, in the project menu navigate to settings.
Then in the your settings menu, situated on the left of the screen, select webhooks
then 'add a webhook'. On this page you can fill in:
 * **payload url :** with your newly created webhook url `http://SERVER_IP/github`
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
# Remove the configuration
1. Run the command `docker-compose stop` inside the repository folder of the culturize docker
2. Run the command `docker-compose rm` inside the repository folder
3. Run the command `docker-compose rmi` inside the repository folder
