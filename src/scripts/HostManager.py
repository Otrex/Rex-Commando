import os
from CommandExecutor import Executor
from errors import SupportedOSException
from utils import *

CACHE_PASSWORD = None

class HostsManager:
  @staticmethod
  def getHostPath():
    if (os.name == 'posix'):
      return DEFAULT_UNIX_HOSTS_PATHS
    else:
      raise SupportedOSException("os not supported")

  @staticmethod
  def write_to_host(content, from_path):
    prepend_to_temp_file(from_path, content)
    result = Executor.sudo_executor(
      f"cp {TEMP_FILE_PATH} {HostsManager.getHostPath()}", 
      CACHE_PASSWORD
    )
    if len(result.error) == 0 or result.error[0] == 'Password:':
      clearTempFile()
    else:
      raise Exception(result.error)

  @staticmethod
  def install(save_to_store = None):
    path = HostsManager.getHostPath()
    
    if os.path.exists(path):
      with open(path, 'r') as f:
        contents = f.read()
        if save_to_store:
          save_to_store(contents)
        else:
          if not os.path.exists(DEFAULT_INSTALLATION_PATH):
            os.makedirs(DEFAULT_INSTALLATION_PATH)
            
          with open(DEFAULT_INSTALLATION_FILE_PATH, 'w') as fn:
            fn.write(contents)
    else:
        raise FileNotFoundError("Hosts file not found")

  @staticmethod
  def add_domain(domain, ip):
    new_content = f"##\n# Added By Host Manager \n{ip}\t{domain}\n"
    HostsManager.write_to_host(new_content, HostsManager.getHostPath())

  @staticmethod
  def reset_hosts():
    HostsManager.write_to_host("", DEFAULT_INSTALLATION_FILE_PATH)


if __name__ == '__main__':
  CACHE_PASSWORD = "obisiket1"
  HostsManager.install()
  HostsManager.add_domain("obi.com", "127.0.0.1")
  HostsManager.reset_hosts()

  r = Executor.executor("cat /etc/hosts")
  print("\n".join(r.output))