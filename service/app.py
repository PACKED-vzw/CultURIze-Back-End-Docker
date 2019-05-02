from flask import Flask, request, jsonify, abort
from werkzeug.contrib.profiler import ProfilerMiddleware, MergeStream
from werkzeug.debug import get_current_traceback
from git import Repo

import os, shutil
import sys
import settings
import sys

app = Flask(__name__)


@app.route('/', methods=['POST'])
def endpoint():
    """ All requests from a github webhook should be redirected here."""
    try:
        json = request.get_json(silent=True)
        github_url = json['repository']['html_url']

        htaccess_dir = '/usr/src/app/htaccess/'

        # delete all content of the htaccess directory
        print('delete all content of the htaccess directory')
        for the_file in os.listdir(htaccess_dir):
            file_path = os.path.join(htaccess_dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

        print('remove the git folder if it exists')
        # remove the git folder if it exists
        try:
            shutil.rmtree(os.path.join(htaccess_dir, '.git'))
        except FileNotFoundError:
            print('.git folder does not exist/has not been found, thus it cannot be deleted')

        print('clone the repo to the htaccess')
        # clone the repo to the htaccess
        try:
            Repo.clone_from(github_url, htaccess_dir)
        except Exception as e:
            print(e)
        
        print('pull done')
        return jsonify({
            "Success": True,
        })
    except Exception as e:
        print(e)
        abort(500)


@app.errorhandler(500)
def internal_error(error):
    track = get_current_traceback(skip=1, show_hidden_frames=True,
                                  ignore_system_exceptions=False)

    track.log()

    return jsonify({
        "Success": False,
        "Message": str(error),
        "traceback": str(track.plaintext),
    }),500


if __name__ == '__main__':
    if settings.DEBUG:
        app.config['PROFILE'] = True
        # app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])

    app.run(debug=settings.DEBUG, host='0.0.0.0', port='8000')
