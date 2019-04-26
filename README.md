

# Culturize Docker configuration ( under construction )

1. Install Docker on your linux server

2. Install docker-compose

3. clone this repository 'git clone https://github.com/PACKED-vzw/CultURIze-Back-End-Docker'

4. Start the containers which will do the redirection with the command
Deze command gaat de specifieke docker containers aanmaken 
> docker-compose build

5. docker-compose up -d
Deze command gaat de docker containers starten. 

6. Configure your Apache/Nginx to redirect a webhook url to the localhost:8000

For Nginx:
Make a new configuration file in `/etc/nginx/conf.d/` and name it culturize.conf with these contents

```
server {
    listen 80;
    listen [::]:80;

        location /github/ {
                proxy_pass http://127.0.0.1:8000/;}
        } 
```          


Apache2 Example:
<VirtualHost example.com:80>
    ProxyPreserveHost On
    ProxyRequests Off
    ServerName www.example.com
    ServerAlias example.com
    ProxyPass /my-webhook http://127.0.0.1:8000
    ProxyPassReverse /my-webhook http://127.0.0.1:8000
</VirtualHost>

This needs to be added in the apache2 configuration file at  '/etc/apache2/apache2.conf' 

5. Add a webhook to github towards the "http://www.example.com/my-webhook"
https://www.youtube.com/watch?v=S9cjO6V7EXg

toevoegen van ip adres content type veranderen naar json

(Uitleg toevoegen)
6. Add the domain for which you want to culture redirect to happen to Apache/Nginx
<VirtualHost redirectdomain.com:80>
    ProxyPreserveHost On
    ProxyRequests Off
    ServerName www.redirectdomain.com
    ServerAlias redirectdomain.com
    ProxyPass / http://127.0.0.1:8080
    ProxyPassReverse / http://127.0.0.1:8080
</VirtualHost>


Remove the configuration: 
1.
2.
3.
