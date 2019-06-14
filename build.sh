git fetch origin
git merge origin/master

pip3 install -r requirements.txt

cd video
python3 manage.py migrate --settings=video.settings_prod
python3 manage.py collectstatic --no-input --settings=video.settings_prod

supervisorctl restart video

service nginx restart

