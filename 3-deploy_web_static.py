#!/usr/bin/python3
'''Fabric script that generates a .tgz(zipped, tar) archive
   comprised of web static content '''

from fabric.api import *
import os.path
from datetime import datetime
from time import strftime
env.hosts = ['66.70.184.164', '142.44.164.121']


def do_pack():
    ''' Method archives files and returns path of archive '''
    time_created = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    directory_created = local('mkdir -p versions')
    archive = local('tar -cvzf versions/web_static_{}.tgz web_static'
                    .format(time_created))

    if archive is not None:
        return ('versions/web_static.{}'.format(time_created))
    else:
        return None


def do_deploy(archive_path):

    '''Method deploys an archive to a web server
    and uncomporesses it to a folder '''

    if (os.path.isfile(archive_path) is False):
        return False

    try:
        ''' Unpacks compressed file / Uploads file to /tmp directory
        of web server '''

        put(archive_path, "/tmp/")
        unpack = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + unpack.split(".")[0])

        run("sudo mkdir -p {:s}".format(folder))

        ''' Uncompress <archive filename without extension> to created
        folder - /data/web_static/releases/ on the web server '''

        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(unpack, folder))

        ''' Deletes the archive from the web server '''
        run("sudo rm /tmp/{:s}".format(unpack))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))

        ''' Delete the symbolic link /data/web_static/current '''
        run('sudo rm -rf /data/web_static/current')

        ''' Create a new the symbolic link /data/web_static/current on the web
        server, linked to the new version of your code
        (/data/web_static/releases/<archive filename without extension>) '''

        run("sudo ln -s {:s} /data/web_static/current".format(folder))
        return True
    except:
        return False


def deploy():

        ''' Method that creates and distributes an archive to your web servers,
        using the function deploy '''

        new_archive_path = do_pack()
        if new_archive_path is None:
            return False
        deployed = do_deploy(new_archive_path)
        return deployed
