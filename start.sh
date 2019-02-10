for url in `cat $1`;do
    python GitHack.py $url
    python CheckResult.py $url
done
