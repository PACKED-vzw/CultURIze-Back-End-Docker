from flask import Flask, request, jsonify, abort
from werkzeug.contrib.profiler import ProfilerMiddleware, MergeStream
from werkzeug.debug import get_current_traceback
import git

import os, shutil
import sys
import settings
import sys
import glob

app = Flask(__name__)

#finds out of a folder is a git folder
def is_git_repo(folder):
    return os.path.isdir(os.path.join(folder, '.git'))

#removes folder and its content
def remove_folder(folder):
    for file in os.listdir(folder):
        filepath = os.path.join(folder,file)
        print(filepath)
        if os.path.isfile(filepath):
            os.unlink(filepath)
    os.rmdir(folder)

#route of web app
@app.route('/', methods=['POST'])
def endpoint():
    """ All requests from a github webhook should be redirected here."""
    try:
        json = request.get_json(silent=True)
        github_url = json['repository']['clone_url']

        htaccess_dir = '/usr/src/app/htaccess/'
        temp_dir = '/usr/src/app/temp'

        # clone the repo to the htaccess
        if is_git_repo(htaccess_dir):
            print('htaccess is a git repository')
            print('pull the git repository')
            try:
                git.Repo(htaccess_dir).remotes.origin.pull()
                print('pull done')

            except Exception as e:
                print(e)
    
        else:
            try:
                print('htaccess is not a git folder')
                print('clone the repo to a temporary folder')
                git.Repo.clone_from(github_url, temp_dir)
                print('clone done')
                print('copy files of temporary folder to htaccess')
                shutil.copytree(temp_dir,htaccess_dir,dirs_exist_ok=True)
                remove_folder(temp_dir)
                print('temporary folder removed')
                print('done')
            except Exception as e:
                print(e)

        print('pull done')
        return jsonify({
            "Success": True,
            "Files added": json['head_commit']['added'],
            "Files removed": json['head_commit']['removed'],
            "Files modified": json['head_commit']['modified']
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
