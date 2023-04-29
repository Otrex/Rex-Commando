from os import remove
"""
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1	localhost
127.0.0.1       projects
255.255.255.255	broadcasthost
::1             localhost
# Added by Docker Desktop
# To allow the same kube context to work on the host and the container:
127.0.0.1 kubernetes.docker.internal
# End of section
"""

TEMP_FILE_PATH = "var/temp/tmp"
DEFAULT_UNIX_HOSTS_PATHS = "/etc/hosts"
DEFAULT_INSTALLATION_PATH = "var/store"
DEFAULT_INSTALLATION_FILE_NAME = "__etc_hosts__.conf"
DEFAULT_INSTALLATION_FILE_PATH = f"{DEFAULT_INSTALLATION_PATH}/{DEFAULT_INSTALLATION_FILE_NAME}"

def clearTempFile():
  remove(TEMP_FILE_PATH)

def prepend_to_temp_file(file_path, line):
  with open(file_path, 'r') as f:
      content = f.readlines()
  content.insert(0, line)
  with open(TEMP_FILE_PATH, 'w') as f:
    f.writelines(content)