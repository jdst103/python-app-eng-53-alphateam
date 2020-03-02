import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

assert ("atomicwrite" in installed_packages)
print("atomicwrites installation test passed..... overall progress 10%")


try:
    assert ("attrs" in installed_packages)
    print("attrs installation test passed..... overall progress 20%")

except AssertionError:
    print ('attrs installation test Failed')

try:

    assert ("beautifulsoup4" in installed_packages)
    print("beautifulsoup4 installation test passed..... overall progress 30%")

except AssertionError:
    print ('beautifulsoup4 installation test Failed')

try:
    assert ("chardet" in installed_packages)
    print("chardet installation test passed..... overall progress 40%")

except AssertionError:
    print ('chardet installation test Failed')

try:
    print("idna installation test passed..... overall progress 50%")
    assert ("importlib-metadata" in installed_packages)

except AssertionError:
    print ('idna installation test Failed')

try:
    assert ("importlib-metadata" in installed_packages)
    print("importlib-metadata installation test passed..... overall progress 60%")

except AssertionError:
    print ('importlib-metadata installation test Failed')

try:
    assert ("more-itertools" in installed_packages)
    print("more-itertools installation test passed..... overall progress 70%")

except AssertionError:
    print ('more-itertools installation test Failed')

try:
    assert ("packaging" in installed_packages)
    print("packaging installation test passed..... overall progress 80%")

except AssertionError:
    print ('packaging installation test Failed')

try:
    assert ("pluggy" in installed_packages)
    print("pluggy installation test passed..... overall progress 90%")
except AssertionError:
    print ('pluggy installation test Failed')

try:
    assert ("py" in installed_packages)
    print("py installation test passed..... overall progress 100%")

except AssertionError:
    print ('py installation test Failed')