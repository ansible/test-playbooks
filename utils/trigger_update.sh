#!/usr/bin/env bash

cat << EOF > ~/git_ssh
#/usr/bin/env bash
exec /usr/bin/ssh -o StrictHostKeyChecking=no -i $GIT_KEY "\$@"
EOF

chmod a+x ~/git_ssh
export GIT_SSH=~/git_ssh

TMPFILE='random'$RANDOM
git checkout inventory_additions
touch $TMPFILE
git add $TMPFILE
git commit -m "Adding temporary file $TMPFILE"
git push -f git@github.com:ansible/test-playbooks.git inventory_additions
git rm $TMPFILE
git commit -m "Removing temporary file $TMPFILE"
git push -f git@github.com:ansible/test-playbooks.git inventory_additions
