name="webdriver-w3c-tests"
main_version="6.35.1.2"
release="1"
version="6.35.1.2"
appname=$(echo $name|sed 's/-/_/g')

# set value "1" if this suite need to sign,otherwise set "0" #
sign="0"

# set value "1" if this suite need to remove src_file,otherwise set "0" #
src_file="1"

# specified files to be removed in blacklist #
blacklist="
pack.sh
webdriver-w3c-tests.spec
support
crosswalk
key
signing
make_xpk.py"
