#!/usr/bin/python3
"""generate .tgz archive from contents of web_static folder"""

import fabric
import os
import datetime

# fabric.api.env.hosts = ['35.196.235.59', '35.237.139.72']


def do_pack():
    """use fabric to generate a .tgz file from the given directory"""
    if os.path.isdir('versions') is False:
        os.mkdir('versions')
    time_stamp = datetime.datetime.now().strftime('%Y%-m%d%H%M%S')
    file = "versions/web_static_" + time_stamp + ".tgz"
    fabric.api.local("tar -cvzf {} web_static/".format(file))
    return file


def do_deploy(archive_path):
    """distribute archive to ws"""
    if archive_path is None:
        return False
    file_name = 'web_static_' + archive_path[-17:-4]
    fabric.operations.put(archive_path, '/tmp/')

    fabric.operations.run(
        "mkdir -p /data/web_static/releases/{}"
        .format(file_name))
    fabric.operations.run(
        "tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
        .format(file_name, file_name))
    fabric.operations.run(
        "rm /tmp/{}.tgz"
        .format(file_name))
    fabric.operations.run(
        "mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/"
        .format(file_name, file_name))
    fabric.operations.run(
        "rm -rf /data/web_static/releases/{}/web_static"
        .format(file_name))
    fabric.operations.run("rm -rf /data/web_static/current")
    fabric.operations.run(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(file_name))
    return True


def deploy():
    """comment about what it does"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
