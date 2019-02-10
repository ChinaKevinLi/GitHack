for ip in `cat $1`;do
    python GitHack.py http://${ip}/.git/
    python CheckResult.py http://${ip}/.git/
done
